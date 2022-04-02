from datetime import datetime


class ScrapeLine:
    line = None

    def __init__(self, line):
        self.line = line

    def execute(self):
        return self.__extract_data()

    def __extract_data(self):
        columns = self.line.findAll('td')

        try:
            data_sorteio = datetime.strptime(columns[1].get_text(), '%d/%m/%Y')

            return {
                'concurso': int(columns[0].get_text()),
                'data_sorteio': data_sorteio.strftime("%Y-%m-%d"),
                'primeiro_numero': int(columns[2].get_text()),
                'segundo_numero': int(columns[3].get_text()),
                'terceiro_numero': int(columns[4].get_text()),
                'quarto_numero': int(columns[5].get_text()),
                'quinto_numero': int(columns[6].get_text()),
                'sexto_numero': int(columns[7].get_text()),
                'ganhadores_sena': int(columns[8].get_text()),
                'ganhadores_quina': int(columns[9].get_text()),
                'ganhadores_quadra': int(columns[10].get_text()),
            }

        except IndexError:
            print(columns)
