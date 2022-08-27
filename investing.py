
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import lxml
from category import Category
from newconnect import NewConnect
from infotable import Table
import json



class GetHtmlPage:
    def __init__(self):
        self.__options = None 
        self.__ua = UserAgent()
        self.__userAgent = None

    def __setpropertise(self):
        self.__options = webdriver.ChromeOptions()
        self.__userAgent = self.__ua.random
        print(self.__userAgent)
        self.__options.add_argument("window-size=1280,800")
        self.__options.add_argument('--headless')
        #self.__options.add_argument('--no-sandbox')
        self.__options.add_argument('--disable-dev-shm-usage')
        self.__options.add_argument('--disable-blink-features=AutomationControlled')
        self.__options.add_argument(f'user-agent={self.__userAgent}')

    def get_sourcepage(self,url):
        self.__setpropertise()
        CROMEPATH = 'selen\chromedriver.exe'
        driver = webdriver.Chrome(CROMEPATH,options=self.__options)
        driver.get(url)
        source_page = driver.page_source
        driver.quit()
        return source_page


class Main:

    def main():
        url = 'https://www.investing.com'
        category = Category()
        newconect = NewConnect()
        if category.get_check():
            data_json = category.get_category()
            for cat in data_json:
                print(cat)
            categorys = input('Enter Category: ')
            if categorys in data_json:
                for cat in data_json[categorys]:
                    print(cat)
                
                subcategories = input('Enter subcategory: ')
                if subcategories in data_json[categorys]:
                    urls = data_json[categorys][subcategories]
                    new_source = newconect.connect(urls)
                    if new_source:
                        body_table = Table(new_source)
                        body_table.info_tables()
                    else:
                        print('error')

        else:
            get_html = GetHtmlPage()
            source = get_html.get_sourcepage(url)
            data_json = category.get_category(source)
            for cat in data_json:
                print(cat)
            categorys = input('Enter Category: ')
            if categorys in data_json:
                for cat in data_json[categorys]:
                    print(cat)
                subcategories = input('Enter subcategory: ')
                if subcategories in data_json[categorys]:
                    urls = data_json[categorys][subcategories]
                    new_source = newconect.connect(urls)
                    body_table = Table(new_source)
                    body_table.info_tables()


if __name__ == '__main__':
    Main.main()
