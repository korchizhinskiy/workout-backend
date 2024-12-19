class InfrastructureError(Exception):
    message = "Unknown error occurred"


class ResourseNotFoundError(InfrastructureError):
    message: str

    def __init__(self, *, resourse_identity: str | None = None) -> None:
        if resourse_identity:
            self.message = f"Resourse with identity {resourse_identity!r} not found."
        else:
            self.message = "Resourse not found."
