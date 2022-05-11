import json
from datetime import datetime
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

from bs4 import BeautifulSoup


class Scraping:
    modality = None
    soup = None
    model = None

    def __init__(self, modality, model):
        self.modality = modality
        self.model = model

    def execute(self):
        self.__create_file()
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
            row_data = self.__extract_data(line=line)
            self.model.insert(data=row_data)

            table.find('tr').extract()
            line = table.find('tr')

    def __extract_data(self, line):
        columns = line.findAll('td')

        try:
            contest_date = datetime.strptime(columns[1].get_text(), '%d/%m/%Y')
            return {
                'contest': int(columns[0].get_text()),
                'contest_date': contest_date.strftime('%Y-%m-%d'),
                'first_number': int(columns[2].get_text()),
                'second_number': int(columns[3].get_text()),
                'third_number': int(columns[4].get_text()),
                'fourth_number': int(columns[5].get_text()),
                'fifth_number': int(columns[6].get_text()),
                'sixth_number': int(columns[7].get_text()),
                'winners_sena': int(columns[8].get_text()),
                'winners_quina': int(columns[9].get_text()),
                'winners_quadra': int(columns[10].get_text()),
            }

        except IndexError:
            print(columns)
