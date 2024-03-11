import sqlite3

class Database:

    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()

        sql="""
        CREATE TABLE IF NOT EXISTS Tasks(
            task TEXT NOT NULL);
        """
        self.cur.execute(sql)
        self.con.commit()

    def add_tsk(self,task):

        sql=f"INSERT INTO Tasks VALUES(?);"
        self.cur.execute(sql,(task,))
        self.con.commit()

    def task_count(self):
        sql="Select count(task) from Tasks;"
        self.cur.execute(sql)
        g=self.cur.fetchall()
        return g[0][0]

    def get_all(self):
        sql="Select * from Tasks;"
        self.cur.execute(sql)
        g = self.cur.fetchall()
        return g

    def delete_task(self,task):
        sql="DELETE FROM Tasks WHERE task= ?; "
        self.cur.execute(sql,(task,))
        self.con.commit()


    def clear_task(self):
        sql = "DELETE FROM Tasks; "
        self.cur.execute(sql)
        self.con.commit()



if __name__=="__main__":

    db=Database("Tasks.db")