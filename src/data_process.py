import pandas as pd


class DataProcess:
    model = None

    def __init__(self, model):
        self.model = model

    def execute(self):
        data = self.model.get_all()
        df = pd.DataFrame(data)
        self.model.close()
        df.rename(columns={0: 'contest',
                           1: 'contest_date',
                           2: 'first_number',
                           3: 'second_number',
                           4: 'third_number',
                           5: 'fourth_number',
                           6: 'fifth_number',
                           7: 'sixth_number',
                           8: 'winners_sena',
                           9: 'winners_quina',
                           10: 'winners_quadra'},
                  inplace=True)
        df.set_index('contest', inplace=True)
