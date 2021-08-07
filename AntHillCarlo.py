import numpy
import sympy as sym
import random

x = sym.Symbol('x')
y = sym.Symbol('x')

#We specify the boundary here
boundary = ((x-2.5)/30)**2 + ((y-2.5)/40)**2

#This is just for testing
#print(boundary.subs([(x,30),(y,30)]))

#We set a seed
random.seed(55)

def findtime(boundary, runs):
    """
    Returns the average time it takes for an ant starting at [0,0] to reach the boundary with a random walk in one direction of 10cm per second. Montecarlo approach.

    Inputs: boundary (a sympy expression with variables x and y we can evaluate), runs (the number of simulations we run)

    Outputs: The average time it takes for the ant to reach the food on the boundary
    """
    times = []

    for i in range(runs):
        antpos = [0,0]
        time = 0
        while(boundary.subs([(x,antpos[0]),(y,antpos[1])]) < 1):

            #We update the time
            time+=1

            #We randomly generate a movement
            movement = random.randint(0,3)
            
            #Depending on the int returned by our generator, we move up or down or left or right by 10 cm
            if (movement == 0):
                antpos[0]+=10
            if (movement == 1):
                antpos[0]-=10
            if (movement == 2):
                antpos[1]+=10
            if (movement == 3):
                antpos[1]=10
        #We append how many seconds it took this run
        times.append(time)
    #And endlich we return the average time
    return sum(times)/len(times)

print(findtime(boundary, 200))