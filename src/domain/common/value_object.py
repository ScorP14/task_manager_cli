from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class IValueObject:
    value: Any

    def __post_init__(self):
        self.validator()

    def validator(self):
        return NotImplementedError()
