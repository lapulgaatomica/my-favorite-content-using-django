import requests
from bs4 import BeautifulSoup
from django.db import IntegrityError, transaction

def get_columns():
    titles = []
    columnists = []
    links = []

    columns = requests.get('https://www.dailymail.co.uk/columnists/index.html')
    parsed_page = BeautifulSoup(columns.text, 'lxml')
    most_recent = parsed_page.find("div", {"class":"js-headers"}).find_all("div", {"class":"columnist-archive-content cleared link-ccox"})

    for column in most_recent:
        link_and_title = column.find('h2', {'class':'linkro-ccox'})
        columnists.append(column.find('a', {"class":"author"}).text)
        titles.append(link_and_title.text)
        links.append('https://www.dailymail.co.uk' + link_and_title.find('a')['href'])

    from .models import DailyMailColumn#i tried to import it at the beginning of the file but kept getting an error
    for new_link, title, columnist in zip(links, titles, columnists):
        print(title)
        column = DailyMailColumn(link=new_link, title=title, columnist=columnist)
        try:
            column.save()
            # send email
        except IntegrityError:
            transaction.rollback()
