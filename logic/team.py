from data.data import Sessions
from models.team import Team


def get_team_by_id(team_id: int) -> Team or None:
    with Sessions() as session:
        return session.query(Team).filter_by(id=team_id).first()


def change_team_name(name: str, id: int) -> bool:
    with Sessions() as session:
        team = get_team_by_id()
        if team is None:
            return False
        team.name = name
        session.add(team)
        session.commit()
    return True
