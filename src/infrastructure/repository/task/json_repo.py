import json
import os
from contextlib import contextmanager
from dataclasses import dataclass
from typing import Any, Sequence
from application.task.command import (
    CreateTaskCommand,
    DeleteTaskCommand,
    DeleteByCategoryTaskCommand,
    SetStatusCompletedTaskCommand,
    UpdateTaskCommand,
)
from application.task.error import NotFoundByIdError
from application.task.query import (
    GetByCategoryTaskQuery,
    SearchTaskQuery,
    GetByIdTaskQuery,
)
from domain.task.entity import Task, MapperTask
from infrastructure.repository.task.interface import ITaskRepository


@dataclass
class JsonDTO:
    metadata: dict[str, Any]
    data: dict[str, dict]

    def get_all(self) -> dict[str, dict]:
        return dict(metadata=self.metadata, data=self.data)


@dataclass
class TaskRepositoryJson:
    path_to_file: str

    def __post_init__(self) -> None:
        if not os.path.exists(self.path_to_file):
            result = JsonDTO(metadata=dict(autoincrement=0), data={})
            self._save_books(result)

    @contextmanager
    def connect(self, save: bool = False):
        database: JsonDTO = self._load_books()
        yield database
        if save:
            self._save_books(database)

    def _save_books(self, data: JsonDTO) -> None:
        with open(self.path_to_file, "w", encoding="utf-8") as file:
            json.dump(data.get_all(), file, ensure_ascii=False, indent=4)

    def _load_books(self) -> JsonDTO:
        with open(self.path_to_file, "r", encoding="utf-8") as file:
            result_data = json.load(file)
        return JsonDTO(metadata=result_data["metadata"], data=result_data["data"])

    def add(self, command: CreateTaskCommand) -> Task:
        with self.connect(save=True) as database:
            _id = database.metadata["autoincrement"]
            database.data[_id] = command.get_dict()
            database.metadata["autoincrement"] += 1

        task = MapperTask.from_dict_to_model({"id": _id} | command.get_dict())
        return task

    def delete(self, command: DeleteTaskCommand) -> None:
        with self.connect(save=True) as database:
            str_id = str(command.id)
            if str_id not in database.data:
                raise NotFoundByIdError(command.id)
            del database.data[str_id]

    def delete_by_category(self, command: DeleteByCategoryTaskCommand) -> None:
        with self.connect(save=True) as database:
            database.data = {
                key: value
                for key, value in database.data.items()
                if not value["category"] == command.category.value
            }

    def all(self) -> Sequence[Task]:
        with self.connect(save=False) as database:
            return [
                MapperTask.from_dict_to_model({"id": _id} | task)
                for _id, task in database.data.items()
            ]

    def get_by_id(self, query: GetByIdTaskQuery) -> Task:
        with self.connect(save=False) as database:
            try:
                task_data = database.data[str(query.id)]
                return MapperTask.from_dict_to_model({"id": query.id} | task_data)
            except KeyError:
                raise NotFoundByIdError(query.id)

    def get_by_category(self, query: GetByCategoryTaskQuery) -> Sequence[Task]:
        with self.connect(save=False) as database:
            return [
                MapperTask.from_dict_to_model({"id": _id} | task)
                for _id, task in database.data.items()
                if task["category"] == query.category.value
            ]

    def set_status_completed(self, command: SetStatusCompletedTaskCommand) -> None:
        with self.connect(save=True) as database:
            str_id = str(command.id)
            if str_id not in database.data:
                raise NotFoundByIdError(command.id)
            database.data[str_id]["status"] = command.status.value

    def search(self, query: SearchTaskQuery) -> Sequence[Task]:
        with self.connect(save=False) as database:
            result = []
            search_key = query.value.lower()
            for _id, task in database.data.items():
                if any(
                    search_key in str(task[field]).lower()
                    for field in [
                        "title",
                        "description",
                        "category",
                        "priority",
                        "status",
                    ]
                ):
                    result.append(MapperTask.from_dict_to_model({"id": _id} | task))
        return result

    def update(self, query: UpdateTaskCommand) -> None:
        with self.connect(save=True) as database:
            data = query.get_not_null_data()
            id_task = data.pop("id")
            database.data[str(id_task)].update(data)
