from typing import Protocol, Sequence

from application.task.command import (
    CreateTaskCommand,
    DeleteTaskCommand,
    DeleteByCategoryTaskCommand,
    UpdateTaskCommand,
    SetStatusCompletedTaskCommand,
)
from application.task.query import (
    SearchTaskQuery,
    GetByCategoryTaskQuery,
    GetByIdTaskQuery,
)
from domain.task.entity import Task


class ITaskRepository(Protocol):
    def add(self, command: CreateTaskCommand) -> Task:
        pass

    def delete(self, command: DeleteTaskCommand) -> None:
        pass

    def delete_by_category(self, command: DeleteByCategoryTaskCommand):
        pass

    def search(self, query: SearchTaskQuery) -> Sequence[Task]:
        pass

    def update(self, query: UpdateTaskCommand) -> None:
        pass

    def all(self) -> Sequence[Task]:
        pass

    def get_by_id(self, query: GetByIdTaskQuery) -> Task:
        pass

    def get_by_category(self, query: GetByCategoryTaskQuery) -> Sequence[Task]:
        pass

    def set_status_completed(self, command: SetStatusCompletedTaskCommand) -> None:
        pass
