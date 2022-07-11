# -*- coding: utf-8 -*-
'''
Created on 11 07 2022

@author: MATRAS research group.
    Department of Physics of the University of Jaen.
'''
import sowisp_lib
from matplotlib import pyplot as plt
import cartopy



file_path = '.../Data/SOWISP_Wind.csv'

df = sowisp_lib.read_database(file_path)


date_beg = '20191231'
date_end = '20191231'
df_date_crop = sowisp_lib.select_date_range(df, date_beg, date_end)
InsPow_MW   = df_date_crop['InsPowMW_'+date_beg].values

# Figure width=14cm, height=8 cm. Note that cmPerInch = 2.54
fig = plt.figure(0, figsize = ((14.0 / 2.54), (8.0/ 2.54)))
# PlateCarree projection also called equirectangular projection.
ax = plt.axes(projection=cartopy.crs.PlateCarree())
# The extent (x0, x1, y0, y1) of the map in the given coordinate system.
ax.set_extent([-11, 4.5, 35, 45])
ax.coastlines(resolution='50m')
ax.stock_img()
ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.75)
plt.scatter(x= df_date_crop['Longitude'].copy(),y= df_date_crop['Latitude'].copy(),
        color='dodgerblue',
        edgecolor='black',
        s=(InsPow_MW),
        alpha=0.8,
        zorder=1,
        transform=cartopy.crs.PlateCarree())
plt.show()
