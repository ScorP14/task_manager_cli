from domain.common.error import ValueObjectError
from dataclasses import dataclass


@dataclass(frozen=True)
class PriorityValueObjectError(ValueObjectError):
    value: str

    def message(self):
        return f'Некорректное значение для поля "Приоритет" - {self.value}'


@dataclass(frozen=True)
class StatusValueObjectError(ValueObjectError):
    value: str

    def message(self):
        return f'Некорректное значение для поля "Статус" - {self.value}'


@dataclass(frozen=True)
class CategoryValueObjectError(ValueObjectError):
    value: str

    def message(self):
        return f'Некорректное значение для поля "Категории" - {self.value}'
