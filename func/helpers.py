import hashlib
import secrets
from data.data import Sessions
from models.user import User

auth_token_len = 20


def hashing_password(password) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def generate_token() -> str:
    return secrets.token_hex(auth_token_len)


def get_user_by_username(username: str) -> User or None:
    with Sessions() as session:
        return session.query(User).filter_by(username=username).first()
