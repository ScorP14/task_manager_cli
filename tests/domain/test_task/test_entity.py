from domain.task.entity import Task
from domain.task.value_object import Category, Priority


def test_task_creation_instance(data_task: dict):
    task_instance = Task(
        id=data_task["id"],
        title=data_task["title"],
        description=data_task["description"],
        category=Category(data_task["category"]),
        deadline=data_task["deadline"],
        priority=Priority(data_task["priority"]),
        status=data_task["status"],
    )
    assert task_instance.id == data_task["id"]
    assert task_instance.title == data_task["title"]
    assert task_instance.description == data_task["description"]
    assert task_instance.category == Category(data_task["category"])
    assert task_instance.deadline == data_task["deadline"]
    assert task_instance.priority == Priority(data_task["priority"])
    assert task_instance.status == data_task["status"]
