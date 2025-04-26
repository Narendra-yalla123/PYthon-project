Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\saich\AppData\Local\Programs\Python\Python313\project 7.py =
=== Dataset Information ===
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1000 entries, 0 to 999
Data columns (total 15 columns): 
 #   Column                       Non-Null Count  Dtype  
---  ------                       --------------  -----  
 0   Citizen_ID                   1000 non-null   int64  
 1   Age                          1000 non-null   int64  
 2   Gender                       1000 non-null   object 
 3   Mode_of_Transport            1000 non-null   object 
 4   Work_Hours                   1000 non-null   int64  
 5   Shopping_Hours               1000 non-null   int64  
 6   Entertainment_Hours          1000 non-null   int64  
 7   Home_Energy_Consumption_kWh  1000 non-null   float64
 8   Charging_Station_Usage       1000 non-null   int64  
 9   Carbon_Footprint_kgCO2       1000 non-null   float64
 10  Steps_Walked                 1000 non-null   int64  
 11  Calories_Burned              1000 non-null   int64  
 12  Sleep_Hours                  1000 non-null   float64
 13  Social_Media_Hours           1000 non-null   float64
 14  Public_Events_Hours          1000 non-null   float64
dtypes: float64(5), int64(8), object(2)
memory usage: 117.3+ KB
None


=== First 5 Rows of the Dataset ===
   Citizen_ID  Age  ... Social_Media_Hours Public_Events_Hours
0        1001   56  ...                5.8                 0.5
1        1002   69  ...                5.5                 1.9
2        1003   46  ...                3.8                 2.8
3        1004   32  ...                3.5                 0.5
4        1005   60  ...                2.2                 0.5

[5 rows x 15 columns]


=== Descriptive Statistics for Numerical Columns ===
        Citizen_ID         Age  ...  Social_Media_Hours  Public_Events_Hours
count  1000.000000  1000.00000  ...         1000.000000          1000.000000
mean   1500.500000    43.81900  ...            3.007500             1.503600
std     288.819436    14.99103  ...            1.706249             0.874226
min    1001.000000    18.00000  ...            0.000000             0.000000
25%    1250.750000    31.00000  ...            1.600000             0.800000
50%    1500.500000    44.00000  ...            3.000000             1.500000
75%    1750.250000    56.00000  ...            4.400000             2.300000
max    2000.000000    69.00000  ...            6.000000             3.000000

[8 rows x 13 columns]


=== Missing Values in Each Column ===
Citizen_ID                     0
Age                            0
Gender                         0
Mode_of_Transport              0
Work_Hours                     0
Shopping_Hours                 0
Entertainment_Hours            0
Home_Energy_Consumption_kWh    0
Charging_Station_Usage         0
Carbon_Footprint_kgCO2         0
Steps_Walked                   0
Calories_Burned                0
Sleep_Hours                    0
Social_Media_Hours             0
Public_Events_Hours            0
dtype: int64


=== Gender Distribution ===
Gender
Female    484
Male      475
Other      41
Name: count, dtype: int64


=== Transport Mode Distribution ===
Mode_of_Transport
Walking             190
Bike                176
Car                 167
EV                  162
Bicycle             154
Public Transport    151
Name: count, dtype: int64


=== Carbon Footprint Summary ===
Average: 54.42 kgCO2
Minimum: 10.02 kgCO2
Maximum: 99.93 kgCO2


=== Comparison: EV vs Non-EV Users ===
Average Carbon Footprint (EV Users): 53.58 kgCO2
Average Carbon Footprint (Non-EV Users): 54.58 kgCO2


✅ Data analysis completed. Cleaned data saved to 'cleaned_citizen_activity.csv'
