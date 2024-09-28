from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class User:
    first_name: str
    last_name: str
    last_name: str
