# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:22:00 2019

@author: Mannawar Hussain
"""

# def total_cost(): # no need
    #def portion_down_payment(): # wrong, no need
        
        
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 14:22:00 2019

@author: Mannawar Hussain
"""

# def total_cost(): # no need
    #def portion_down_payment(): # wrong, no need
        
        
x = float(input("Enter your annual salary:"))
y= float(input("Enter the percent of salary to save, as decimal input:"))
z= float(input("Enter the cost of your dream home: "))

monthly_savings = (x/12)*y
portion_down_payment = 0.25
down_payment = portion_down_payment * z

annual_return =0.04
current_saving = 0.0
number_of_months = 0

while current_saving<down_payment:
    current_saving += monthly_savings + (current_saving * annual_return)/12
    number_of_months += 1
       
print("Number of months: {}".format(number_of_months))



        
    
    
    
    #current_saving =0
     #   current_saving = ((x/12)*(.25)) 
      #  portion_saved_monthly = ("current_saving") + ("current_saving") * 0.04)
       # Number_of_months_for_down_payment = (z*0.25)/portion_saved_monthly
        








# =============================================================================
# x = float(input("Enter your annual salary:"))
# y= float(input("Enter the percent of salary to save, as decimal input:"))
# z= float(input("Enter the cost of your dream home: "))
# 
# monthly_savings = (x/12)*y
# portion_down_payment = 0.25
# down_payment = portion_down_payment * z
# portion_saved_monthly += current_saving + (current_saving * 0.04)
# current_saving =0
# Number_of_months_for_down_payment = 0
# 
# while portion_saved_monthly < down_payment:
#       current_saving += ((x/12)*(.25)) 
#       
#       Number_of_months_for_down_payment = (z*0.25)/portion_saved_monthly
#  
# print("Number_of_months_for_down_payment: {}".format(Number_of_months_for_down_payment))
# 
# =============================================================================



       