import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content_Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload_link(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {
            "path": file_path,
            "overwrite": "true"
        }
        response = requests.get(upload_url, params=params, headers=headers)
        return response.json()

    def upload(self, file_path: str, filename):
        response_dict = self.upload_link(file_path = file_path)
        pprint(response_dict)
        href = response_dict.get("href", "")
        pprint(href)
        data = open("test_file.txt", 'rb')
        response = requests.put(href, data)
        data.close()
        response.raise_for_status()
        print(response.status_code)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = "netology/test"
    filename = "test_file.txt"
    token = "AQAAAAAZJUXrAADLW-qtmvkOBUvjvOye265SgRU"
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, filename)