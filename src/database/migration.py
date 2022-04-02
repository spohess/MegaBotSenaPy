class Migrate:
    con = None

    def __init__(self, con):
        self.con = con

    def execute(self):
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE mega_sena (
            concurso          integer  NOT NULL CONSTRAINT table_name_pk PRIMARY KEY,
            data_sorteio      date NOT NULL,
            primeiro_numero   integer  NOT NULL,
            segundo_numero    integer  NOT NULL,
            terceiro_numero   integer  NOT NULL,
            quarto_numero     integer  NOT NULL,
            quinto_numero     integer  NOT NULL,
            sexto_numero      integer  NOT NULL,
            ganhadores_sena   integer DEFAULT 0 NOT NULL,
            ganhadores_quina  integer DEFAULT 0,
            ganhadores_quadra integer DEFAULT 0 NOT NULL)''')
        self.con.close()
