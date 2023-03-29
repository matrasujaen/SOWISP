# -*- coding: utf-8 -*-
'''
Created on July 2022

@author: MATRAS research group.
    Department of Physics of the University of Jaen.
'''
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime

import sowisp_lib


df_NUTS2 = sowisp_lib.group_data(df, aggregator='NUTS_2')
mask_inspow = np.array([df_NUTS2.columns[i][:8]=='InsPowMW'
                    for i in range(len(df_NUTS2.columns))])
inspow_cols = df_NUTS2.columns[mask_inspow]


# You can repite this time serie representation adding as many NUTS-2 as you want
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
