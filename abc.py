from models.repo import ApiCreateRepo

repo = ApiCreateRepo(name='NaviApp', id=2, owner_username='ramz1t')

from logic.repo import create_new_repo, delete_repo_by_name


create_new_repo(repo)
