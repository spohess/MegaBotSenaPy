from src.database.database_manager import DatabaseManager


class MegaSenaModel(DatabaseManager):
    def insert(self, data):
        self.connect()
        cur = self.con.cursor()
        query = "INSERT INTO mega_sena VALUES ({0},'{1}',{2},{3},{4},{5},{6},{7},{8},{9},{10})".format(
            data['concurso'],
            data['data_sorteio'],
            data['primeiro_numero'],
            data['segundo_numero'],
            data['terceiro_numero'],
            data['quarto_numero'],
            data['quinto_numero'],
            data['sexto_numero'],
            data['ganhadores_sena'],
            data['ganhadores_quina'],
            data['ganhadores_quadra'],
        )

        cur.execute(query)
        self.con.commit()
        self.close()

    def get_all(self):
        self.connect()
        cur = self.con.cursor()
        query = 'SELECT * FROM mega_sena'
        result = cur.execute(query)

        return result
