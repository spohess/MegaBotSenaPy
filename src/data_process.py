import pandas as pd


class DataProcess:
    model = None

    def __init__(self, model):
        self.model = model

    def execute(self):
        data = self.model.get_all()
        df = pd.DataFrame(data)
        self.model.close()
        df.rename(columns={0: 'concurso',
                           1: 'data_sorteio',
                           2: 'primeiro_numero',
                           3: 'segundo_numero',
                           4: 'terceiro_numero',
                           5: 'quarto_numero',
                           6: 'quinto_numero',
                           7: 'sexto_numero',
                           8: 'ganhadores_sena',
                           9: 'ganhadores_quina',
                           10: 'ganhadores_quadra'},
                  inplace=True)
        df.set_index('concurso', inplace=True)
