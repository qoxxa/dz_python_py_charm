import requests


base_url = ('https://yougile.com')

auth = {
        'Authorization': '',
        'Content-Type': 'application/json'
}


# 1. Получить список проектов без токена
def test_auth():
    auth_headers = {
        'Authorization': '',
        'Content-Type': 'application/json'
    }

    resp = requests.get(base_url + '/api-v2/projects/', headers=auth_headers)
    assert resp.status_code == 400


# 2. Создать проект без обязательного поля 'Название'
def test_create_project():
    title = {
        "title": ""
    }
    resp = requests.post(base_url + '/api-v2/projects', headers=auth, json=title)
    assert resp.status_code == 400


# 3. Получить проект с несуществующим ID
def test_get_project_id():
    id = 'asdasd123123'
    resp = requests.get(base_url + '/api-v2/projects/' + str(id), headers=auth)
    assert resp.status_code == 404


# 4. Изменить название проекта на пустое
def test_edit_project():
    # создать проект
    title = {
        "title": "Компания для редактирования"
    }
    resp = requests.post(base_url + '/api-v2/projects', headers=auth, json=title)
    id = resp.json()['id']

    # изменить название на пустое
    new_title = {
        "title": ""
    }
    company = requests.post(base_url + '/api-v2/projects' + str(id), headers=auth, json=new_title)
    assert company.status_code == 404
