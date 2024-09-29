from typing import Protocol


class IUserRepository(Protocol):
    def create(self) -> None:
        pass
