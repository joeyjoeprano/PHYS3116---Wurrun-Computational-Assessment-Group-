import importlib.util
import sys
import subprocess

def check_and_install(package_name):
    # Check if the package is installed
    spec = importlib.util.find_spec(package_name)
    
    if spec is None:
        # Install if it is not found
        print(f" '{package_name}' not found. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    else:
        print(f" '{package_name}' is already installed.")

check_and_install("numpy")
check_and_install("matplotlib")
check_and_install("cmasher")
check_and_install("astropy")
check_and_install("scipy")

# import libraries
from math import log10, floor
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colours
import cmasher as cm
from astropy.io import ascii, fits
from astropy.table import Table, join
from scipy.odr import *

# import the csv file
# here we put the name of the file as a string
# the delimiter is what separate the different data
# skiprow tells the function how many rows to skip from the start of the file
# dtype sets the type of object being imported
harris_data = np.loadtxt('HarrisPartI.csv', delimiter= ',', skiprows=1, dtype=object)

# store each column as a new variable
Id_name = harris_data[:,0]
star_name = harris_data[:,1]
R_sun = harris_data[:,6].astype(float) 
R_gc = harris_data[:,7].astype(float)



cmap = colours.ListedColormap(['#ff6347', '#fe8951', '#ffa93e', '#ffc728', '#ffe410', '#90b2e8', '#778ce5', '#5d66df', '#403ed7', '#0000cd'])
cmap_2 = cm.tropical

plt.scatter(np.log(R_sun), np.log(R_gc), c=R_sun, marker='o', s=10, cmap=cmap_2)

# Since the HR diagram has inverted scales
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()

# Axes
plt.title('Hertzsprung-Russel Diagram') # Title of graph
plt.xlabel('$\ln R_{\odot}$, $R_{\odot}$') # x-axis label
plt.ylabel('$\ln R_{gc}$, $R_{gc}$') # y-axis label