#!/usr/bin/python

import datetime, sys

def age_try():
	try:
		age=int(input("Enter age: "))
		return age
	except:
		return False


name=input("Enter name: ")
last_name=input("Enter last name: ")
age=age_try()
while age==False or age <=0 or age>=100:
	print("Enter correct age")
	age=age_try()
		
now=datetime.datetime.now()
exp_year=(100-age)+now.year


print("\n",name,"\n","Year, when you'll be 100 yo:",exp_year)

if exp_year%4==0 and exp_year%100!=0 or exp_year%400==0:
	print(" Leap year!")
else:
	print(" Not a leap year!")
