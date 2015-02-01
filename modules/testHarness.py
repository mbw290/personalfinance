#!/usr/bin/python
import dbConnect

print ("WELCOME TO THE PERSONAL FINANCE APPLICATION\n")

choice = raw_input ("Please enter a choice 1. Enter account")


config = [line.rstrip() for line in open('pass.txt')]
hostname=config[0]
user=config[1]
password=config[2]
database=config[3]


dbConnect.pfDBConnect(hostname,user,password,database,"describe account")
