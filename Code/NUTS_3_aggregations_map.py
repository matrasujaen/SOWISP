# -*- coding: utf-8 -*-
'''
Created on July 2022

@author: MATRAS research group.
    Department of Physics of the University of Jaen.
'''
import numpy as np
import pandas as pd
import geopandas as gpd
import cartopy.crs as ccrs
import cartopy.feature as cf
import matplotlib as mpl
from datetime import datetime
from matplotlib import pyplot as plt
import sowisp_lib


file_path = '.../Data/'
shapefile = '.../shapefile/recintos_provinciales_inspire_peninbal_etrs89.shp'
dict_colors = {'PV': 'Reds', 'Wind': 'PuBu'}
dict_replace_NUTS3 = {'Castellon': 'Castello/Castellon', 'Alicante': 'Alacant/Alicante', 'Araba': 'Araba/Alava', 'Valencia': 'València/Valencia'}
date_map = '20201231' # format %Y%m%d

geoDf = gpd.read_file(shapefile)
arrayProvIGN = np.array(
    [nombre.replace('Á', 'A').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ñ', 'n').replace(' ', '') for nombre in geoDf['NAMEUNIT'].values]
)

fig = plt.figure(0, (19.0 / 2.54, 7.5 / 2.54), dpi = 600, clear = True)
ax = {}
dx = 0.0
for Tech in ['PV','Wind']:
    dfSOWISP = sowisp_lib.read_database(file_path+'SOWISP_'+Tech+'.csv')
    dfSOWISP = sowisp_lib.select_date_range(dfSOWISP, date_map, date_map)
    dfSOWISP = sowisp_lib.group_data(dfSOWISP, aggregator='NUTS_3')

    ax[f'Map_{Tech}'] = fig.add_axes([0.02 + dx, 0.1, 0.46, 0.95], projection = ccrs.PlateCarree())
    ax[f'Map_{Tech}'].set_extent([-11.0, 4.5, 35.0, 45.0], ccrs.PlateCarree())
    cmap = plt.get_cmap(dict_colors[Tech])

    ax[f'Map_{Tech}'].stock_img()
    ax[f'Map_{Tech}'].coastlines(resolution = '50m')
    ax[f'Map_{Tech}'].add_feature(cf.BORDERS)

    ax[f'Cbar_{Tech}'] = fig.add_axes([0.02 + dx, 0.15, 0.46, 0.02])
    cbar = mpl.colorbar.ColorbarBase(
        ax[f'Cbar_{Tech}'],
        cmap = cmap,
        norm = mpl.colors.Normalize(vmin = 0.0, vmax = dfSOWISP['InsPowMW_'+date_map].max()),
        orientation = 'horizontal'
    )
    cbar.set_label(f'{Tech} Installed Capacity [MW]', fontsize = 10, family = 'Liberation Sans')
    cbar.ax.tick_params(labelsize = 8)

    for idx in dfSOWISP.index.values:
        if np.isin(np.array(dfSOWISP.loc[idx]['NUTS_3'], dtype = 'U11'), np.array(tuple(dict_replace_NUTS3.keys()), dtype = 'U11')).item() == True:
            NUTS3IGN = dict_replace_NUTS3[dfSOWISP.loc[idx]['NUTS_3']]
        else:
            NUTS3IGN = dfSOWISP.loc[idx]['NUTS_3']
        ax[f'Map_{Tech}'].add_geometries(
            geoms = geoDf[arrayProvIGN == NUTS3IGN]['geometry'].values,
            crs = ccrs.PlateCarree(),
            facecolor = cmap(dfSOWISP.loc[idx]['InsPowMW_'+date_map] / dfSOWISP['InsPowMW_'+date_map].max()),
            edgecolor = 'black',
            linewidth = 0.5
        )
    if (Tech == 'Wind'):
        for NUTS3 in ('Badajoz', 'Córdoba', 'Alacant/Alicante', 'Madrid', 'Girona'):
            ax[f'Map_{Tech}'].add_geometries(
                geoms = geoDf[geoDf['NAMEUNIT'] == NUTS3]['geometry'].values,
                crs = ccrs.PlateCarree(),
                facecolor = cmap(0.0),
                edgecolor = 'black',
                linewidth = 0.5
            )
    dx = 0.5
fig.savefig('.../OUTFP/NUTS3_map.jpg', dpi = 600)
plt.close(0)
