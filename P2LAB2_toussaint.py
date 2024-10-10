# Nexabet Toussaint
# 10/10/2024
# P2LAB2
# Using dictionaries

# create a dictionary
cars = {"camaro":18.21, "prius":52.36, "Model S":110, "Silverado":26}

# VAriable to hold the keys
keys = cars.keys()

# Show all the keys to the user
print(keys)

# Get a car (key) from the user
selected_car = input("Enter a vehicle to see it's mpg: ")

# Display the selected car and it's mpg
print(f"The {selected_car} gets {cars[selected_car]} mpg")

# Display How many miles you will drive
miles_planned = int(input(f"How many miles will you drive the {selected_car}: "))

#calculate how many gallons to drive a distance
gas_needed = miles_planned / cars[selected_car]


# Display the gallons of gas needed to drive a certain amount of miles
print(f"{gas_needed: .2f} gallon(s) of gas are needed to drive the {selected_car}, {miles_planned}, miles.")


