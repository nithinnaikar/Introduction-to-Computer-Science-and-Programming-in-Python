# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 18:31:26 2021

@author: Nithin

**NOTE: Early version of program. Needs refining.
"""

annual_salary = float(input("Enter your annual salary: "))

total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost
current_savings = 0
months = 1

def compute_current_savings(annual_salary, portion_saved):
    current_savings = 0
    for month in range(36):
        if months % 6 == 0 and months != 0:
            annual_salary += (semi_annual_raise * annual_salary)
       
        current_savings += ((portion_saved * (annual_salary / 12)) + ((current_savings * 0.04) / 12))
    return annual_salary, current_savings

low = 0
high = 10000
portion_saved = (high + low) / 2.0

annual_salary, current_savings = compute_current_savings(annual_salary, portion_saved/10000)

steps = 0
while abs(current_savings - down_payment) > 100:
    if current_savings < down_payment:
        low = portion_saved
    else:
        high = portion_saved
        
    portion_saved = (high + low) / 2.0
    
    annual_salary, current_savings = compute_current_savings(annual_salary, portion_saved/10000)
    steps += 1
    
print(portion_saved/10000)
print(steps)
    
