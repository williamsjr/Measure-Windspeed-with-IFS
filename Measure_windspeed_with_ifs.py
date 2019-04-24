windspeed = eval(input("How fast was the wind in the storm: "))

if windspeed < 74:
    print("NO CATEGORY - NOT A STORM")
elif windspeed in range(74, 96):
    print("Category 1")
elif windspeed in range(96, 111):
    print("Category 2")
elif windspeed in range(111, 131):
    print("Category 3")
elif windspeed in range(131, 156):
    print("Category 4")
elif windspeed > 156:
    print("Category 5")