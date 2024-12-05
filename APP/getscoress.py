import sqlite3

class ScoresTables:

    def __init__(self):
        self.conn = sqlite3.connect('game_data.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                time INTEGER,
                level INTEGER
            )
        ''')
        self.conn.commit()

    def add_score(self, time, level):
        try:
            self.cursor.execute('''
                INSERT INTO game_scores (time, level) VALUES (?, ?)
            ''', (time, level))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def fetch_scores(self):
        try:
            self.cursor.execute('SELECT * FROM game_scores')
            return self.cursor.fetchall()  # Return all scores
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []

    def close(self):
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    scores_table = ScoresTables()
    #scores_table.add_score(120, 1)
    scores = scores_table.fetch_scores()
    print(scores)
    scores_table.close()