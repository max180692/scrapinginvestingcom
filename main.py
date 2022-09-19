from re import U
from category import Category
from connectrequests import NewConnect
from  connectselen import GetHtmlPage
from investing import Investing
from settingsparser import URL


def main():
    url = URL
    category = Category()
    newconect = NewConnect()
    invest = Investing()
    while True:
        if category.get_check():
            invest.set_html_page()
            invest.get_info()
        else:
            html_page = newconect.connect(url)
            if html_page:
                invest.set_html_page(html_page=html_page)
                invest.get_info()
            else:
                ghp = GetHtmlPage()
                html_page = ghp.get_sourcepage(url)
                invest.set_html_page(html_page=html_page)
                invest.get_info()
                
            


if __name__ == '__main__':
    main()