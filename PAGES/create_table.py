import sqlite3 as sql


def main():
    try:
        vt = sql.connect("./db/mxsoftware.db")

        im = vt.cursor()
        im.execute("CREATE TABLE IF NOT EXISTS details (tc TEXT,date_of_birth TEXT,belt_color TEXT,"
                   "veli_name TEXT,veli_number TEXT,"
                   "lisans_no TEXT,photo BLOB , hes_code TEXT,mail TEXT)")

        vt.commit()

        db = sql.connect('./db/mxsoftware.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE IF NOT EXISTS ogrenciler (tc TEXT UNIQUE, isim TEXT,soyad TEXT, telefon TEXT, brans TEXT, kayit_tarihi TEXT, bitis_tarihi TEXT)"
        tablequery3 = "CREATE TABLE IF NOT EXISTS aidatlar (Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,tc TEXT,isim TEXT,soyad TEXT , ay TEXT, yıl TEXT , ucret TEXT)"
        tablequery4 = "CREATE TABLE IF NOT EXISTS dereceler (Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,tc TEXT,isim TEXT,soyad TEXT , brans TEXT, turnuva_adi TEXT , turnuva_yeri TEXT,derece TEXT)"
        tablequery5 = "CREATE TABLE IF NOT EXISTS psiko (Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,tc TEXT,isim TEXT,soyad TEXT , tarih TEXT, boy TEXT , kilo TEXT,denge TEXT,uzun_atlama TEXT,dikey_sicrama TEXT,esneklik TEXT,kisa_metre TEXT,uzun_metre TEXT)"
        cur.execute(tablequery)
        cur.execute(tablequery3)
        cur.execute(tablequery4)
        cur.execute(tablequery5)
        db.commit()

    except sql.Error as e:
        print("There is a table or an error has occurred")

    finally:

        db.close()
        vt.close()


if __name__ == "__main__":
    main()