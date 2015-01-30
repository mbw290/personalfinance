#!/usr/bin/python

import mysql.connector
debug=1


#connect to database
def pfDBConnect (hostname,user,password,database,task):
  cnx = mysql.connector.connect(user=user, password=password,
                              host=hostname,
                              database=database)


  cursor = cnx.cursor()

  if debug == 1:
    query = (task)
    cursor.execute(query)
    for row in cursor:
      print row
  cursor.close()
  cnx.close()


config = [line.rstrip() for line in open('pass.txt')]
hostname=config[0]
user=config[1]
password=config[2]
database=config[3]

pfDBConnect(hostname,user,password,database,"describe account")
