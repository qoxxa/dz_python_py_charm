from yougile_api import YouGileApi


api = YouGileApi('https://yougile.com')


# 1. Получить список проектов
def test_get_projects():
    projects_list = api.get_projects_list()

    # проверить, что список не пуст
    assert len(projects_list['content']) > 0


def test_all_projects():
    # получить список проектов
    project_list = api.get_projects_list()
    project = len(project_list['content'])

    # получить список вместе с удалёнными проектами
    filtered_list = api.get_projects_list(my_params={'includeDeleted': 'true'})
    full_project_list = len(filtered_list['content'])

    # проверить что список 1 > списка 2
    assert full_project_list > project


# 2. Создать проект
def test_create_project():
    # получить список компаний

    body = api.get_projects_list()
    len_before = len(body['content'])

    # создать компанию
    name = 'Новая компания'
    result = api.create_project(name)
    new_id = result['id']

    # получить кол-во компаний
    body = api.get_projects_list()
    len_after = len(body['content'])

    # проверить название проекта
    assert body['content'][-1]['title'] == name

    # проверить, что проект добавился
    assert len_after - len_before == 1

    # проверить, что id проекта верный
    assert body['content'][-1]['id'] == new_id


# 3. Получить по ID
def test_get_project_id():
    # создание компании
    name = 'Новая компания3'
    result = api.create_project(name)
    new_id = result['id']

    # обращаемся к проекту
    new_project = api.project_id(new_id)

    # проверить что, ID верный
    assert new_project["id"] == new_id

    # проверить, что название верное
    assert new_project["title"] == name


# 4. Изменить проект
def test_edit_project():
    # создать проект
    name = 'Проект, который должен быть удалён'
    result = api.create_project(name)
    new_id = result['id']

    # изменить название проекта
    new_name = 'Редактировано'
    edited = api.edit_project(new_id, new_name)

    # проверить что ID совпадает
    assert edited["id"] == new_id

    # обратиться к проекту
    edited_project = api.project_id(new_id)

    # проверить новое название проекта
    assert edited_project["title"] == new_name

    # удалить проект
    api.delete_project(new_id)

    # проверить, что id компании нет
    body = api.get_projects_list()
    assert body['content'][-1]['id'] != new_id
