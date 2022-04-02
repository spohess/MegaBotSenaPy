from types import NoneType
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import json


class Scraping:
    modality = None
    soup = None

    def __init__(self, modality):
        self.modality = modality

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
        self.soup = BeautifulSoup(file.read(), 'html.parser')

    def __read_html(self):
        tbodys = self.soup.findAll('tbody')
        print(tbodys)
