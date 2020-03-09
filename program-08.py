#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 17:08:57 2020

@author: aetienne
"""
import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
import matplotlib.pyplot as plt

#read in the Wabash River daily discharge text file 
#Use Columns 3 and 4 for a single Datetime element
#Use Column 6 (discharge in cubic feet per second) for the value
wabash_data= pd.read_table('WabashRiver_DailyDischarge_20150317-20160324.txt',
 skiprows=[0,23,25], header=[24], parse_dates=[[2,3]])

#Create daily average streamflow in a time series fashion 
dailysf = pd.date_range('2015-03-17 00:00:00', periods= wabash_data.shape[0],
                       freq='15min')
dailysf.shape
avgsf = Series(wabash_data['23100'].values, index= dailysf)

#rutilize the resampling method to get mean daily streamflow 
avgsf_d = avgsf.resample("D").mean()

#create a plot of mean daily streamflow 
ax= avgsf_d.plot(style='g')
ax.set_xlabel('Time')
ax.set_ylabel('Daily Average Streamflow Rate (ft^3/s)')
plt.savefig('avg_daily_streamflow.pdf') 
plt.show()

#pick out top ten days with highest daily average stream flow in dataset
avgsf_d.sort_values(ascending=False)

#plot top ten days with highest stream discharge rate 
ax=avgsf_d[0:9].plot(style='r^')
ax.set_xlabel('Time')
ax.set_ylabel('Top Ten Daily Average Streamflow Rates (ft^3/s)')
plt.savefig('avg_streamflow_tten.pdf')
plt.show()

#again utilize the resampling method to get monthly average streamflow
avgsf_month = avgsf.resample("M").mean()

#plot the average monthly streamflow
ax= avgsf_month.plot()
ax.set_xlabel('Time')
ax.set_ylabel('Monthly Average Streamflow Rate (ft^3/s)')
plt.savefig('avg_monthly_streamflow.pdf') 
plt.show()