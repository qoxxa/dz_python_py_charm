import requests


auth_headers = {
            'Authorization': '',
            'Content-Type': 'application/json'
        }


class YouGileApi:

    def __init__(self, url):
        self.url = url

    def get_projects_list(self, my_params=None):
        resp = requests.get(self.url + '/api-v2/projects/', headers=auth_headers, params=my_params)
        return resp.json()

    def get_token(self, user='***', password='***', company_id='f203355c-206d-4565-a62e-0a2b1f6a2db0'):

        creds = {
            'login': user,
            'password': password,
            'companyId': company_id
        }
        resp = requests.post(self.url + '/api-v2/auth/keys/', json=creds)
        return resp.json()['key']

    def create_project(self, name):

        title = {
            "title": name
        }
        resp = requests.post(self.url + '/api-v2/projects', headers=auth_headers, json=title)
        return resp.json()

    def project_id(self, id):

        resp = requests.get(self.url + '/api-v2/projects/' + str(id), headers=auth_headers)
        return resp.json()

    def edit_project(self, new_id, new_name):
        project = {
            "title": new_name
        }

        resp = requests.put(self.url + '/api-v2/projects/' + str(new_id), headers=auth_headers, json=project)
        return resp.json()

    def delete_project(self, new_id):
        project = {
            "deleted": True
        }

        resp = requests.put(self.url + '/api-v2/projects/' + str(new_id), headers=auth_headers, json=project)
        return resp.json()
