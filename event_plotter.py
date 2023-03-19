#make sure mpl_toolskits.basemap is installed
#Additional lines of code to fix errors of basemap on python 3.7 
#<<<<<<<<<<<<<<<<<<<< mpl_toolkits.basemap bug fixing >>>>>>>>>>>>>>>>
import os
import conda

conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"] = proj_lib

#<<<<<<<<<<<<<<<<<<<<< mpl_toolkits.basemap bug solved >>>>>>>>>>>>>>>>>>>>
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import os

cwd=os.getcwd()

cwd=os.getcwd()

#Reading events Catalogue
events=pd.read_csv(cwd+'\\events.csv')
plt.figure(figsize=(12,8))
plt.tight_layout()
m=Basemap(projection='merc',
          llcrnrlat=23,
          llcrnrlon=76,
          urcrnrlat=35,
          urcrnrlon=97,
          resolution='i')
lon_d,lat_d=m(events.longitude,events.latitude)


m.drawcountries(linewidth=1,color='r')
#m.drawstates(color='b')
m.drawrivers(color='aqua')
m.drawparallels(range(-90, 100, 2), color='k', linewidth=0.35, dashes=[4, 4], labels=[1, 0, 0, 0])
m.drawmeridians(range(0, 360, 2), color='k', linewidth=0.35, dashes=[4, 4], labels=[0, 0, 0, 1])
#m.drawcoastlines()
#********************
#Map Display options (activate one)
#********************

m.fillcontinents(color='grey', lake_color='aqua', ax=None, zorder=None, alpha=0.3)
#m.shadedrelief()
#m.bluemarble()
#m.etopo()
mL4=0
mG4L5=0
mG5L6=0
mG6L7=0
mG7=0

N=len(lat_d)
for i in range(N):
    if events.mag[i]<=4:
        mL4=mL4+1
        if mL4==1:
            plt.scatter(lon_d[i],lat_d[i],color='m',s=5,alpha=0.85,label='Mw<=4')
        else:
            plt.scatter(lon_d[i],lat_d[i],color='m',s=5,alpha=0.85)
    elif events.mag[i]>4 and events.mag[i]<=5:
        mG4L5=mG4L5+1
        if mG4L5==1:
            plt.scatter(lon_d[i],lat_d[i],color='g',s=25,alpha=0.5,label='4<Mw<=5')
        else:
            plt.scatter(lon_d[i],lat_d[i],color='g',s=25,alpha=0.5)
    elif events.mag[i]>5 and events.mag[i]<=6:
        mG5L6=mG5L6+1
        if mG5L6==1:
            plt.scatter(lon_d[i],lat_d[i],color='b',s=40,alpha=0.5,label='5<Mw<=6')
        else:
            plt.scatter(lon_d[i],lat_d[i],color='b',s=40,alpha=0.5)
    elif events.mag[i]>6 and events.mag[i]<=7:
        mG6L7=mG6L7+1
        if mG6L7==1:
            plt.scatter(lon_d[i],lat_d[i],color='r',s=140,alpha=0.65,label='6<Mw<=7')
        else:
            plt.scatter(lon_d[i],lat_d[i],color='r',s=140,alpha=0.65)
    elif events.mag[i]>7:
        mG7=mG7+1
        if mG7==1:
            plt.scatter(lon_d[i],lat_d[i],color='k',s=200,alpha=0.75,label='Mw>7')
        else:
            plt.scatter(lon_d[i],lat_d[i],color='k',s=200,alpha=0.75)
    else:
        pass
    plt.tight_layout()
    plt.title("Event Date: "+str(events.yyyy[i])+"-"+str(events.mm[i])+"-"+str(events.dd[i])+'( Event Time: '+str(events.time[i])+')',loc='right')
    plt.legend(loc='lower left')
    plt.pause(0.05)
    plt.show() 

    
