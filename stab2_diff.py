from __future__ import unicode_literals

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit
import math
import matplotlib as mpl
import pandas as pd

#package setting plot
mpl.use('GTK3Cairo')
plt.rc('text', usetex = True)
plt.rc('font', family ='serif')

# define function for differential control rod characteristics
def difffunc(z,const,H):
	return const*0.5*(1-np.cos(2.0*np.pi*z/H))
# open ods file
df=pd.read_excel('Steuerstab.ods', engine='odf', usecols="E:F", skiprows=17, nrows=6)

# fit of the differential control rod characteristics
popt, pcov = curve_fit(difffunc,df.values[:,0],df.values[:,1], bounds=([0,100],[0.4,6000]))

#settings for the plot
xdata=np.linspace(0,math.ceil(popt[1]),6000)

fig= plt.figure()
ax = fig.add_subplot(111)
ax.scatter(df.values[:,0],df.values[:,1], marker='.', color='red',label=r'gemessenes $\frac{\mathrm{d}\rho^\ast}{\mathrm{d}z}$')
ax.plot(xdata,difffunc(xdata,*popt),color='black',label=r'Fit')

ax.set_xlim(-100.0,math.ceil(popt[1])+100)
ax.set_ylim(-0.01,0.13)

ax.set_xlabel(r'$z$', fontsize=20)
ax.set_ylabel(r'$\frac{\mathrm{d}\rho^\ast}{\mathrm{d}z}$', fontsize=20)
ax.set_title('Differentielle Steuerstabkennlinie für Stab 2', fontsize=22, pad=30, x= 0.6)
    
ax.tick_params(axis = 'both', which = 'major', width = 1, length= 6, direction = 'in', labelsize =16, zorder = 5)
ax.tick_params(axis = 'both', which = 'minor', width = 1, length= 2, direction = 'in', labelsize =4, zorder = 5)
ax.tick_params(which = 'both', top = True, labeltop = False, right = True, labelright = False, zorder = 5)

ax.xaxis.set_major_locator(ticker.AutoLocator())
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax.yaxis.set_major_locator(ticker.AutoLocator())
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator())
 
#ax.xaxis.set_major_locator(ticker.MultipleLocator(100.0))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
#ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
   
ax.grid(True, which = 'major', linestyle='-', zorder= 2)
ax.grid(True, which = 'minor', linestyle=':', zorder= 2, alpha= 0.75)

ax.legend(fontsize = 16, loc='upper right')

#plt.plot(z,diffreakt)
plt.show()
