from models.user import User
from fastapi import Request
from func.helpers import get_repo_users_count, get_most_effective_user, get_least_effective_user, \
    get_repo_commits_count, get_user_repo_commits, get_repo_branches_count, get_commits_leaderboard, \
    repo_users
from logic.repo import get_repo_by_name
from git.gitfuncs import get_repo_commits, get_repo_contributors, get_user_repo_stats, get_repo_branches
from logic.user import get_user_added_repos

class StatsPage:

    def __init__(self, Auth_params, username: str, reponame: str, current_user: User, request: Request) -> None:
        self.username = username
        self.reponame = reponame
        self.current_user = current_user
        self.request = request
        self.gender = current_user.gender
        self.repo_contributors_count = ''
        self.most_effective_user = ''
        self.least_effective_user = ''
        self.commits_count = ''
        self.user_repo_commits = ''
        self.repo_branches = ''
        self.commit_leaderboard = []
        self.Auth_params = Auth_params

    def make(self):
        db_repo = get_repo_by_name(repo_name=self.reponame)
        contributors_list = get_repo_contributors(auth_params=self.Auth_params, repo_name=self.reponame,
                                                  users_name=db_repo.owner_username)
        commits = get_repo_commits(auth_params=self.Auth_params, repo_name=self.reponame, username=db_repo.owner_username)
        self.repo_contributors_count = get_repo_users_count(contributors_list)
        self.most_effective_user = get_most_effective_user(commits)
        self.least_effective_user = get_least_effective_user(commits)
        self.commits_count = get_repo_commits_count(commits)
        self.user_repo_commits = get_user_repo_commits(commits, self.username)
        branches = get_repo_branches(auth_params=self.Auth_params, repo_name=self.reponame, username=db_repo.owner_username)
        self.repo_branches = get_repo_branches_count(branches)
        self.commit_leaderboard = get_commits_leaderboard(commits)

    def export(self):
        self.make()
        return {"request": self.request,
                "reponame": self.reponame,
                "username": self.username,
                "gender": self.current_user.gender,
                "repo_contributors_count": self.repo_contributors_count,
                "most_effective_user": self.most_effective_user,
                "least_effective_user": self.least_effective_user,
                "repo_commits_count": self.commits_count,
                "user_repo_commits": self.user_repo_commits,
                "repo_branches": self.repo_branches,
                "commit_leaderboard": self.commit_leaderboard}


class NavbarData:

    def __init__(self, current_user: User, Auth_params, reponame: str) -> None:
        self.reponame = reponame
        self.current_user = current_user
        self.Auth_params = Auth_params
        self.repos = []
        self.users = []

    def make(self):
        self.repos = get_user_added_repos(user_id=self.current_user.id)
        db_repo = get_repo_by_name(self.reponame)
        contributors_list = get_repo_contributors(auth_params=self.Auth_params, repo_name=self.reponame,
                                                  users_name=db_repo.owner_username)
        self.users = repo_users(contributors_list)

    def export(self):
        self.make()
        return {"repos": self.repos, "users": self.users}
