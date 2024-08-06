# this file contains all of the DAO information

# importing the modules 

import mysql.connector
import dbconfig as cfg

class playerDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''

    def __init__(self):
      self.host = cfg.mysql['host']
      self.user = cfg.mysql['user']
      self.password = cfg.mysql['password'] 
      self.database = cfg.mysql['database'] 