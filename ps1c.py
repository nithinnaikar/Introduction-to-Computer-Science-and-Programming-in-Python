# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 18:31:26 2021

@author: Nithin
"""

annual_salary = float(input("Enter your annual salary: "))

total_cost = 1000000
portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost


def compute_current_savings(annual_salary, portion_saved):
    '''
    Takes input the annual salary and portion saved, simulates the process over
    36 months, then returns the resulting savings; implemented in constant O(1) time
    '''
    current_savings = 0
    for month in range(36):
        if month % 6 == 0 and month != 0:
            annual_salary += (0.07 * annual_salary)
       
        current_savings += (((portion_saved * annual_salary) / 12) + ((current_savings * 0.04) / 12))
    return current_savings

low = 0
high = 10000
portion_saved = (high + low) / 2.0

current_savings = compute_current_savings(annual_salary, portion_saved/10000)

steps = 0
while abs(current_savings - down_payment) > 100:
    if current_savings < down_payment:
        low = portion_saved
    else:
        high = portion_saved
        
    portion_saved = (high + low) / 2.0
    
    current_savings = compute_current_savings(annual_salary, portion_saved/10000)
    steps += 1
    
print("Best savings rate:", portion_saved/10000)
print("Steps in binary search:", steps)
    
