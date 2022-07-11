# SOWISP

Solar and Wind Spain Power


## Data
In Data folder we can find the SOWISP database. The SOWISP database consists of two CSV files, one for the installed capacity corresponding to wind and the other for PV.

Wind CSV:

```python
         Town  Latitude  ...  InsPowMW_20201130 InsPowMW_20201231
0      Abadín     43.37  ...            243.510           243.510
1        Abla     37.16  ...             38.000            38.000
2     Ablitas     41.96  ...             41.580            41.580
3    Abrucena     37.13  ...             12.000            12.000
4     Adradas     41.35  ...            121.450           121.450
..        ...       ...  ...                ...               ...
496  Zaragoza     41.68  ...            254.600           254.600
497       Zas     43.09  ...             24.000            24.000
498    Zestoa     43.24  ...              0.004             0.004
499  Zierbena     43.35  ...             10.000            10.000
500     Zújar     37.57  ...             34.000            34.000

[501 rows x 78 columns]

```

PV CSV:

```python
Work In Progres...

```



## Using data with sowisp_lib
### Requirements

- Python  3.8.10
- Numpy   1.21.2
- Pandas  1.3.3


### Example of use
You can see some examples for the use of SOWISP library in ./example_of_use/ folder. The examples show how to draw a map of installed power by towns and by NUTS_3 for the Iberian Peninsula. Also how to draw a time series of the data for NUTS_2 and how to obtain a table in LateX format of the installed power for each NUTS_2, both in .tex file and by terminal.


[Example of use](https://github.com/matrasujaen/SOWISP/blob/main/Code/example_of_use.md)
