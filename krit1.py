from __future__ import unicode_literals

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit
import math
import matplotlib as mpl
import pandas as pd

#plot package settings
mpl.use('GTK3Cairo')
plt.rc('text', usetex = True)
plt.rc('font', family ='serif')

#open ods file with data form columns E (lifting height of the core) as well as F (relative neutron count) 
df=pd.read_excel('Krit_Werte.ods', engine='odf', usecols="E:F", skiprows=0, nrows=17)

# dfe: values for inserted control rod from even row numbers
# dfa: values for not inserted one from even odd row numbers
dfe=df[df.index % 2 !=1]
dfa=df[df.index % 2 !=0]

# x- axis
xdata=np.linspace(0,600,3000)

#settings of the plot
fig= plt.figure()
ax = fig.add_subplot(111)
# x axis core lifting height
# y axis relative neutron count
ax.scatter(dfa['Hubhöhe'],dfa['N_0/N_i'], marker='.', color='blue',label=r'aus')
ax.scatter(dfe['Hubhöhe'],dfe['N_0/N_i'], marker='.', color='red',label=r'ein')
ax.scatter(504.0,0.0, marker='.', color='black', label=r'maximale Hubhöhe')

ax.plot(dfa['Hubhöhe'],dfa['N_0/N_i'], color='blue')
ax.plot(dfe['Hubhöhe'],dfe['N_0/N_i'], color='red')

ax.set_xlim(-10.0,610)
ax.set_ylim(-0.05,1.05)

ax.set_xlabel(r'Hubhöhe [digits]', fontsize=20)
ax.set_ylabel(r'$N_0/N_x$', fontsize=20)
ax.set_title('Kritisches Experiment, Weitbereich 1', fontsize=22, pad=30, x= 0.6)

    
ax.tick_params(axis = 'both', which = 'major', width = 1, length= 6, direction = 'in', labelsize =16, zorder = 5)
ax.tick_params(axis = 'both', which = 'minor', width = 1, length= 2, direction = 'in', labelsize =4, zorder = 5)
ax.tick_params(which = 'both', top = True, labeltop = False, right = True, labelright = False, zorder = 5)

ax.xaxis.set_major_locator(ticker.MultipleLocator(100))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
 
#ax.xaxis.set_major_locator(ticker.MultipleLocator(100.0))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
#ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))
   
ax.grid(True, which = 'major', linestyle='-', zorder= 2)
ax.grid(True, which = 'minor', linestyle=':', zorder= 2, alpha= 0.75)

ax.legend(fontsize = 16, loc='upper right')

plt.show()
