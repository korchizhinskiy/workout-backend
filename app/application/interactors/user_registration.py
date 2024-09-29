from app.application.interfaces.repository.user import IUserRepository


class UserRegistrationInteractor:
    def __init__(self, repository: IUserRepository) -> None:
        self.repository = repository

    def execute(self) -> None:
        pass
