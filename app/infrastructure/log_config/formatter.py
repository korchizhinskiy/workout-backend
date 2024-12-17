import http
import logging
import logging.config
import sys
from typing import Literal

COLORED_LEVELS = {
    logging.DEBUG: "\033[36mDEBUG\033[0m",
    logging.INFO: "\033[32mINFO\033[0m",
    logging.WARNING: "\033[33mWARNING\033[0m",
    logging.ERROR: "\033[31mERROR\033[0m",
    logging.CRITICAL: "\033[91mCRITICAL\033[0m",
}

class ColourizedFormatter(logging.Formatter):
    def __init__(
        self,
        fmt: str | None = None,
        datefmt: str | None = None,
        style: Literal["%", "{", "$"] = "%",
        use_colors: bool | None = None,  # noqa: FBT001
    ) -> None:
        if use_colors in {True, False}:
            self.use_colors = use_colors
        else:
            self.use_colors = sys.stdout.isatty()
        super().__init__(fmt=fmt, datefmt=datefmt, style=style)

    def formatMessage(self, record: logging.LogRecord) -> str:  # noqa: N802
        if self.use_colors:
            record.levelname = expand_log_field(
                field=COLORED_LEVELS.get(record.levelno, record.levelname),
                symbols=17,
            )
        return super().formatMessage(record)


class UvicornAccessColourizedFormatter(ColourizedFormatter):
    def __init__(
        self,
        fmt: str | None = None,
        datefmt: str | None = None,
        style: Literal["%", "{", "$"] = "%",
        use_colors: bool | None = None,  # noqa: FBT001
    ) -> None:
        if use_colors in {True, False}:
            self.use_colors = use_colors
        else:
            self.use_colors = sys.stdout.isatty()
        super().__init__(fmt=fmt, datefmt=datefmt, style=style)

    def formatMessage(self, record: logging.LogRecord) -> str:  # noqa: N802
        if self.use_colors:
            record.levelname = expand_log_field(
                field=COLORED_LEVELS.get(record.levelno, record.levelname),
                symbols=17,
            )
        return super().formatMessage(record)

    def get_status_code(self, status_code: int) -> str:
        try:
            status_phrase = http.HTTPStatus(status_code).phrase
        except ValueError:
            status_phrase = ""
        status_and_phrase = f"{status_code} {status_phrase}"
        # if self.use_colors:
        #     func = self.status_code_colours.get(status_code // 100, status_and_phrase)
        #     return func(status_and_phrase)
        return status_and_phrase


def expand_log_field(field: str, symbols: int) -> str:
    return field + (" " * (symbols - len(field)))
