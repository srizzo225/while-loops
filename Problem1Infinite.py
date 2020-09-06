#Sara Margaret Rizzo
#2020-09-06

#Problem 1: Write an infinite loop that prints “Infinite”. 
#An infinite loop never ends. The condition is always true. 

#Proceed with caution, it seems Visual Studio Code doesn't have any kind of built in break, 
#so eventually it just freezes and you need to restart the program. Make sure all work is saved!

#random variable to keep the loop going
n = 10

#function that gets stuck in an infinite loop
def infinite(n):
    #we're not doing anything to alter n, so it will always be less than 11
    while n < 11:
            print("Infinite")
    return n

#start the loop. 
print(infinite(n))
