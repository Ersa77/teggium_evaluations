import sqlite3
try:
    my_conection = sqlite3.connect("database\mybd")
    cursor= my_conection.cursor()
    cursor.execute("""CREATE TABLE "campaigns_pt_teggium" (
	"id_campaign"	INTEGER NOT NULL,
	"name_campaign"	VARCHAR(50),
	"description"	VARCHAR(100),
	PRIMARY KEY("id_campaign" AUTOINCREMENT)
);""")
except Exception as ex:
    print(ex)