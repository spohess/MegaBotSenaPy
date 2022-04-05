class Migrate:
    con = None

    def __init__(self, con):
        self.con = con

    def execute(self):
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE mega_sena (
            concurso          INTEGER  NOT NULL CONSTRAINT table_name_pk PRIMARY KEY,
            data_sorteio      DATE NOT NULL,
            primeiro_numero   INTEGER  NOT NULL,
            segundo_numero    INTEGER  NOT NULL,
            terceiro_numero   INTEGER  NOT NULL,
            quarto_numero     INTEGER  NOT NULL,
            quinto_numero     INTEGER  NOT NULL,
            sexto_numero      INTEGER  NOT NULL,
            ganhadores_sena   INTEGER DEFAULT 0 NOT NULL,
            ganhadores_quina  INTEGER DEFAULT 0,
            ganhadores_quadra INTEGER DEFAULT 0 NOT NULL)''')
        self.con.close()
