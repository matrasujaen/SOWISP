# -*- coding: utf-8 -*-
'''
Created on 01 07 2022

@author: MATRAS research group.
    Department of Physics of the University of Jaen.
'''
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
