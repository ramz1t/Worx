from data.data import Sessions
from models.team import Team, ApiCreateTeam
from fastapi.responses import JSONResponse
from fastapi import status


def get_team_by_id(team_id: int) -> Team or None:
    with Sessions() as session:
        return session.query(Team).filter_by(id=team_id).first()


def get_team_by_name(team_name: str) -> Team or None:
    with Sessions() as session:
        return session.query(Team).filter_by(name=team_name).first()


def change_team_name(name: str, id: int) -> JSONResponse:
    with Sessions() as session:
        team = get_team_by_id(id)
        if team is None:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='no team with this id')
        team.name = name
        session.add(team)
        session.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content='name changed')


def change_team_url(url: str, id: int) -> JSONResponse:
    with Sessions() as session:
        team = get_team_by_id(id)
        if team is None:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='no team with this id')
        team.url = url
        session.add(team)
        session.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content='url changed')


def create_team(team: ApiCreateTeam):
    return Team(name=team.name, url=team.url)


def delete_team_by_id(team_id: int):
    with Sessions() as session:
        team = session.query(Team).filter_by(name=team_id).first()
        if team is None:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='no team with this id')
        session.delete(team)
        session.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content='team deleted')


def delete_team_by_name(team_name: int):
    with Sessions() as session:
        team = session.query(Team).filter_by(name=team_name).first()
        if team is None:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='no team with this name')
        session.delete(team)
        session.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content='team deleted')
