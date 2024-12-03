def banner() -> None:
    print("==========================")
    print("     Менеджер задач")
    print("==========================")


def get_command_for_menu() -> int | None:
    print()
    banner()
    print("Выберите действие: ")
    print("1. Просмотр всех текущих задач")
    print("2. Просмотр задач по категориям")
    print("3. Добавление новой задачи")
    print("4. Изменение существующей задачи")
    print("5. Отметка задачи как выполненной")
    print("6. Удаление задачи")
    print("7. Поиск задач")
    print()
    print("8. Выход")
    print()
    choice = input("Введите номер действия: ")
    if choice.isdigit():
        return int(choice)
