from git.classes import JsonOutput, UserStats, generate_year_dict, User
from git.gitfuncs import get_user, get_user_repos, get_user_repo_stats, get_repo_contributors, get_repo_subs, \
    get_repo_pulls, get_repo_comment, get_repo_branches, get_repo_commits, get_repo_yearly_stats, \
    get_repo_contributors_stats, get_repo_issues, get_user_repo_weekly_stats
from git.urls import urls

GITHUB_TOKEN = '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'
username = 'githubgithabovich'

Auth_params = {
    'username': username,
    'GITHUB_TOKEN': GITHUB_TOKEN
}
