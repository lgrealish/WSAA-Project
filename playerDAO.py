# playerDAO.py
# Author: Linda Grealish
# this file contains all of the DAO information

# importing the modules 

import mysql.connector
import dbconfig as cfg

# Create a class to include all functions
class PlayerDAO:
    host=       ''
    user=       ''
    password=   ''
    database=   ''

    connection=""
    cursor =''

# Create function to set up variables and attributes required for SQL queries
    def __init__(self):
      self.host = cfg.mysql['host']
      self.user = cfg.mysql['user']
      self.password = cfg.mysql['password'] 
      self.database = cfg.mysql['database'] 

# Create getcursor function to establish connection to My SQL and returns a cursor object used for executing SQL commands
    def getcursor(self): 
       self.connection = mysql.connector.connect(
           host=       self.host,
           user=       self.user,
           password=   self.password,
           database=   self.database,
        )
       self.cursor = self.connection.cursor()
       return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

# Create function to select all record in database        
    def getAll(self):
        cursor = self.getcursor()
        sql="select * from player"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []       
        for result in results:           
            returnArray.append(self.convertToDictionary(result))        
        self.closeAll()
        return returnArray

# Create function to search for record in database by name  
    def findbyname(self, name):
        cursor = self.getcursor()
        sql="select * from player where name = %s"
        values = (name,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

# Create function to create new record in database with incremental id assignment
    def create(self, player):
        cursor = self.getcursor()
        sql="insert into player (Name, Club, Age, Position) values (%s,%s,%s,%s)"
        values = (player.get("Name"), player.get("Club"), player.get("Age"), player.get("Position"))
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        player["id"] = newid
        self.closeAll()
        return player

# Create function to update existing records
    def update(self, id, player):
        cursor = self.getcursor()
        sql="update player set Name= %s, Club=%s, Age=%s, Position=%s"        
        values = (player.get("Name"), player.get("Club"), player.get("Age"), player.get("Position"),id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

# Create function to delete existing records        
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from player where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
        print("Player record deleted")

# Create a function that takes a list of player attributes and outputs as a dictionary object
    def convertToDictionary(self, resultLine):
        attkeys=["id","name","club", "age", "position"]
        player = {}
        currentkey = 0
        for attrib in resultLine:
            player[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return player

# Class init        
playerDAO = PlayerDAO()