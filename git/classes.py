from time import strftime, gmtime

from git.gitfuncs import get_user, get_user_repos, get_repo_contributors_stats

DAY_DUR = 24 * 60 * 60


def generate_year_dict(year):
    months = {
        'Jan': 31,
        'Feb': 28,
        'Mar': 31,
        'Apr': 30,
        'May': 31,
        'Jun': 30,
        'Jul': 31,
        'Aug': 31,
        'Sep': 30,
        'Oct': 31,
        'Nov': 30,
        'Dec': 31
    }
    # days = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    if int(year) % 4 == 0:
        months['Feb'] = 29
    return {key: {str(i): {} for i in range(1, value + 1)} for key, value in months.items()}


class JsonOutput:
    """
    класс для вывода json'ов в более менее удобном формате
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[key] = value

    def __repr__(self, recnum=0) -> str:
        output = ""
        for key, value in self.__dict__.items():
            if type(value) == dict:
                output += \
                    '\n' + '\t' * recnum + key + ' : \n' + JsonOutput(**value).__repr__(recnum + 1)
            elif type(value) == list or type(value) == set:
                for something in value:
                    if type(something) != list or type(something) != set:
                        output += \
                            '\n' + '\t' * recnum + key + ' : ' + str(something)
                    else:
                        output += \
                            '\n' + '\t' * recnum + key + ' : ' + JsonOutput(**something).__repr__(recnum + 1)
            else:
                output += \
                    '\n' + '\t' * recnum + key + " : " + str(value) + '\n'
        return output


class UserStats:

    def __init__(self, **kwargs):
        """
        класс для организации статов из функций get_repo_contributors_stats и get_repo_yearly_stats
        """
        self.stats = {}
        if kwargs.get('author') is None:
            date = kwargs.get('week')
            days_stats = kwargs.get('days')
            for i in range(len(days_stats)):
                day, number, month, year = \
                    map(str, strftime("%a %d %b %Y", gmtime(date + DAY_DUR * i)).split())
                number = str(int(number))
                if self.stats.get(year) is None:
                    self.stats[year] = generate_year_dict(year)
                self.stats[year][month][number] = {day: days_stats[i]}
                print(day, number, month, year)
        else:
            self.username = kwargs.get('author').get('login')
            stats = kwargs.get('weeks')
            for stat in stats:
                day, number, month, year = \
                    map(str, strftime("%a %d %b %Y", gmtime(stat.get('w'))).split())
                number = str(int(number))
                if self.stats.get(year) is None:
                    self.stats[year] = generate_year_dict(year)
                self.stats[year][month][number] = \
                    {
                        'additions': stat.get('a'),
                        'deletions': stat.get('d'),
                        'commits': stat.get('c')
                    }

    def __repr__(self):
        return JsonOutput(**self.__dict__).__repr__()


class User:
    login: str
    id: int
    avatar_url: str
    repos: list

    def __init__(self, auth_params=None, username='', **kwargs):
        if len(kwargs) == 0:
            user_info = get_user(auth_params, username)
            self.login = user_info.get('login')
            self.id = int(user_info.get('id'))
            self.avatar_url = user_info.get('avatar_url')
            self.repos = []
            user_repos = get_user_repos(auth_params,username)
            for repo in user_repos:
                self.repos.append(Repo(auth_params, **repo))
        else:
            self.login = kwargs.get('login')
            self.id = kwargs.get('id')
            self.avatar_url = kwargs.get('avatar_url')

    def __repr__(self):
        return JsonOutput(**self.__dict__).__repr__()


class Repo:
    name: str
    id: int
    owner: User
    contributors: dict

    def __init__(self, auth_params, **kwargs):
        self.name = kwargs.get('name')
        self.id = kwargs.get('id')
        self.owner = User(**kwargs.get('owner'))
        self.contributors = {}
        for stat in get_repo_contributors_stats(auth_params, self.name,self.owner.login):
            self.contributors[stat['author']['login']] = UserStats(**stat)

    def __repr__(self):
        return JsonOutput(**self.__dict__).__repr__()
