''' For understanding solve this questionj
take the input of temperature in celsiusX
Below 0°C → "Freezing Cold
0°C to 10°C → "Very Cold
10°C to 20°C → "Cold
20°C to 30°C → "Pleasant
30°C to 40°C → "Hot 
Above 40°C → "Very Hot "'''


temp=int(input("Enter temperature: "))

if temp<0:
    print("Freezing Cold")
elif 0<temp<10:
    print("Very Cold")
elif 10<temp<20:
    print("cold")    
elif 20<temp<30:
    print("Pleasant")    
elif 30<temp<40:
    print("hot")
else:
    print("very hot")        