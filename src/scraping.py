import json
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup

from src.scrape_line import ScrapeLine


class Scraping:
    modality = None
    soup = None
    model = None

    def __init__(self, modality, model):
        self.modality = modality
        self.model = model

    def execute(self):
        # self.__create_file()
        self.__set_soup()
        self.__read_html()

    def __create_file(self):
        url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade={0}'.format(self.modality)
        file = 'htmlfiles/{0}.html'.format(self.modality)

        try:
            response = urlopen(url)
            payload = json.load(response)
            soup = BeautifulSoup(payload['html'], 'html.parser')

            debug_file = open(file, 'w')
            print(soup.prettify(), file=debug_file)
            debug_file.close()
        except HTTPError as e:
            print(e.status, e.reason)

        except URLError as e:
            print(e.reason)

    def __set_soup(self):
        path_file = 'htmlfiles/{0}.html'.format(self.modality)
        file = open(path_file, 'r')
        html = ' '.join(file.read().split()).replace('> <', '><').replace('> ', '>').replace(' <', '<')
        self.soup = BeautifulSoup(html, 'html.parser')

    def __read_html(self):
        table = self.soup.find('table')
        table.find('thead').extract()
        line = table.find('tr')

        while line is not None:
            sl = ScrapeLine(line=line)

            row_data = sl.execute()
            self.model.insert(data=row_data)

            table.find('tr').extract()
            line = table.find('tr')
