from dataclasses import dataclass
from datetime import datetime
from typing import Sequence

from application.task.command import (
    CreateTaskCommand,
    DeleteTaskCommand,
    DeleteByCategoryTaskCommand,
    UpdateTaskCommand,
    SetStatusCompletedTaskCommand,
)
from application.task.query import (
    GetByCategoryTaskQuery,
    SearchTaskQuery,
    GetByIdTaskQuery,
)
from domain.task.entity import Task
from domain.task.value_object import CategoryEnum, Category, Priority, Status
from infrastructure.repository.task.interface import ITaskRepository
from settings.config import FORMAT_DATA


@dataclass(frozen=True)
class ServiceTask:
    repository: ITaskRepository

    def add_task(
        self, title: str, description: str, category: str, deadline: str, priority: str
    ) -> Task:
        category = Category(category)
        priority = Priority(priority)
        deadline = datetime.strptime(deadline, FORMAT_DATA).date()
        command = CreateTaskCommand(
            title=title,
            description=description,
            category=category,
            deadline=deadline,
            priority=priority,
        )
        return self.repository.add(command)

    def delete_task_by_id(self, id: int) -> None:
        command = DeleteTaskCommand(id=id)
        self.repository.delete(command)

    def delete_task_by_category(self, category: str) -> None:
        category = Category(category)
        command = DeleteByCategoryTaskCommand(category=category)
        self.repository.delete_by_category(command)

    def get_task_by_id(self, id: int) -> Task:
        query = GetByIdTaskQuery(id=id)
        return self.repository.get_by_id(query)

    def get_all_task(self) -> Sequence[Task]:
        return self.repository.all()

    def get_task_by_category(self, category: str) -> Sequence[Task]:
        category = Category(CategoryEnum(category))
        query = GetByCategoryTaskQuery(category=category)
        return self.repository.get_by_category(query)

    def update_task(self, id: int, field: str, value: str) -> None:
        mapper = {
            "title": str,
            "description": str,
            "category": lambda v: Category(v).value,
            "deadline": lambda v: str(datetime.strptime(v, FORMAT_DATA).date()),
            "priority": lambda v: Priority(v).value,
            "status": lambda v: Status(v).value,
        }

        command = UpdateTaskCommand(id, **{field: mapper[field](value)})
        self.repository.update(command)

    def set_completed_task(self, id: int) -> None:
        command = SetStatusCompletedTaskCommand(id)
        self.repository.set_status_completed(command)

    def search_task(self, query: str) -> Sequence[Task]:
        query = SearchTaskQuery(query)
        return self.repository.search(query)
