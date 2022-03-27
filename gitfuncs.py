import requests

from classes import JsonOutput


def get_urls(filename):
    urls = {}
    with open(filename + '.txt', 'r') as f:
        fileinput = f.read().split('\n')[:-1]
        for url in fileinput:
            key, value = url.split(' ')
            urls[key] = value
        return urls


def write_urls(filename, data):
    with open(filename + '.txt', 'w') as f:
        # urls = {key: 'f\''+str(value).replace('{/','{')+'\'' for key, value in data.items() if key.find('url') != -1}
        urls = {key: str(value).replace('{/', '{') for key, value in data.items() if
                key.find('url') != -1}
        for key, value in urls.items():
            f.write(key + ' ' + value + '\n')


def get_user(Auth_params):
    user = requests.get('https://api.github.com/user', auth=Auth_params).json()
    write_urls('users_urls', user)
    return user


def get_user_repos(Auth_params):
    urls = get_urls('users_urls')
    repos = requests.get(urls['repos_url'], auth=Auth_params).json()
    for repo in repos:
        write_urls(repo['name'], repo)
        # print(JsonOutput(**repo))
    return repos


def get_repo_issues(Auth_params, repo_name, id=None):
    urls = get_urls(repo_name)
    url = urls['issues_url'][:urls['issues_url'].find('{')]
    issues = requests.get(url, auth=Auth_params).json()
    if id is None:
        return issues
    return issues[id]


def get_repo_branches(Auth_params, repo_name):
    urls = get_urls(repo_name)
    url = urls['branches_url'][:urls['branches_url'].find('{')]
    branches = requests.get(url, auth=Auth_params).json()
    return branches


def get_repo_commits(Auth_params, repo_name, info=False):
    urls = get_urls(repo_name)
    url = urls['commits_url'][:urls['commits_url'].find('{')]
    commits = requests.get(url, auth=Auth_params).json()
    if info:
        for commit in commits:
            commitinfo = requests.get(commit['url'], auth=Auth_params).json()
            return commitinfo
    return commits


def get_repo_comment(Auth_params, repo_name):
    urls = get_urls(repo_name)
    url = urls['comments_url'][:urls['comments_url'].find('{')]
    comments = requests.get(url, auth=Auth_params).json()
    return comments


def get_repo_pulls(Auth_params, repo_name):
    urls = get_urls(repo_name)
    url = urls['pulls_url'][:urls['pulls_url'].find('{')]
    pulls = requests.get(url, auth=Auth_params).json()
    return pulls


def get_repo_subs(Auth_params, repo_name):
    urls = get_urls(repo_name)
    url = urls['subscribers_url']
    subs = requests.get(url, auth=Auth_params).json()
    return subs


def get_repo_contributors(Auth_params, repo_name):
    urls = get_urls(repo_name)
    url = urls['contributors_url']
    contributors = requests.get(url, auth=Auth_params).json()
    return contributors


def get_user_repo_stats(Auth_params, repo_name):
    url=f'https://api.github.com/repos/{Auth_params[0]}/{repo_name}/community/profile'

    '''
    return all community profile metrics, including an overall health score, repository description, the presence of 
    documentation, detected code of conduct, detected license, and the presence of ISSUE_TEMPLATE
    , PULL_REQUEST_TEMPLATE, README, and CONTRIBUTING files.
    '''

    url=f'https://api.github.com/repos/{Auth_params[0]}/{repo_name}/stats/code_frequency'

    '''
    Returns a weekly aggregate of the number of additions and deletions pushed to a repository.
    '''

    url=f'https://api.github.com/repos/{Auth_params[0]}/{repo_name}/stats/contributors'

    '''
    Returns the total number of commits authored by the contributor. 
    In addition, the response includes a Weekly Hash (weeks array) with the following information:

        w - Start of the week, given as a Unix timestamp.
        a - Number of additions
        d - Number of deletions
        c - Number of commits
    '''
    stats = requests.get(url, auth=Auth_params).json()
    print(stats)
    #for stat in stats:
    #    print(JsonOutput(**stat))
