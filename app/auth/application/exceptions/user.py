from app.auth.application.exceptions.base import ApplicationError


class UserNotFoundError(ApplicationError):
    message: str

    def __init__(self, *, username: str | None = None) -> None:
        if username:
            self.message = f"User with username {username!r} not found in system"
        else:
            self.message = "User not found in system"


class UserAlreadyRegisteredError(ApplicationError):
    message: str

    def __init__(self, *, username: str | None = None) -> None:
        if username:
            self.message = f"User with username {username!r} already registered."
        else:
            self.message = "User already registred in system"


class WrongPasswordError(ApplicationError):
    message = "Wrond password for this user"
