weight = input("Weight: ")
mass = input("(K)g or (L)bs: ")
if mass.upper() == "K":
    print("Weight in pounds: " + str(float(weight) * 2.2046226))
elif mass.upper() == "L":
    print("Weight in kilograms: " + str(float(weight)/2.2046226))
else:
    print("Wrong input!")
