#If the script fails, copy the line below this to your terminal and run.
#python3 -m pip install numpy scipy

import numpy as np
import scipy
import sys, math, random


###Commenting:

#This line has been commented out.
print("After this, the following bits have been commented out.") #See you dont get the rest of this text.
#or this.
#or even this.


###Printing:
print()
print("Hello World")
print(3)
print("This works?")
print("You", "can", "have", "multiple", "items")
print([1,2,3,4])
print()
#Feel free to add your own print commands below.




print()




###Variables:
variables = 3
are = 4.0
easy = "This is more than one word..."
butPleaseUseGoodNamingSchemes = 'a'

a = 10
b = 15
c = a * b

d, e, f = 20, 25, 30

print(c, math.log(c), easy, butPleaseUseGoodNamingSchemes)
print(d, e, f, d + e)



#As a quick side note, ^ is not the same as "raised to the power of"
print(a, a^2, a * a, a**2)


#######################
#########Loops#########
#######################
example_data_set = [29, 63, 74, 13, 44, 18, 53, 8, 68, 92]

for x in example_data_set:
    print(x)

i = 0
while i < 10:
    #We can use if statements if we want to do different things within the loop.
    if i == 9:
        print("Yikes we are at 9")
    elif i == 5:
        i += 1
        continue
    else:
        print(i)
        
    #Always occurs.
    i += 1

summation = 0
for x in example_data_set:
    summation += x
    
#To check our work lets divide the sum by the length of the vector. (To avoid integer division we multiply by 1.0)
print("Our work:", summation * 1.0 / len(example_data_set))

#We can check our work using the numpy mean function
print("Numpy results:", np.mean(example_data_set))
print()





#######################
#######Functions#######
#######################
def sayHello():
    print("Dont tell me what to do.")
    
sayHello()

def mean(data):
    result = 0
    for item in data:
        result += item
    return result * 1.0 / len(data)

def raiseToThePower(number, power):
    return number ** power

def giveMeLotsOfStuff():
    return 1, 2, 3, "Hi", 5, 6

temp_array = [1,2,3,4,5,6,7,8,9,10]
print(mean(temp_array))

#Parameters by default fill in order but, if you want, you can specify which parameter you want to fill.
print(raiseToThePower(5,3))
print(raiseToThePower(power=3, number=5))

#You can return multiple items.
a, b, c, d, e, f = giveMeLotsOfStuff()
print("Multiple Items:", a, b, c, d, e, f)
print()


