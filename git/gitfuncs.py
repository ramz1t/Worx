import requests
from urls import urls


def get_user(auth_params, username=''):
    if username == '':
        username = auth_params['username']
    user = requests.get(urls['user_url'].format(username), auth=tuple(auth_params.values())).json()
    print(user)
    return user


def get_user_repos(auth_params, users_name=None):
    if users_name is None:
        users_name = auth_params['username']
    repos = requests.get(urls['repos_url'].format(users_name), auth=tuple(auth_params.values())).json()
    return repos


def get_repo_issues(auth_params, repo_name, issue_id=''):
    if issue_id != '':
        issue_id = '/' + str(issue_id)
    issues = requests.get(
        urls['issues_url'].format(auth_params['username'], repo_name, issue_id),
        auth=tuple(auth_params.values())).json()
    return issues


def get_repo_branches(auth_params, repo_name, sha=''):
    if sha != '':
        sha = '/' + sha
    branches = requests.get(urls['branches_url'].format(auth_params['username'], repo_name, sha),
                            auth=tuple(auth_params.values())).json()
    return branches


def get_repo_commits(auth_params, repo_name, sha="", info=False):
    if sha != "":
        sha = "/" + str(sha)
    commits = requests.get(urls['commits_url'].format(auth_params['username'], repo_name, sha),
                           auth=tuple(auth_params.values())).json()
    if info:
        commitinfo = []
        for commit in commits:
            commitinfo.append(requests.get(commit['url'], auth=tuple(auth_params.values())).json())
        return commitinfo
    return commits


def get_repo_comment(auth_params, repo_name, number=''):
    if number != '':
        number = '/' + str(number)
    comments = requests.get(urls['comments_url'].format(auth_params['username'], repo_name, number),
                            auth=tuple(auth_params.values())).json()
    return comments


def get_repo_pulls(auth_params, repo_name, number=''):
    if number != '':
        number = '/' + str(number)
    pulls = requests.get(urls['pulls_url'].format(auth_params['username'], repo_name, number),
                         auth=tuple(auth_params.values())).json()
    return pulls


def get_repo_subs(auth_params, repo_name, users_name=None):
    if users_name is None:
        users_name = auth_params['username']
    subs = requests.get(urls['subscribers_url'].format(users_name, repo_name),
                        auth=tuple(auth_params.values())).json()
    return subs


def get_repo_contributors(auth_params, repo_name, users_name=None):
    if users_name is None:
        users_name = auth_params['username']
    contributors = requests.get(urls['contributors_url'].format(users_name, repo_name),
                                auth=tuple(auth_params.values())).json()
    return contributors


def get_repo_yearly_stats(auth_params, repo_name, users_name=None):
    if users_name is None:
        users_name = auth_params['username']
    yearly_stats = requests.get(urls['yearly_stats'].format(users_name, repo_name),
                                auth=tuple(auth_params.values())).json()
    return yearly_stats


def get_repo_contributors_stats(auth_params, repo_name, users_name=None):
    if users_name is None:
        users_name = auth_params['username']
    contributors_stats = requests.get(urls['contributors_stats'].format(users_name, repo_name),
                                      auth=tuple(auth_params.values())).json()
    return contributors_stats


def get_user_repo_weekly_stats(auth_params, repo_name, users_name=None):
    if users_name is None:
        users_name = auth_params['username']
    weekly_stats = requests.get(urls['weekly_stats'].format(users_name, repo_name),
                                auth=tuple(auth_params.values())).json()
    return weekly_stats


def get_user_repo_stats(auth_params, repo_name, users_name=None):
    if users_name is None:
        users_name = auth_params['username']
    repo_stats = requests.get(urls['repo_stats'].format(users_name, repo_name),
                              auth=tuple(auth_params.values())).json()
    return repo_stats
