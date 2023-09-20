# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 19:44:30 2021

@author: nuhaa
"""


# Inputs
starting_annual_salary = float(input('Enter the starting annual salary: ').strip())
monthly_salary = starting_annual_salary / 12   
# Assumptions
semi_annual_raise = 0.07
r = 0.04
total_cost = 1000000
down_payment = total_cost/4
current_savings = 0
total_money = 0
portion_saved = 0.5 # for the bisection search
investment = 0
steps = 0

def bisection(steps, portion_saved, down_payment, total_savings)
    """ conducts a bisection search
    inputs: steps, portion_saved, down_payment, total_savings 
    returns: portion_saved, steps"""
        
    low = 0
    high = 1

    if (total_savings * portion_saved) < down_payment:
        low = portion_saved

    elif (total_savings * portion_saved) > down_payment:
        high = portion_saved
    
    portion_saved = (high + low) / 2 
    
    steps += 1
return portion_saved, steps


# total savings

total_savings=0 #to calculate the annual salary with the semi annual raise

for months in range(36):

    if ((months + 1) % 6) == 0 and months != 0:    #factoring in the semi annual raise, subtracted one from the month so that the raise will be added to the month after the 6th 12th etc
        monthly_salary = monthly_salary + (semi_annual_raise * monthly_salary )

    if ((months + 1) % 12) == 0 and months != 0:   #factoring in annual savings
        investment = investment + (total_savings * r)
        total_savings += investment
            
    total_savings += monthly_salary

    
    
while abs(down_payment - (total_savings*portion_saved))>100:   # factorizing in the $100 descrepancy allowed
    
    bisection(steps, portion_saved, down_payment, total_savings)



     






