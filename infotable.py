import lxml
from bs4 import BeautifulSoup as bs

# Класс по парсингу таблиц из сайта

class Table:
    def __init__(self,source):
        self.soup = bs(source,'lxml')
        self.soup_body = None
        self.list_table = None
        self.inform = False
        self.not_table = None

#Проверка наличии таблицы

    def check_body_table(self):
        self.list_table = self.soup_body.find_all('tbody')
        self.not_table = self.soup_body.find('div',{'class':'fullHeaderTwoColumnPage--top'})
        if self.not_table:
            self.inform = True
        else:
            self.inform = False
            
        
# Поиск елементов в разных блоках

    def find_table(self):
        if self.soup.main:
            self.soup_body = self.soup.main
            self.check_body_table()
        elif self.soup.section:
            self.soup_body = self.soup.section
            self.check_body_table()
            
#Функция поиска если не таблица

    def find_not_table(self):
        list_title = self.soup_body.find('h1')
        information = self.soup_body.find('div',{'class':'fullHeaderTwoColumnPage--top'}).select_one('div.top.bold.inlineblock').select('span')
        print(list_title.text)
        print(information[0].text,information[1].text,information[2].text,information[3].text,information[4].text)
        print('+++++',self.inform)

#Вывод информации с сайта

    def output_info_table(self,list_title):
        if len(list_title) == len(self.list_table):
            for i in range(len(list_title)):
                title = list_title[i].text
                print(title)
                list_tag_td = self.list_table[i].find_all('td')
                all_text = "|".join([tag_td.text.strip() for tag_td in list_tag_td]).replace('|||','\n').replace('||','\n')
                print(all_text,'\n')

    def info_tables(self):
        self.find_table()
        if self.inform:
            self.find_not_table()
        else:
            if len(self.list_table)>1:
                list_title = self.soup_body.find_all('h2')
                self.output_info_table(list_title)
            elif len(self.list_table) == 1:
                list_title = self.soup_body.find_all('h1')
                self.output_info_table(list_title)



