# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 17:18:04 2021

@author: Nithin
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost
monthly_saved = portion_saved * (annual_salary / 12)
current_savings = 0
months = 0

while current_savings < down_payment:
    current_savings += (monthly_saved + ((current_savings * 0.04) / 12))
    months += 1
    
print("Number of months:", months)