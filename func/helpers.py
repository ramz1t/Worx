import hashlib
import secrets
from data.data import Sessions
from models.user import User

auth_token_len = 20


def hashing_password(password) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def generate_token() -> str:
    return secrets.token_hex(auth_token_len)


def get_user_by_email(email: str):
    with Sessions() as session:
        return session.query(User).filter_by(email=email).first()


def get_most_productive_day(data):
    pass


def get_most_effective_user(data):
    users = {}
    for commit in data:
        name = commit['commit']['author']['name']
        if name not in users:
            users[name] = 1
        else:
            users[name] += 1
    most_effective_user = max(users)
    return most_effective_user


def get_least_effective_user(data):
    users = {}
    for commit in data:
        name = commit['commit']['author']['name']
        if name not in users:
            users[name] = 1
        else:
            users[name] += 1
    least_effective_user = min(users)
    return least_effective_user


def get_least_productive_day(data):
    pass


def get_lines_per_commit(data):
    pass


def get_added_lines(data):
    pass


def get_repo_commits_count(data):
    return len(data)


def get_repo_users_count(data):
    return len(data)


def get_user_repo_commits(data, username):
    k = 0
    for commit in data:
        if commit['commit']['author']['name'] == username:
            k += 1
    return k


def get_repo_issues_count(data):
    return len(data)


def get_repo_branches_count(data):
    return len(data)


def get_commits_leaderboard(data):
    result = []
    users = {}
    for commit in data:
        name = commit['commit']['author']['name']
        if name not in users:
            users[name] = 0
        users[name] += 1
    k = 1
    users = dict(sorted(users.items(), key=lambda item: item[1], reverse=True))
    for user in users:
        result.append(dict({'id': k, 'name': user, 'count': users.get(user)}))
        k += 1
    print(result)
    return result


def repo_users(data):
    users = set()
    for user in data:
        name = user['login']
        users.add(name)
    return users
