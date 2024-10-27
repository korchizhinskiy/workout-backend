class InvalidAuthenticationTokenError(Exception):
    message = "Using invalidate token"


class SessionIsExpiredError(Exception):
    message = "User session is expired"
