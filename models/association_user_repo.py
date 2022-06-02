from sqlalchemy import Table, Column, ForeignKey
from data.data import Base


association_table = Table(
    "association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("repo_id", ForeignKey("repos.id")),
)
