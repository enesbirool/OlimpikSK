import sqlite3 as sql
import os

def main():
    dirName = './db'
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    else:    
        pass
    try:
       db = sql.connect('./db/mxsoftware.db')
    except Exception as error:
        print("Hata Mesajı : "+error)
    finally:
        db.close()

if __name__ == "__main__":
    main()