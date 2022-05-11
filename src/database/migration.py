class Migrate:
    con = None

    def __init__(self, con):
        self.con = con

    def execute(self):
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE mega_sena (
            contest         INTEGER  NOT NULL CONSTRAINT mega_sena_pk PRIMARY KEY,
            contest_date    DATE NOT NULL,
            first_number    INTEGER  NOT NULL,
            second_number   INTEGER  NOT NULL,
            third_number    INTEGER  NOT NULL,
            fourth_number   INTEGER  NOT NULL,
            fifth_number    INTEGER  NOT NULL,
            sixth_number    INTEGER  NOT NULL,
            winners_sena    INTEGER DEFAULT 0 NOT NULL,
            winners_quina   INTEGER DEFAULT 0,
            winners_quadra  INTEGER DEFAULT 0 NOT NULL)''')
        self.con.close()
