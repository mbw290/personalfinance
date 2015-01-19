#!/usr/bin/python

import mysql.connector
debug=1
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

  #print result

pfDBConnect("127.0.0.1","svc_mysql","cbVMI3i6Ol","personalfinance","show tables")
