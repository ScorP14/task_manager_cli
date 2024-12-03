from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ApplicationError(Exception):
    value: Any = None

    def message(self):
        return NotImplementedError()


class ValueObjectError(ApplicationError): ...
