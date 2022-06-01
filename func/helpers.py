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
    pass


def get_least_produstive_day(data):
    pass


def get_lines_per_commit(data):
    pass


def get_added_lines(data):
    pass


def get_repo_users_count(data):
    return len(data)
