# SOWISP

**SO**lar and **WI**nd **S**panish **P**ower.

SOWISP is a database containing information associated with PV and Wind installed power. In this database, the geographic information and the installed power in that location appears on a monthly basis.


## Data
In "*Data*" folder we can find the SOWISP database. The SOWISP database consists of two CSV files, one for the installed capacity corresponding to PV and the other for Wind. 


PV CSV:

```python
              Town   Area  Latitude  Longitude NUTS2  NUTS3   InsPowMW_20150131   ...     InsPowMW_20201231
0           Abadín  196.0     43.37      -7.49  ES11  ES112               0.043   ...                 0.043
1          Abadiño   36.0     43.13      -2.62  ES21  ES213               0.095   ...                 0.095
2     Abaltzisketa   11.2     43.04      -2.11  ES21  ES212               0.008   ...                 0.008
3         Abánades   36.1     40.89      -2.47  ES42  ES424               1.334   ...                 1.334
...            ...    ...       ...        ...   ...    ...                 ...   ...                   ...
3895         Zújar  102.1     37.57      -2.85  ES61  ES614               0.480   ...                 0.480
3896        Zumaia   11.4     43.29      -2.24  ES21  ES212               0.130   ...                 0.130
3897     Zumarraga   18.4     43.10      -2.31  ES21  ES212               0.145   ...                 0.145
3898       Zurgena   71.7     37.36      -2.03  ES61  ES611               0.216   ...                 0.291

[3899 rows x 78 columns]

```



Wind CSV:

```python
              Town   Area  Latitude  Longitude NUTS2  NUTS3   InsPowMW_20150131   ...     InsPowMW_20201231 
0           Abadín  196.0     43.37      -7.49  ES11  ES112             208.860   ...               243.510
1             Abla   45.2     37.16      -2.77  ES61  ES611              38.000   ...                38.000
2          Ablitas   77.5     41.96      -1.59  ES22  ES220               0.000   ...                41.580
3         Abrucena   83.7     37.13      -2.83  ES61  ES611              12.000   ...                12.000
...            ...    ...       ...        ...   ...    ...                 ...   ...                   ...
499            Zas  133.1     43.09      -8.93  ES11  ES111               0.000   ...                24.000
500         Zestoa   43.7     43.24      -2.24  ES21  ES212               0.004   ...                 0.004
501       Zierbena   12.2     43.35      -3.09  ES21  ES213              10.000   ...                10.000
502          Zújar  102.1     37.57      -2.85  ES61  ES614              34.000   ...                34.000

[503 rows x 78 columns]

```


## Code
### Requirements

- Python  3.8.10
- Numpy   1.21.2
- Pandas  1.3.3


### Example of use
You can see some examples for the use of SOWISP library in ./example_of_use/ folder. The examples show how to draw a map of installed power by towns and by NUTS_3 for the Iberian Peninsula. Also how to draw a time series of the data for NUTS_2 and how to obtain a table in LateX format of the installed power for each NUTS_2, both in .tex file and by terminal.


[Example of use](https://github.com/matrasujaen/SOWISP/blob/main/Code/README.md)
