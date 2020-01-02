#Program to learn on the if, if else, if elif and else.

customData=int(input("Enter the room temperature: "))# Performing type conversion at the time of input receving from user

if ((customData > 25) and (customData <=28)):
    print("The temperature is at room temperature")
    print("Performing only IF statement")

if (customData < 0):
   print("It's freezing over there")
   print("Performed IF ELSE statement")
else:
   print("Temperature is warmer")
   print("Performed IF ELSE statement")

if (customData < 0):
   print("It's freezing over there")
   print("Performed IF ELIF ELSE statement")
elif ((customData >25) and (customData <=28)):
   print("Temp is Perfect for ROOM")
   print("Performed IF ELIF ELSE statement")
else:
   print("Temp is BURING")
   print("Performed IF ELIF ELSE statement")
