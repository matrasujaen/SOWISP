# -*- coding: utf-8 -*-
'''
Created on 01 07 2022

@author: MATRAS research group.
    Department of Physics of the University of Jaen.
'''
import pandas as _pd
import numpy as _np

def read_database(file_path):
    '''
    Basic function for read the Database of Power Installed.

    Parameters
    ----------
    file_path   : str

    Returns
    -------
    pandas.DataFrame
        A DataFrame with the information of the file
    '''
    return _pd.read_csv(file_path, sep=';')


def group_data(df, aggregator = None):
    '''
    This function aggregates the installed power for each month of each year.
    You can aggregate, from smallest to largest spatial size, provincial,
    autonomous community and national level (default value).

    Mean for latitude, longitude and sum for the installed power columns
    is calculated.

    Parameters
    ----------
    df          : pandas.DataFrame,
                    Contain the entire installed power database for PV or Wind.

    aggregator  : str or None, default None
                    If None the national (highest spatial aggregation) average
                    for Spain for latitude and longitude is returned and the sum
                    for all power installed columns.
                    If 'NUTS_3', group by provincies (smallest spatial
                    aggregation) is returned, mean for (lat,lon) and sum for the
                    installed power columns.
                    If 'NUTS_2', group by autonomous community (intermediate spatial
                    aggregation) is returned.

    Returns
    -------
    pandas.DataFrame, when aggregator is None only one row is returned
                        corresponding to national aggregation for Spain.


    Examples
    --------
    National aggregation.
    >>>df = read_database(file_path)
    >>>group_data(df)

        Latitude  Longitude  ...  InsPowMW_20201130  InsPowMW_20201231
    0  41.193553  -3.574571  ...          26015.072          26243.937

    [1 rows x 75 columns]


    Province aggregation.
    >>>df = read_database(file_path)
    >>>group_data(df, aggregator='NUTS_3')

             NUTS_3   Latitude  ...  InsPowMW_20201130 InsPowMW_20201231
    0       ACoruna  43.165758  ...          37.318121         37.318121
    1      Albacete  38.895333  ...          67.641567         67.641567
    2       Almeria  37.193000  ...          47.076100         47.076100
    3         Araba  42.768000  ...          21.871000         21.871000
    ..        ...       ...     ...            ...                ...
    38     Valencia  39.403333  ...          72.470000         72.470000
    39   Valladolid  41.646667  ...         109.885833        109.885833
    40       Zamora  41.763636  ...          52.170909         52.170909
    41     Zaragoza  41.685897  ...          73.491923         78.078333

    [42 rows x 77 columns]

    '''

    if aggregator == 'NUTS_3':
        aggregations = {
            'Latitude':'mean', 'Longitude':'mean', 'NUTS_2':'first'
            }
    else:
        aggregations = {
            'Latitude':'mean', 'Longitude':'mean'
            }

    if aggregator is not None:
        df_latlon = df.groupby(aggregator).agg(aggregations)
        df_pot   = df.drop(['Latitude', 'Longitude'], axis=1).groupby(aggregator).mean()
        df_groupby =  _pd.concat([df_latlon, df_pot], axis=1)
        df_groupby.reset_index(inplace=True)
    else:
        serie = _pd.concat([df[df.columns[1:3]].mean(),df[df.columns[5:]].sum()])
        df_groupby   = _pd.DataFrame(serie).transpose()
    return df_groupby.copy()

def _idx_from_date(df, date_stop, mask_columns_pot):
    '''
    <no docstring>
    '''
    i=0
    date=0
    while date != date_stop:
        date = df.columns[mask_columns_pot][i].split('_')[1]
        i+=1
    return i-1

def select_date_range(df, date_beg, date_end):
    '''
    Work In Progress ...

    Parameters
    ----------
    df          : pandas.DataFrame,
                    Contain the entire installed power database for PV or Wind.

    date_beg    : str,
                    Format must be 'YYYYmmdd'.

    date_end    : str,
                    Format must be 'YYYYmmdd'.

    Returns
    -------
    pandas.DataFrame, slicing of the original returning the columns
                            corresponding to the date range entered.


    Examples
    --------
    Select a single date from original dataframe.
    >>>date_beg = '20171231'
    >>>date_end = '20171231'
    >>>select_date_range(df, date_beg, date_end)

             Town  Latitude  Longitude         NUTS_2    NUTS_3  InsPowMW_20171231
    0      Abadín     43.37      -7.49        Galicia      Lugo            208.860
    1        Abla     37.16      -2.77      Andalucia   Almeria             38.000
    2     Ablitas     41.96      -1.59        Navarra   Navarra              0.000
    3    Abrucena     37.13      -2.83      Andalucia   Almeria             12.000
    4     Adradas     41.35      -2.49  CastillaYLeon     Soria            121.450
    ..        ...       ...        ...            ...       ...                ...
    496  Zaragoza     41.68      -0.93         Aragon  Zaragoza            137.800
    497       Zas     43.09      -8.93        Galicia   ACoruna              0.000
    498    Zestoa     43.24      -2.24      PaisVasco  Gipuzkoa              0.004
    499  Zierbena     43.35      -3.09      PaisVasco   Bizkaia             10.000
    500     Zújar     37.57      -2.85      Andalucia   Granada             34.000

    [501 rows x 6 columns]



    Select a year from original dataframe.
    >>>date_beg = '20170131'
    >>>date_end = '20171231'
    >>>select_date_range(df, date_beg, date_end)

             Town  Latitude  ...  InsPowMW_20171130 InsPowMW_20171231
    0      Abadín     43.37  ...            208.860           208.860
    1        Abla     37.16  ...             38.000            38.000
    2     Ablitas     41.96  ...              0.000             0.000
    3    Abrucena     37.13  ...             12.000            12.000
    4     Adradas     41.35  ...            121.450           121.450
    ..        ...       ...  ...                ...               ...
    496  Zaragoza     41.68  ...            119.800           137.800
    497       Zas     43.09  ...              0.000             0.000
    498    Zestoa     43.24  ...              0.004             0.004
    499  Zierbena     43.35  ...             10.000            10.000
    500     Zújar     37.57  ...             34.000            34.000

    [501 rows x 17 columns]
    '''
    mask_potins = _np.array([df.columns[i][:8]=='InsPowMW' for i in range(len(df.columns))])
    idx_beg = _idx_from_date(df, date_beg, mask_potins)
    idx_end = _idx_from_date(df, date_end, mask_potins)
    if date_beg == date_beg:
        idx_end+=1
    cols = df.columns[_np.r_[0:len(df.columns[mask_potins==False]),idx_beg+len(df.columns[mask_potins==False]):idx_end+len(df.columns[mask_potins==False])]]
    return df[cols].copy()
