# -*- coding: utf-8 -*-
"""
Created on Sat May 30 19:36:43 2020

@author: nuhaa
"""

#==============
#User Inputs
#===============

annual_salary = input('Enter your starting annaul salary: $ ')
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
total_cost = input("Enter the cost of your dream home: $ ")
semi_annual_raise = input("Enter the decimal percentage of your semi annual raise: ")

#converiting input strings to floats

annual_salary = float(annual_salary)
portion_saved = float(portion_saved)
total_cost = float(total_cost)
semi_annual_raise = float(semi_annual_raise)


#==============================
#behind the scenes calculations
#==============================

portion_down_payment = total_cost * 0.25
current_savings = 0.00
monthly_salary = annual_salary / 12
r = 0.04   #decimal percentage of investment return


months = 0    #setting a counter to count the months needed to save for a downpayment

#second attempt with a more pythonic code

while current_savings < portion_down_payment:
    
    if ((months-1) %6)==0 and months !=0 : #factoring in the semi annual raise, subtracted one from the month so that the raise will be added to the month after the 6th 12th etc excluding month 1 which would turn month-1 to 0        
        monthly_salary = monthly_salary+ (semi_annual_raise* monthly_salary )
 
    current_savings+= (monthly_salary * portion_saved) + (current_savings*(r / 12))
    months+=1  

print("Number of months: "+ str(months))

#=============
#first attempt, the code was not pythonic


# while current_savings < portion_down_payment:

#     if months <=6:
        
#         current_savings = current_savings + (monthly_salary * portion_saved) + (current_savings*(r / 12))
#         months+=1         
         
#     elif ((months -1)%6)==0:    #factoring in the semi annual raise, subtracted one from the month so that the raise will be added to the month after the 6th 12th etc 
        
#         monthly_salary = monthly_salary+ (semi_annual_raise* monthly_salary )    
#         current_savings = current_savings + (monthly_salary * portion_saved) + (current_savings*(r / 12))
#         months+=1                    
    
#     else: 
        
#         current_savings = current_savings + (monthly_salary * portion_saved) + (current_savings*(r / 12))
#         months+=1  

# else:
    
#     print("Number of months: "+ str(months))
