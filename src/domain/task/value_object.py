from enum import Enum
from dataclasses import dataclass

from domain.common.value_object import IValueObject

from domain.task.error import PriorityValueObjectError, StatusValueObjectError


class CategoryEnum(str, Enum):
    WORK: str = "работа"
    PRIVATE: str = "личное"
    EDUCATION: str = "обучение"


@dataclass(frozen=True)
class Category(IValueObject):
    value: str

    @staticmethod
    def choices():
        return [i.value for i in CategoryEnum]

    @staticmethod
    def is_check_validation(text: str) -> bool:
        if text.lower() in CategoryEnum:
            return True
        return False

    def validator(self):
        if not self.is_check_validation(self.value):
            raise StatusValueObjectError(self.value)


class StatusEnum(str, Enum):
    COMPLETED: str = "выполнена"
    NOT_COMPLETED: str = "не выполнена"


@dataclass(frozen=True)
class Status(IValueObject):
    value: str

    @staticmethod
    def choices():
        return [i.value for i in StatusEnum]

    @staticmethod
    def is_check_validation(text: str) -> bool:
        if text.lower() in StatusEnum:
            return True
        return False

    def validator(self):
        if not self.is_check_validation(self.value):
            raise StatusValueObjectError(self.value)


class PriorityEnum(str, Enum):
    LOW: str = "низкий"
    MEDIUM: str = "средний"
    HIGH: str = "высокий"


@dataclass(frozen=True)
class Priority(IValueObject):
    value: str

    @staticmethod
    def choices():
        return [i.value for i in PriorityEnum]

    @staticmethod
    def is_check_validation(text: str) -> bool:
        if text.lower() in PriorityEnum:
            return True
        return False

    def validator(self):
        if not self.is_check_validation(self.value):
            raise PriorityValueObjectError(self.value)
