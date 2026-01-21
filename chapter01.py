print("Hello, World")
# Python is a interpreter language. C/C++/Java - compilational language |
#  dynamic |rich in libraries - numpy, pandas,  pygame and lot more

print('Quote of the day')
print('"With age, you get to a place where \nyou don\'t want to knock people out.\n You just want to give people a hug."')
print('\t\t\t\tVin Diesel \n\t\t\t\tAmerican actor and filmmaker')

# ==================== variables ===============================
utility = 1250
tax = 375
gas = 300
wifi = 1000
communication = 350
cashback = 75

total = utility + tax + gas + wifi + communication - cashback
print(total)

utility = 1500
total = utility + tax + gas + wifi + communication - cashback
print(total)

'''
Problem Statement: 3 locations Mumbai, Pune, Bangalore; 3 modes of travel flight, car, train; 
Calculate cost of travel, time duration
'''

distance_MUM_BAN = 845 # Mumbai to Bangalore is 845 km
distance_MUM_PUN = 150 # Mumbai to Pune is 150 km
distance_BAN_PUN = 840 # Bangalore to Pune is 840 km

flight_MUM_BAN = 12000 # cost of flight from Mumbai to Banaglore in INR
flight_MUM_PUN = 3500 # cost of flight from Mumbai to Pune in INR
flight_BAN_PUN = 11000 # cost of of flight from Banaglore to Pune in INR

car_MUM_BAN = 25000 # cost of car with fuel and toll fare from Mumbai to Banaglore in INR
car_MUM_PUN = 5000 # cost of car with fuel and toll fare from Mumbai to Pune in INR
car_BAN_PUN = 27000 # cost of car with fuel and toll fare from Banaglore to Pune in INR

train_MUM_BAN = 3000 # cost of train from Mumbai to Banaglore in INR
train_MUM_PUN = 850 # cost of train from Mumbai to Pune in INR
train_BAN_PUN = 2900 #cost of train from Banaglore to Pune in INR

source_userinput = input("type your SOURCE of journey as MUM | PUN | BAN")
destination_userinput = input("type your DESTINATION of journey as MUM | PUN | BAN")
duration_userinput = int(input("how much time you can spend on your journey(considered in hours)"))
budget_userinput = int(input("how much amount you will spend on this journey(considered in INR)"))

# Considering flight journey it will not take more than 2 hours;
# train or car journey will be of more than 12 hours for distance more than 800 km

if (source_userinput == 'PUN' and destination_userinput == 'MUM') or (source_userinput == 'MUM' and destination_userinput == 'PUN'):
    if budget_userinput > 3499 and duration_userinput < 2:
        print(f"Kindly Proceed, with the flight from {source_userinput} to {destination_userinput}.\nThe cost will be {flight_MUM_PUN}")
    elif budget_userinput > 3499 and duration_userinput > 2:
        print(f"Kindly Proceed, with the car from {source_userinput} to {destination_userinput}.\nThe cost will be {car_MUM_PUN}")
    elif budget_userinput < 1000 and budget_userinput > 849:
        print(f"Kindly Proceed, with the train from {source_userinput} to {destination_userinput}.\nThe cost will be {train_MUM_PUN}")
    else:
        print("Oops!, you can't have a journey. Low Budget")

if (source_userinput == 'MUM' and destination_userinput == 'BAN') or (source_userinput == 'BAN' and destination_userinput == 'MUM'):
    if budget_userinput > 9999 and duration_userinput < 2:
        print(f"Kindly Proceed, with the flight from {source_userinput} to {destination_userinput}.\nThe cost will be {flight_MUM_BAN}")
    elif budget_userinput > 9999 and duration_userinput > 2:
        print(f"Kindly Proceed, with the car from {source_userinput} to {destination_userinput}.\nThe cost will be {car_MUM_BAN}")
    elif budget_userinput < 3500 and budget_userinput > 2999:
        print(f"Kindly Proceed, with the train from {source_userinput} to {destination_userinput}.\nThe cost will be {train_MUM_BAN}")
    else:
        print("Oops!, you can't have a journey. Low Budget")

if (source_userinput == 'PUN' and destination_userinput == 'BAN') or (source_userinput == 'BAN' and destination_userinput == 'PUN'):
    if budget_userinput > 9999 and duration_userinput < 2:
        print(f"Kindly Proceed, with the flight from {source_userinput} to {destination_userinput}.\nThe cost will be {flight_BAN_PUN}")
    elif budget_userinput > 9999 and duration_userinput > 2:
        print(f"Kindly Proceed, with the car from {source_userinput} to {destination_userinput}.\nThe cost will be {car_BAN_PUN}")
    elif budget_userinput < 3000 and budget_userinput > 2899:
        print(f"Kindly Proceed, with the train from {source_userinput} to {destination_userinput}.\nThe cost will be {train_BAN_PUN}")
    else:
        print("Oops!, you can't have a journey. Low Budget")

# Python follows BODMAS while executing mathematical operations
print(6 - 5.7) # why the result is not 0.3
# as computer machine works on digital logic as 1's or 0's form. 
# On performing floating calculation it generates precise result not accurate result

a = 6
b = 5.7
result = round((a-b), 1)
print(result)
