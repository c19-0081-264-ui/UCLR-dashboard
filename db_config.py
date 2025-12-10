import MySQLdb

def get_db_connection():
    return MySQLdb.connect(
        host = "localhost",
        user = "root",
        passwd = "PrincessCabrera88",
        database = "school_db",
    )