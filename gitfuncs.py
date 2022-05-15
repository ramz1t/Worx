import requests


def get_urls(filename):
    urls = {}
    with open(filename + '.txt', 'r') as file:
        fileinput = file.read().split('\n')[:-1]
        for url in fileinput:
            key, value = url.split(' ')
            urls[key] = value
        return urls


def write_urls(filename, data):
    with open(filename + '.txt', 'w') as file:
        urls = {key: str(value).replace('{/', '{') for key, value in data.items() if
                key.find('url') != -1}
        for key, value in urls.items():
            file.write(key + ' ' + value + '\n')


def get_user(auth_params):
    user = requests.get('https://api.github.com/user', auth=auth_params).json()
    write_urls('users_urls', user)
    return user


def get_user_repos(auth_params):
    urls = get_urls('users_urls')
    repos = requests.get(urls['repos_url'], auth=auth_params).json()
    for repo in repos:
        write_urls(repo['name'], repo)
        # print(JsonOutput(**repo))
    return repos


def get_repo_issues(auth_params, repo_name, issue_id=None):
    urls = get_urls(repo_name)
    url = urls['issues_url'][:urls['issues_url'].find('{')]
    issues = requests.get(url, auth=auth_params).json()
    if issue_id is None:
        return issues
    return issues[issue_id]


def get_repo_branches(auth_params, repo_name):
    urls = get_urls(repo_name)
    url = urls['branches_url'][:urls['branches_url'].find('{')]
    branches = requests.get(url, auth=auth_params).json()
    return branches


def get_repo_commits(auth_params, repo_name, info=False):
    urls = get_urls(repo_name)
    url = urls['commits_url'][:urls['commits_url'].find('{')]
    commits = requests.get(url, auth=auth_params).json()
    if info:
        commitinfo = []
        for commit in commits:
            commitinfo.append(requests.get(commit['url'], auth=auth_params).json())
        return commitinfo
    return commits


def get_repo_comment(auth_params, repo_name):
    urls = get_urls(repo_name)
    url = urls['comments_url'][:urls['comments_url'].find('{')]
    comments = requests.get(url, auth=auth_params).json()
    return comments


def get_repo_pulls(auth_params, repo_name):
    urls = get_urls(repo_name)
    url = urls['pulls_url'][:urls['pulls_url'].find('{')]
    pulls = requests.get(url, auth=auth_params).json()
    return pulls


def get_repo_subs(auth_params, repo_name):
    urls = get_urls(repo_name)
    url = urls['subscribers_url']
    subs = requests.get(url, auth=auth_params).json()
    return subs


def get_repo_contributors(auth_params, repo_name):
    urls = get_urls(repo_name)
    url = urls['contributors_url']
    contributors = requests.get(url, auth=auth_params).json()
    return contributors


def get_repo_yearly_stats(auth_params, repo_name):
    url = f'https://api.github.com/repos/{auth_params[0]}/{repo_name}/stats/commit_activity'
    yearly_stats = requests.get(url, auth=auth_params).json()
    return yearly_stats


def get_repo_contributors_stats(auth_params, repo_name):
    url = f'https://api.github.com/repos/{auth_params[0]}/{repo_name}/stats/contributors'
    contributors_stats = requests.get(url, auth=auth_params).json()
    return contributors_stats


def get_user_repo_weekly_stats(auth_params, repo_name):
    url = f'https://api.github.com/repos/{auth_params[0]}/{repo_name}/stats/code_frequency'
    weekly_stats = requests.get(url, auth=auth_params).json()
    return weekly_stats


def get_user_repo_stats(auth_params, repo_name):
    url = f'https://api.github.com/repos/{auth_params[0]}/{repo_name}/community/profile'
    repo_stats = requests.get(url, auth=auth_params).json()
    return repo_stats
