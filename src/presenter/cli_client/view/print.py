from typing import Sequence

from tabulate import tabulate

from domain.task.entity import Task

COLUMN = ["id", "Название", "Описание", "Категория", "Сроки", "Приоритет", "Статус "]


def print_task(task: Task):
    print_data = (
        [
            task.id,
            task.title,
            task.description,
            task.category.value,
            task.deadline,
            task.priority.value,
            task.status.value,
        ],
    )
    print(tabulate(print_data, headers=COLUMN, tablefmt="grid", stralign="center"))


def print_tasks(tasks: Sequence[Task]):
    print_data = (
        [
            task.id,
            task.title,
            task.description,
            task.category.value,
            task.deadline,
            task.priority.value,
            task.status.value,
        ]
        for task in tasks
    )
    print(tabulate(print_data, headers=COLUMN, tablefmt="grid", stralign="center"))
