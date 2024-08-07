import sqlite3
from tkinter import messagebox
import pandas as pd

class Db:
    def __init__(self):
        self.conn = sqlite3.connect(database="password.db")
        self.cursor = self.conn.cursor()
        password_query = """CREATE TABLE IF NOT EXISTS password(
                website TEXT PRIMARY KEY,
                email TEXT,
                password TEXT,
                status TEXT
                )
                """
        self.cursor.execute(password_query)
        self.conn.commit()
    def insert_new_info(self, website: str, email: str, password: str, status: str):
        """
        It takes user's info and saved it in the database.
        :param website: website name (it should be unique)
        :param email: email address
        :param password: password
        :param status: normal/encrypted
        :return: None
        """
        query = f"""INSERT INTO password VALUES
                    ('{website}', '{email}', '{password}', '{status}')
                    """
        try:
            self.cursor.execute(query)

            # commit the changes
            self.conn.commit()
            messagebox.showinfo(title="Successful", message="Details saved successfully!!")

        except sqlite3.IntegrityError:
            messagebox.showwarning(title="Failed", message="Website name is not already present.\nIt"
                                                           "should be unique.")

    # searching passwords
    def search_password(self, website):
        query = f"""SELECT * FROM password
                    WHERE website LIKE '%{website}%'
                    """
        self.cursor.execute(query)
        result = self.cursor.fetchall()   # it returns list of tuples. All matching records will be fetched.
        # print(result)
        return result


    def delete_data(self, website):
        try:
            query = f"""DELETE FROM password
                        WHERE website = '{website}'
                    """
            self.cursor.execute(query)
            self.conn.commit()
            return 1
        except:
            messagebox.showwarning(title="Failed", message="Error in query")
            return 0

    def delete_all_pass(self):
        try:
            query = """DELETE FROM password;"""
            self.cursor.execute(query)
            self.conn.commit()

            self.cursor.execute("VACUUM;")
            return 1
        except:
            messagebox.showwarning(title="Failed", message="Error in query")
            return 0

    def total_count(self):
        self.cursor.execute("""SELECT COUNT(*) FROM password""")
        return self.cursor.fetchone()[0]  # as it returns in the form tuple.

    def data_status(self, website):
        query = f"""SELECT * FROM password
                            WHERE website = '{website}'
                            """
        self.cursor.execute(query)
        result = self.cursor.fetchone()[3]
        if result == "normal":
            return 0
        else:
            return 1
    def close_connection(self):
        self.conn.close()

    def export_pass(self):
        df = pd.read_sql("SELECT * FROM password", self.conn)
        return df

    def import_pass(self, filepath):
        df = pd.read_csv(filepath)
        df.to_sql(name="password", con=self.conn, if_exists="replace", index=False)
        return 1
