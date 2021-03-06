from data.data import Sessions
from models.repo import Repo, ApiCreateRepo
from fastapi.responses import JSONResponse
from fastapi import status


def create_new_repo(ApiRepo) -> JSONResponse:
    with Sessions() as session:
        if not session.query(Repo).filter_by(name=ApiRepo.name).first() is None:
            return JSONResponse(status_code=status.HTTP_409_CONFLICT, content='repo already in use')
        repo = Repo(name=ApiRepo.name, owner_username=ApiRepo.owner_username)
        session.add(repo)
        session.commit()
    return JSONResponse(status_code=status.HTTP_201_CREATED, content='Successfully')


def get_repo_by_id(repo_id: int) -> Repo or None:
    with Sessions() as session:
        return session.query(Repo).filter_by(id=repo_id).first()


def get_repo_by_name(repo_name: str) -> Repo or None:
    with Sessions() as session:
        return session.query(Repo).filter_by(name=repo_name).first()


def change_repo_name(name: str, id: int) -> JSONResponse:
    with Sessions() as session:
        repo = get_repo_by_id(id)
        if repo is None:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='no repo with this id')
        repo.name = name
        session.add(repo)
        session.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content='name changed')


def change_repo_ownerusername(owner_username: str, id: int) -> JSONResponse:
    with Sessions() as session:
        repo = get_repo_by_id(id)
        if repo is None:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='no repo with this id')
        repo.owner_username = owner_username
        session.add(repo)
        session.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content='url changed')


def create_repo(repo: ApiCreateRepo):
    return Repo(name=repo.name, owner_username=repo.owner_username)


def delete_repo_by_id(repo_id: int):
    with Sessions() as session:
        repo = session.query(Repo).filter_by(name=repo_id).first()
        if repo is None:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='no repo with this id')
        session.delete(repo)
        session.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content='repo deleted')


def delete_repo_by_name(repo_name: str):
    with Sessions() as session:
        repo = session.query(Repo).filter_by(name=repo_name).first()
        if repo is None:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content='no repo with this name')
        session.delete(repo)
        session.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content='repo deleted')
