#A Python program that prints a welcome banner. It asks you to pick a vehicle — Bike or Car. It uses a nested if-else inside each branch to ask for a specific model. It prints the name, top speed or seats, and best use case for the chosen model. It handles invalid input with an else at the outer level. It closes with a goodbye message.

print ("---WElCOME TO CUSTOM RIDE BUILDER---")

vehicle = input("Pick a vehicle (Bike or Car): ")

if vehicle == "Bike":
    model = input("Choose a bike mode (Sport or Cruiser):")
    if model == "Sport":
        print("Sport Bike: Roughly 100 to 120 mph . Best for racing.")
    else:
        print("Cruiser Bike: Roughly 43 to 56 mph . Best for touring.")
elif vehicle == "Car":
    model = input("Choose Honda or SUV: ")
    if model == "Honda":
        print("Honda-Seating Capacity: 5 seats . Best for city driving")
    else:
        print("SUV- Seating Capacity: Ranges from 5 to 8 passengers. Best for trips.")

else: 
    print("invalid input")

print("Goodbye. <3")