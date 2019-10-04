# What is an octothorpe?
# <- This is an octothrope.
# What is the octothorpe used for in python?
# Notes, also known in the programming community as Comments

print("hello world")
print("howdy y'all")
print("I like typing this")
print("Printing....Yay!!!")

# Practice with Maths and things
print("I will now count my chickens")
print("Hens", 25 + 30 / 6)
print("Roosters: ", 100 - 25 * 3 % 4)
print("Now I will count the eggs:")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 +6)
print(" Is it true that 3 + 2 < 5 -7?")
print(3 + 2 < 5 - 7)

#print about how many stamps i have
print("how many ounces of milk do I have")
#now I am going to add my equation and get my answer
print(3.0 + 0.5)
#put in math equation for how many stamps I have and made the floating numbers only go to 2 floating numbers
print("%.2f" % 3.5)
#by inputing this command I now made my equation go to 2 decimal places in order to make it more precise
#This way I can make sure that my equation is precise for someone who needs it


# variables
cars = 80
space_in_a_car = 4.0
drivers = 40
passengers = 115
CarsNotDriven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven

print("There are" ,cars, "cars available")
print("There are only" ,drivers, "drivers available")
print("There will b", CarsNotDriven, "people today")
print("We can transport" , carpool_capacity, "people today")
print("We have" ,passengers, "to carpool today")
print("We need to put about" ,average_passengers_per_car, "in each car")

# More variables

myName = "Blazin"
myAge = 420
myHeight = 72 # inches
myEyes = "Yellow"
myTeeth = "Black"
myHair = "Curly"

print("Let's talk about %s." % myName)
print("He's %d inches tall." % myHeight)
print("He's got %s eyes and %s hair." % (myEyes, myHair))
