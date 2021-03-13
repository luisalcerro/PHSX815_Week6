import numpy as np
from random import seed
from random import random
import scipy.integrate as integrate

###########  MONTE CARLO ####################
def MonteCarlo(f, a, b, n):
    subint = np.arange(0, n+1, n/10000)
    u = np.zeros(n)
    for i in range(10000):
        lim1 =int(subint[i])
        lim2 = int(subint[i+1])
        u[lim1:lim2] = np.random.uniform(i/10000, (i+1)/10000, lim2-lim1)
    arr = f(a+(b-a)*u)
    total = ((b-a)/n)*(arr.sum())
    return total
########### TRAPEZOIDAL RULE #################
def h (a, b, n):
	return (b-a)/float(n)

def trap_rule (f, a, b, n):
	total = f(a)+f(b)
	dx = h(a, b, n)
	for k in range (1, n):
        	total = total + 2.0*f((a + (k*dx)))
	return dx/2.0*total
######### FUNCTION TO INTEGRATE #############   
def f(x):
    return (np.cos(x))**5*np.exp(-x/2.0)
##############################################
print("We are integrating the function cos(x)^5 exp(-x/2) in the interval [5,20]: \n")
print("Enter number of random points to evaluate: ")
num = int(input())
I_exact = 0.038964609200183953761884221510468
I_MC = MonteCarlo(f, 5.0, 20.0, num)
I_trap = trap_rule(f, 5.0, 20.0, num)
I_gauss = integrate.fixed_quad(f, 5.0, 20.0, n=num)
print("\nExact:\n", I_exact)
print("Monte Carlo:\n", I_MC)
print("Trapezoidal method:\n", I_trap)
print("Gaussian quadrature:\n", I_gauss[0])
print("\nErrors:\n")
print("Iexact-I_MonteCarlo: ", I_exact-I_MC)
print("Iexact-Itrapezoidal: ", I_exact-I_trap)
print("Iexact-Igauss_quad: ", I_exact-I_gauss[0])
