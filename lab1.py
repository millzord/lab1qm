import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("results.txt", unpack=True, delimiter=" ") #import data from a plain text file
wavelength = data[1] #collect data for y axis
temp = data[0] #collect data for x axis
tempinv = 1/temp #invert temperature to get 1/T

plt.scatter(tempinv, wavelength) #plot the data
plt.xlabel('Temperature 1/T (K)') #label x axis
plt.ylabel('Max wavelength λ (µm)') #label y axis
fit = np.polyfit(tempinv, wavelength, 1) #fit a straight line for a linear graph
gradient = fit[0] #collect gradient data
intercept = fit[1] #collect intercept data
xmax = np.min(tempinv) #define minimum x value
xmin = np.max(tempinv) #define maximum x value
xl = np.array([xmin, xmax]) #create an array with the min and max x values
yl = gradient*xl+intercept #calculate  y values for the line of best fit between min and max x values
fitY = gradient*tempinv+intercept #calculate predicted y values for each value of 1/T
deltaY = (wavelength-fitY)*(wavelength-fitY) #calculate the difference between actual values and fitted y values, but squared
# use the lecture notes formula for uncertainty, multiply by a fraction because I'm scared of how python would interpret it otherwise
uncertainty = (np.sqrt(sum(deltaY)/(len(tempinv)-1))*(1/(xmax-xmin)))*-1 #calculate the uncertainty in gradient, don't square deltaY it's already squared when defined.
plt.plot(xl, yl, 'r') #finally plot the line on the graph
print("gradient =",gradient,'λT') #print the gradient
print("intercept =",intercept,"λ") # print the intercept
print("uncertainty in gradient =",uncertainty, "λT")#print the uncertainty

h = 6.62607015*10**-34 #define Planck's constant
c = 299792458 #define speed of light
k = 1.380649*10**-23 #define the boltzmann constant
pi = np.pi #define pi with numpy
e = np.exp #define e as the exponential function with numpy
x = 4.96511 #using the value found for x from theory C
hc = h*c #define hc for ease
xk = x*k #define xk for ease
bp = hc/xk #define the constant b for Planck's formula
# print(bp) just checking
check = bp/temp
# print(check) check the theoretical value
# b = gradient ##just to remind myself
# h = bkx/c ##another reminder
bup = gradient+uncertainty
bdown = gradient-uncertainty
hplanck = (gradient*k*x)/c # quick maths
hplup = (bup*k*x)/c
hpldown = (bdown*k*x)/c
testplanck = h-hplanck
print("h value from Planck's formula",hplanck) # print my h value from Planck's formula
print("difference between theoretical and experimental value for hplanck",testplanck)
hwien = (gradient*k*5)/c #quick maths again
hwienup = (bup*k*5)/c
hwiendown = (bdown*k*5)/c
testwien = h-hwien
testhwien = h-hwiendown
print(testhwien)
print("h value from Wien's formula",hwien) # print my h value from Wien's formula
print("difference between theoretical and experimental value for hwien",testwien)
plt.show() #show the scatter plot just to check, do it at the end so it prints everything
print("planck upper",hplup)
print("planck lower",hpldown)
print("wien upper",hwienup)
print("wien lower",hwiendown)
delhplanck = hplup-hpldown
delhwien = hwienup-hwiendown
print("del h plank", delhplanck)
print("del h wien", delhwien)
