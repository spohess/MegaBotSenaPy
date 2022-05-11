from src.database.database_manager import DatabaseManager


class MegaSenaModel(DatabaseManager):
    def insert(self, data):
        self.connect()
        cur = self.con.cursor()
        query = "INSERT INTO mega_sena VALUES ({0},'{1}',{2},{3},{4},{5},{6},{7},{8},{9},{10})".format(
            data['contest'],
            data['contest_date'],
            data['first_number'],
            data['second_number'],
            data['third_number'],
            data['fourth_number'],
            data['fifth_number'],
            data['sixth_number'],
            data['winners_sena'],
            data['winners_quina'],
            data['winners_quadra'],
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
