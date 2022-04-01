import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff

df=pd.read_csv("Data.csv")
h_list=df["Height(Inches)"].to_list()
w_list=df["Weight(Pounds)"].to_list()

fig = ff.create_distplot([df['Height(Inches)'].tolist()],['Height'],show_hist=True)

fig.show()

h_mean=statistics.mean(h_list)
h_mode=statistics.mode(h_list)
h_median=statistics.median(h_list)

w_mean=statistics.mean(w_list)
w_mode=statistics.mode(w_list)
w_median=statistics.median(w_list)

print("Mean, Median and Mode of height is {}, {} and {} respectively".format(h_mean, h_median, h_mode))
print("Mean, Median and Mode of Weight is {}, {} and {} respectively".format(w_mean, w_median, w_mode))

Hstd_deviation=statistics.stdev(h_list)
Wstd_deviation=statistics.stdev(w_list)

print("Hstd_deviation : "+str(Hstd_deviation))
print("Wstd_deviation : "+str(Wstd_deviation))

height_first_std_deviation_start, height_first_std_deviation_end = h_mean-Hstd_deviation, h_mean+Hstd_deviation 
height_second_std_deviation_start, height_second_std_deviation_end = h_mean-(2*Hstd_deviation), h_mean+(2*Hstd_deviation) 
height_third_std_deviation_start, height_third_std_deviation_end = h_mean-(3*Hstd_deviation), h_mean+(3*Hstd_deviation)

weight_first_std_deviation_start, weight_first_std_deviation_end = w_mean-Wstd_deviation, w_mean+Wstd_deviation 
weight_second_std_deviation_start, weight_second_std_deviation_end = w_mean-(2*Wstd_deviation), w_mean+(2*Wstd_deviation) 
weight_third_std_deviation_start, weight_third_std_deviation_end = w_mean-(3*Wstd_deviation), w_mean+(3*Wstd_deviation)

height_list_of_data_within_1_std_deviation = [result for result in h_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in h_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in h_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]

weight_list_of_data_within_1_std_deviation = [result for result in w_list if result > weight_first_std_deviation_start and result < weight_first_std_deviation_end]
weight_list_of_data_within_2_std_deviation = [result for result in w_list if result > weight_second_std_deviation_start and result <weight_second_std_deviation_end]
weight_list_of_data_within_3_std_deviation = [result for result in w_list if result > weight_third_std_deviation_start and result <weight_third_std_deviation_end]

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_std_deviation)*100.0/len(h_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2_std_deviation)*100.0/len(h_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(height_list_of_data_within_3_std_deviation)*100.0/len(h_list)))

print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_std_deviation)*100.0/len(w_list)))
print("{}% of data for weight lies within 2 standard deviation".format(len(weight_list_of_data_within_2_std_deviation)*100.0/len(w_list)))
print("{}% of data for weight lies within 3 standard deviation".format(len(weight_list_of_data_within_3_std_deviation)*100.0/len(w_list)))

fig.show()