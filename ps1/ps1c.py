# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 19:44:30 2021

@author: nuhaa
"""


# Inputs
starting_annual_salary = input('Enter the starting annual salary: ')
monthly_salary=float(starting_annual_salary)/12   
# Assumptions
semi_annual_raise= 0.07
r= 0.04
total_cost= 1000000
down_payment = total_cost/4
current_savings=0
total_money=0
months=0





# monthly salary function

def pbisection(down_payment,monthly_salary,semi_annual_raise):
    """
    Input: will (low,high,portion_saved)
    Returns the portion saved from the salary

    """
    total_savings=0 #to calculate the annual salary with the semi annual raise
    
    for months in range(36):
    
        if ((months -1)%6)==0 and months != 0:    #factoring in the semi annual raise, subtracted one from the month so that the raise will be added to the month after the 6th 12th etc
            monthly_salary = monthly_salary+(semi_annual_raise* monthly_salary )
                
        total_savings+=monthly_salary
    
    # Bisection method variables   
    bisection_steps=0
    low=0
    high=1
    portion_saved=(low+high)/2.0
    
    while abs(down_payment - (total_savings*portion_saved))>100:   # factorizing in the $100 descrepancy allowed

    #code to calculate the percentage to save using bisection method               
    # if bisection_steps>36: #for 1 bisection step =1 month passes        
    #    print('It is not possible to pay the downpayment in three years')
        # break
        # print('current savings ' +str(current_savings))
        # print('down payment '+str(down_payment))         
               
        if total_savings<down_payment:            
            print("It is not possible to pay the downpayment in three years")
            break 
    
        elif (total_savings*portion_saved) < down_payment:
            low= portion_saved
        else:
            high=portion_saved
        
        portion_saved=(high+low)/2.0 
        #current_savings = current_savings + (monthly_salary * portion_saved + (current_savings*(r / 12))          
        bisection_steps +=1
           
    print('best savings rate is '+str(portion_saved))
    print('Steps in bisection search: '+str(bisection_steps))
    #print('down payment '+str(down_payment)) 
    
    return portion_saved

x=1      
while current_savings < down_payment: #range is set to the maximum number of months
        
        # code to calculate the monthly salary
    if ((months -1)%6)==0 and months != 0:    #factoring in the semi annual raise, subtracted one from the month so that the raise will be added to the month after the 6th 12th etc
        monthly_salary = monthly_salary+(semi_annual_raise* monthly_salary )
            
#i should make another bisection loop to get the best rate with the investment
        
    current_savings = current_savings + (monthly_salary * pbisection(down_payment,monthly_salary,semi_annual_raise)) + (current_savings*(r / 12))
    months+=1
   
   

    
    #print(current_savings)



    
   # print('Steps in bisection search: '+str(bisection_steps)+"\n Best savings rate: "+str(pbisection(down_payment,current_savings)))


