from dataclasses import dataclass, asdict
from datetime import date

from domain.task.value_object import Category, Priority, Status, StatusEnum


@dataclass(frozen=True)
class CreateTaskCommand:
    title: str
    description: str
    category: Category
    deadline: date
    priority: Priority
    status: Status = StatusEnum.NOT_COMPLETED

    def get_dict(self):
        return dict(
            title=self.title,
            description=self.description,
            category=self.category.value,
            deadline=str(self.deadline),
            priority=self.priority.value,
            status=self.status.value,
        )


@dataclass(frozen=True)
class DeleteTaskCommand:
    id: int


@dataclass(frozen=True)
class DeleteByCategoryTaskCommand:
    category: Category


@dataclass(frozen=True)
class SetStatusCompletedTaskCommand:
    id: int
    status: Status = StatusEnum.COMPLETED


@dataclass
class UpdateTaskCommand:
    id: int
    title: str = None
    description: str = None
    category: Category = None
    deadline: date = None
    priority: Priority = None
    status: Status = None

    def get_not_null_data(self):
        return {key: value for key, value in asdict(self).items() if value is not None}
