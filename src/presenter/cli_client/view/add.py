from application.task.service import ServiceTask
from presenter.cli_client.view.common import get_category, get_deadline, get_priority


def add_view(task_service: ServiceTask):
    print("Для добавление задачи введите. ")
    title = input("Название: ")
    description = input("Описание: ")
    category = get_category()
    deadline = get_deadline()
    priority = get_priority()
    task = task_service.add_task(title, description, category.value, deadline, priority.value)
    return task
