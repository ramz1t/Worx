from time import strftime, gmtime

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
    '''
    класс для вывода json'ов в более менее удобном формате
    '''

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
                for smting in value:
                    output +=\
                        '\n'+'\t'*recnum + key + ' : ' + JsonOutput(**smting).__repr__(recnum + 1)
            else:
                output +=\
                    '\n' + '\t' * recnum + key + " : " + str(value) + '\n'
        return output


class UserStats:

    def __init__(self, args):
        '''
        класс для организации статов из функций get_repo_contributors_stats и get_repo_yearly_stats
        '''
        self.stats = {}
        for kwargs in args:
            if kwargs.get('author') is None:
                date = kwargs.get('week')
                days_stats = kwargs.get('days')
                for i in range(len(days_stats)):
                    day, number, month, year =\
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
                    day, number, month, year =\
                        map(str, strftime("%a %d %b %Y", gmtime(stat.get('w'))).split())
                    number = str(int(number))
                    if self.stats.get(year) is None:
                        self.stats[year] = generate_year_dict(year)
                    self.stats[year][month][number] =\
                        {
                            'additions': stat.get('a'),
                            'deletions': stat.get('d'),
                            'commits': stat.get('c')
                        }
