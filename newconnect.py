import requests
from fake_useragent import UserAgent


class NewConnect:
    def __init__ (self):
        self.ua = UserAgent()
        self.session = requests.Session()

    def connect(self,url):
        headers = {'user-agent':self.ua.random}
        response = self.session.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
