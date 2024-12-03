from datetime import datetime

from domain.task.value_object import CategoryEnum, PriorityEnum, StatusEnum
from settings.config import FORMAT_DATA


def get_category() -> CategoryEnum:
    print()
    print("Выберете категории: ")
    print("1. Работа.")
    print("2. Личное.")
    print("3. Обучение.")

    while True:
        category = input("Введите номер категории: ")
        match category:
            case "1":
                return CategoryEnum.WORK
            case "2":
                return CategoryEnum.PRIVATE
            case "3":
                return CategoryEnum.EDUCATION
            case _:
                print("Некорректный ввод, попробуйте снова. ")
                continue


def get_priority() -> PriorityEnum:
    print()
    print("Приоритет: ")
    print("1. Низкий.")
    print("2. Средний.")
    print("3. Высокий.")

    while True:
        priority = input("Укажите приоритет: ")
        match priority:

            case "1":
                return PriorityEnum.LOW
            case "2":
                return PriorityEnum.MEDIUM
            case "3":
                return PriorityEnum.HIGH
            case _:
                print("Некорректный ввод, попробуйте снова. ")
                continue


def get_deadline() -> str:
    while True:
        deadline = input("Срок выполнения задачи. (Пример - 2024-12-31): ")
        try:
            datetime.strptime(deadline, FORMAT_DATA).date()
            return deadline
        except ValueError:
            print("Некорректный ввод, попробуйте снова. ")


def get_status() -> StatusEnum:
    print()
    print("Статус: ")
    print("1. Выполнена.")
    print("2. Не выполнена.")
    while True:
        status = input("")
        match status:
            case "1":
                return StatusEnum.COMPLETED
            case "2":
                return StatusEnum.NOT_COMPLETED
            case _:
                print("Некорректный ввод, попробуйте снова. ")
