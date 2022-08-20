import lxml
from bs4 import BeautifulSoup as bs

class Table:
    def __init__(self,source):
        self.table = False
        self.source = source
        self.soup = None
        self.body = None
        self.inform = False
        self.not_table = None

    def find_table(self):
        self.soup = bs(self.source,'lxml')
       
        if self.soup.main:
            self.soup_body = self.soup.main
            self.list_table = self.soup_body.find_all('tbody')
            self.not_table = self.soup_body.find('div',{'data-test':'instrument-header-details'})
            if self.not_table:
                self.inform = True
            else:
                self.inform = False
        elif self.soup.section:
            self.soup_body = self.soup.section
            self.list_table = self.soup_body.find_all('tbody')
            self.not_table = self.soup_body.find('div',{'data-test':'instrument-header-details'})
            if self.not_table:
                self.inform = True
            else:
                self.inform = False
            


    def find_not_table(self):
        self.find_table()
        list_title = self.soup_body.find('h1')
        information = self.soup_body.find('div',{'data-test':'instrument-header-details'})
        if information:
            print(list_title.text)
            print(information.text)
            self.inform = True
        else:
            self.inform = False

        print('+++++',self.inform)


    def info_tables(self):
        self.find_table()
        if self.inform:
            list_title = self.soup_body.find('h1')
            print(list_title.text)
            print(self.not_table.text)
        else:
            if len(self.list_table)>1:
                list_title = self.soup_body.find_all('h2')
                if len(list_title) == len(self.list_table):
                    for i in range(len(list_title)):
                        title = list_title[i].text
                        print(title)
                        list_tag_td = self.list_table[i].find_all('td')
                        all_text = "|".join([tag_td.text.strip() for tag_td in list_tag_td]).replace('|||','\n')
                        print(all_text,'\n')
            elif len(self.list_table) == 1:
                list_title = self.soup_body.find_all('h1')
                if len(list_title) == len(self.list_table):
                    for i in range(len(list_title)):
                        title = list_title[i].text
                        print(title)
                        list_tag_td = self.list_table[i].find_all('td')
                        all_text = "|".join([tag_td.text.strip() for tag_td in list_tag_td]).replace('|||','\n')
                        print(all_text,'\n')




