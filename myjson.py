

class MyJson:

    def __init__(self,title,list_info):
        self.__title = title
        self.__list_information = list_info


    def generate_json(self):
        text_info = [ [td.text for td in tag_td.find_all('td')] for tag_td in self.__list_information]
        my_dict = {self.__title:text_info}
        return my_dict