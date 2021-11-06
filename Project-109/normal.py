from os import name
from re import X
import statistics
import random
import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go


df=pd.read_csv('StudentsPerformance.csv')
listeddata=df['reading score'].tolist()
mean=statistics.mean(listeddata)
mode=statistics.mode(listeddata)
median=statistics.median(listeddata)
std=statistics.stdev(listeddata)


first_stdev_start,first_stdev_end=mean-std,mean+std
second_stdev_start,second_stdev_end=mean-(2*std),mean+(2*std)
third_stdev_start,third_stdev_end=mean-(3*std),mean+(3*std)
figure=ff.create_distplot([listeddata],['reading score'],show_hist=False)
figure.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name='mean'))
figure.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.17],mode='lines',name='std1'))
figure.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.17],mode='lines',name='std1end'))

figure.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.17],mode='lines',name='std3'))
figure.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.17],mode='lines',name='std3end'))
figure.show()
list_of_data_within_1_std_deviation = [result for result in listeddata if result > first_stdev_start and result < first_stdev_end]
list_of_data_within_2_std_deviation = [result for result in listeddata if result > second_stdev_start and result < second_stdev_end]
list_of_data_within_3_std_deviation = [result for result in listeddata if result > third_stdev_start and result < third_stdev_end]
print(f'mean is :',mean)
print(f'mode is :',mode)
print(f'median is :',median)
print(f'standard deviation is :',std)
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(listeddata)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(listeddata)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(listeddata)))

