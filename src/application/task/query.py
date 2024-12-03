from dataclasses import dataclass

from domain.task.value_object import Category


@dataclass(frozen=True)
class SearchTaskQuery:
    value: str


@dataclass(frozen=True)
class GetByCategoryTaskQuery:
    category: Category


@dataclass(frozen=True)
class GetByIdTaskQuery:
    id: int
