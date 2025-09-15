#Write a Python script to merge two Python dictionaries?

d1 = {10:100,20:200,30:300,40:400}
d2 = {40:450,50:500,60:600}

for i in d2:               #40,50,60
    d1[i] = d2[i]             #d1[40]=d2[450] creation

print(d1)

