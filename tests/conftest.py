from datetime import datetime

import pytest

list_data_task = [
    dict(
        id=1,
        title="Изучить основы FastApi",
        description="Пройти документацию по FastApi и создать простой проект",
        category="обучение",
        deadline=datetime.now().date(),
        priority="низкий",
        status=False,
    ),
    dict(
        id=2,
        title="Повторить основы FastApi",
        description="Повторить документацию по FastApi и создать простой проект",
        category="личное",
        deadline=datetime.now().date(),
        priority="высокий",
        status="выполнена",
    ),
    dict(
        id=3,
        title='Изучить "фишки" FastApi',
        description="Пройти документацию по FastApi и создать сложный проект",
        category="обучение",
        deadline=datetime.now().date(),
        priority="средний",
        status="выполнена",
    ),
    dict(
        id=4,
        title='Повторить "фишки" FastApi',
        description="Повторить документацию по FastApi и создать простой проект",
        category="работа",
        deadline=datetime.now().date(),
        priority="средний",
        status="не выполнена",
    ),
]


@pytest.fixture(params=list_data_task)
def data_task(request):
    return request.param
