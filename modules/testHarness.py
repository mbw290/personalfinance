#!/usr/bin/python
import dbConnect

print ("WELCOME TO THE PERSONAL FINANCE APPLICATION\n")

choice = raw_input ("Please enter a choice 1. Enter account\n")


config = [line.rstrip() for line in open('pass.txt')]
hostname=config[0]
user=config[1]
password=config[2]
database=config[3]

if choice == "1":
  acctpk = raw_input ("How many accounts do you already have in the system?")
  acctpk = int(acctpk)+1
  acctnum = raw_input ("Please enter your accunt number:")
  acctnum = int(acctnum)
  desc = raw_input ("Please enter an account description:")
  accttypechoice = raw_input ("Is the account checking (1) or savings (2)")
  if accttypechoice == "1":
    accttype = "checking"
  else:
    accttype = "savings"

#INSERT INTO account (account_pk,account_num,description,acct_type )  VALUES (2,1234 ,'myacct' ,'checking');
query = "INSERT INTO account (account_pk,account_num,description,acct_type )  VALUES (%s,%s,'%s','%s');" % (acctpk,acctnum,desc,accttype)
print query
dbConnect.pfDBConnect(hostname,user,password,database,query)
