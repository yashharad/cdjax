from turtle import pd


import pandas as pd
import statistics
import csv
df=pd.read_csv("height-weight.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)

height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

print(height_mean)
print(weight_mean)

print(height_median)
print(weight_median)

print(height_mode)
print(weight_mode)

height_std_daviasion=statistics.stdev(height_list)
weight_std_daviasion=statistics.stdev(weight_list)

print(height_std_daviasion)
print(weight_std_daviasion)