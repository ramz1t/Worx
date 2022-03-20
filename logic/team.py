from data.data import Sessions
from models.team import Team, ApiCreateTeam


def get_team_by_id(team_id: int) -> Team or None:
    with Sessions() as session:
        return session.query(Team).filter_by(id=team_id).first()


def get_team_by_name(team_name: str) -> Team or None:
    with Sessions() as session:
        return session.query(Team).filter_by(name=team_name)

def change_team_name(name: str, id: int) -> bool:
    with Sessions() as session:
        team = get_team_by_id(id)
        if team is None:
            return False
        team.name = name
        session.add(team)
        session.commit()
    return True


def change_team_url(url: str, id: int) -> bool:
    with Sessions() as session:
        team = get_team_by_id(id)
        if team is None:
            return False
        team.url = url
        session.add(team)
        session.commit()


def create_team(team: ApiCreateTeam):
    return Team(name=team.name, url=team.url)


def delete_team_by_id(team_id: int):
    with Sessions() as session:
        session.query(Team).filter_by(id=team_id).delete()
        session.commit()


def delete_team_by_name(team_name: int):
    with Sessions() as session:
        session.query(Team).filter_by(id=team_name).delete()
        session.commit()
