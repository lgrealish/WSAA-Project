import mysql.connector


mysql = {
    'host':"localhost",
    'user':"root",
    'password':"",
    'database':"player_info"
}


'''
db =  mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="player_info"
)

cursor = db.cursor()

cursor.execute("create DATABASE player_info")
cursor.close()
db.close()

cursor = db.cursor()
'''