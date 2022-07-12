# Example of use
NOTE: Additional Python libraries are required.

## Installed Power (scaled sizes) Scatter Plot for Iberian Peninsula.
The following is an example of the wind database representation of the installed power for each Town.

[Town Scatter Plot Iberian Peninsula](https://github.com/matrasujaen/SOWISP/blob/main/Code/town_scatterplot_iberianpeninsula.py)

![Town Scatter Plot Iberian Peninsula](https://github.com/matrasujaen/SOWISP/blob/main/Code/imgs/town_scatterplot_ip.png)


```python

import pandas as pd
from matplotlib import pyplot as plt
import cartopy.crs as ccrs
import cartopy
import sowisp_lib

file_path = .../Data/SOWISP_Wind.csv
df = sowisp_lib.read_database(file_path)


date_beg = '20191231'
date_end = '20191231'
df_date_crop = sowisp_lib.select_date_range(df, date_beg, date_end)
InsPow_MW   = df_date_crop['InsPowMW_'+date_beg].values


fig = plt.figure(0, figsize = ((14.0 / 2.54), (8.0/ 2.54)))
ax = plt.axes(projection=cartopy.crs.PlateCarree())
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
```


## Installed Power for NUTS-3 aggregations.
In this examples we show how to select a specific date, aggregations to NUTS-3 and plot a political map with a colorbar.

Import the required python libraries.

```python
import numpy as np
import pandas as pd
import geopandas as gpd
import cartopy.crs as ccrs
import cartopy.feature as cf
import matplotlib as mpl
from datetime import datetime
from matplotlib import pyplot as plt
import sowisp_lib
```
Define the path's and dictionaries 

```python
file_path = '.../Data/'
shapefile = '.../shapefiles/recintos_provinciales_inspire_peninbal_etrs89.shp'
dict_colors = {'PV': 'Reds', 'Wind': 'PuBu'}
dict_replace_NUTS3 = {'Castellon': 'Castello/Castellon', 'Alicante': 'Alacant/Alicante', 'Araba': 'Araba/Alava', 'Valencia': 'València/Valencia'}
date_map = '20201231'


geoDf = gpd.read_file(shapefile)
# Modify if change DataBase names.
arrayProvIGN = np.array(
    [nombre.replace('Á', 'A').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ñ', 'n').replace(' ', '') for nombre in geoDf['NAMEUNIT'].values]
)

Tech = 'Wind'  #Select 'PV' or 'Wind'
```

Read the corresponding database, select a date for plot a map and group by NUTS-3.
```python
dfSOWISP = sowisp_lib.read_database(file_path+'SOWISP_'+Tech+'.csv')
dfSOWISP = sowisp_lib.select_date_range(dfSOWISP, date_map, date_map)
dfSOWISP = sowisp_lib.group_data(dfSOWISP, aggregator='NUTS_3')
```



Initialize Iberian Peninsula Map.
```python
fig = plt.figure(0, (19.0 / 2.54, 7.5 / 2.54), dpi = 600, clear = True)
ax = {}
dx = 0.0 #Change to dx = 0.5 when change technology
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
```

Add geometries from shapefiles for each NUTS-3 to the map.
```python
# add geometries for each NUTS-3
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
```

Repeat the above for both technologies (PV and Wind) and save the figure. 
```python

fig.savefig('.../OUTFP/NUTS3_map.jpg', dpi = 600)
plt.close(0)
```

[Installed power for Iberian Peninsula, NUTS-3 aggregations](https://github.com/matrasujaen/SOWISP/blob/main/Code/NUTS_3_aggregations_map.py)

![Installed power for Iberian Peninsula, NUTS-3 aggregations](https://github.com/matrasujaen/SOWISP/blob/main/Code/imgs/NUTS3_map.jpg)


## NUTS-2 time serie representation 
We have chosen several NUTS2 for the representation of the temporal evolution of the installed power. You can choose as many NUTS2 as you want.

[NUTS-2 time serie representation](https://github.com/matrasujaen/SOWISP/blob/main/Code/NUTS_2_timeserie.py)



![NUTS-2 time serie representation](https://github.com/matrasujaen/SOWISP/blob/main/Code/imgs/NUTS2_timeserie.png)




```python
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
import sowisp_lib

df_NUTS2 = sowisp_lib.group_data(df, aggregator='NUTS_2')
mask_inspow = np.array([df_NUTS2.columns[i][:8]=='InsPowMW'
                    for i in range(len(df_NUTS2.columns))])
inspow_cols = df_NUTS2.columns[mask_inspow]

mask_NUTS2 = (df_NUTS2['NUTS_2']==df_NUTS2['NUTS_2'].values[0])|(df_NUTS2['NUTS_2']==df_NUTS2['NUTS_2'].values[5])|(df_NUTS2['NUTS_2']==df_NUTS2['NUTS_2'].values[9])|(df_NUTS2['NUTS_2']==df_NUTS2['NUTS_2'].values[7])
df_inspow_to_plot = df_NUTS2[inspow_cols][mask_NUTS2].transpose()
df_inspow_to_plot.index = [datetime.strptime(date, 'InsPowMW_%Y%m%d') for date in df_inspow_to_plot.index]

plt.title('NUTS-2 time serie representation')
plt.xlabel('Year (YYYY)')
plt.ylabel('Ins. Pow. [MW]')
plt.ylim(19.5, 75.5)
plt.tick_params(direction = 'in', which = 'both')
[plt.grid(axis = axis, which = 'both', ls = ':', color = '0.4', lw = 0.5) for axis in ('x', 'y')]
plt.plot_date(df_inspow_to_plot.index, df_inspow_to_plot[df_inspow_to_plot.columns[0]].values, '--', label=df_NUTS2['NUTS_2'].values[0])
plt.plot_date(df_inspow_to_plot.index, df_inspow_to_plot[df_inspow_to_plot.columns[1]].values, '--', label=df_NUTS2['NUTS_2'].values[5])
plt.plot_date(df_inspow_to_plot.index, df_inspow_to_plot[df_inspow_to_plot.columns[2]].values, '--', label=df_NUTS2['NUTS_2'].values[9])
plt.plot_date(df_inspow_to_plot.index, df_inspow_to_plot[df_inspow_to_plot.columns[3]].values, '--', label=df_NUTS2['NUTS_2'].values[7])
plt.legend(loc = 'lower right')
plt.show()
```

## DataFrame as LateX table for a specific dates
You can build a table in LateX format with one or several dates, for any of the spatial aggregations. In the following example a few months are shown for NUTS-2 aggregations.

```python
\begin{tabular}{lrrrrr}
\toprule
          NUTS\_2 &  Latitude &  Longitude &  InsPowMW\_20180131 &  InsPowMW\_20180228 &  InsPowMW\_20180331 \\
\midrule
       Andalucia & 37.013878 &  -4.612041 &          66.320020 &          66.320020 &          66.320020 \\
          Aragon & 41.518475 &  -1.012712 &          31.007458 &          31.007458 &          31.007458 \\
        Asturias & 43.370000 &  -6.670833 &          43.204167 &          43.204167 &          43.204167 \\
     CValenciana & 39.854706 &  -0.709412 &          69.955294 &          69.955294 &          69.955294 \\
       Cantabria & 43.260000 &  -3.897500 &           8.827000 &           8.827000 &           8.827000 \\
CastillaLaMancha & 39.616667 &  -2.236944 &          53.035194 &          53.035194 &          53.179222 \\
   CastillaYLeon & 41.945736 &  -4.165736 &          42.733194 &          42.733194 &          42.733194 \\
        Cataluna & 41.283333 &   0.868889 &          48.691111 &          48.691111 &          48.691111 \\
     Extremadura & 40.010000 &  -6.140000 &           0.000000 &           0.000000 &           0.000000 \\
         Galicia & 42.985733 &  -8.137467 &          42.121200 &          43.027867 &          43.027867 \\
         LaRioja & 42.177143 &  -2.130000 &          64.017143 &          64.017143 &          64.017143 \\
          Murcia & 37.982000 &  -1.152000 &          44.872000 &          44.872000 &          44.872000 \\
         Navarra & 42.470323 &  -1.681290 &          28.271839 &          28.271839 &          28.271839 \\
       PaisVasco & 43.074615 &  -2.553846 &          11.798462 &          11.798462 &          11.798462 \\
\bottomrule
\end{tabular}
```

You can save a LateX table file or show by terminal. 

[NUTS-2 LateX Table](https://github.com/matrasujaen/SOWISP/blob/main/Code/NUTS_2_LateXTable.py)

```python
import pandas as pd
import sowisp_lib


out_LateX_fp = '.../OUTFP/LateXTable.tex'

date_beg = '20180131'
date_end = '20180331'
df_date_crop = sowisp_lib.select_date_range(df, date_beg, date_end)
df_date_crop_NUTS2 = sowisp_lib.group_data(df_date_crop, aggregator='NUTS_2')

# Save a LateX file
df_date_crop_NUTS2.to_latex(out_LateX_fp, index=False)
# Print on terminal like LateX Table format
print(df_date_crop_NUTS2.to_latex(index=False))
```



