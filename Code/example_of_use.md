# Example of use

## Installed Power (scaled sizes) Scatter Plot for Iberian Peninsula.
The following is an example of the wind database representation of the installed power for each Town.

![Town Scatter Plot Iberian Peninsula](https://github.com/matrasujaen/SOWISP/blob/main/Code/imgs/town_scatterplot.png)


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

## Some NUTS-2 time serie representation 
We have chosen several NUTS2 for the representation of the temporal evolution of the installed power. You can choose as many NUTS2 as you want.

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
