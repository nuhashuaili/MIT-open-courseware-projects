# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:19:13 2020

@author: nuhaa
"""
#==============
#User Inputs
#===============

# print("Hello there this is Nuha! You're planning to buy a house in the near future, congratulations!")

# print("This programme is degined to help you calculate the number of months it would take to save a downpayment for your house.")

# print("Please answer the following questions")

# name=input("What's your name? ")

annual_salary=input('Enter your annaul salary: $ ')
portion_saved=input("Enter the percent of your salary to save, as a decimal: ")
total_cost=input("Enter the cost of your dream home: $ ")

#converiting inputs to floats
annual_salary= float(annual_salary)
portion_saved=float(portion_saved)
total_cost= float(total_cost)

#==============================
#behind the scenes calculations
#==============================

portion_down_payment = total_cost * 0.25
current_savings = 0.00
monthly_salary= annual_salary / 12

r= 0.04

months=0

while current_savings < portion_down_payment:
    
    current_savings = current_savings + (monthly_salary * portion_saved) + (current_savings*(r / 12))
    months += 1   
    
else:
    
    print("Number of months: "+ str(months)
    

    