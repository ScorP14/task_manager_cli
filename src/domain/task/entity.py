from datetime import datetime
from dataclasses import dataclass
from typing import Any
from datetime import date

from domain.common.entity import IEntity
from domain.task.value_object import (
    Category,
    Priority,
    Status,
    StatusEnum,
)
from settings.config import FORMAT_DATA


@dataclass(frozen=True)
class Task(IEntity):
    title: str
    description: str
    category: Category
    deadline: date
    priority: Priority
    status: Status = StatusEnum.NOT_COMPLETED.value


class MapperTask:
    @staticmethod
    def from_dict_to_model(data: dict[str, Any]) -> Task:
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            category=Category(data["category"]),
            deadline=datetime.strptime(data["deadline"], FORMAT_DATA).date(),
            priority=Priority(data["priority"]),
            status=Status(
                data.get("status", StatusEnum.NOT_COMPLETED),
            ),
        )

    @staticmethod
    def from_model_to_dict(task: Task) -> dict[str, Any]:
        return dict(
            id=task.id,
            title=task.title,
            description=task.description,
            category=task.category.value.lower(),
            deadline=str(task.deadline),
            priority=task.priority.value.lower(),
            status=task.status.value.lower(),
        )
