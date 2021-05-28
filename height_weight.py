#import plotly.figure_factory as ff
import pandas as pd
import statistics
import csv

df = pd.read_csv("data.csv")
# fig = ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist = False)
# fig.show()
height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

height_standard_deviation = statistics.stdev(height_list)
weight_standard_deviation = statistics.stdev(weight_list)

print("Mean,median and mode of height is {},{} and {} respectively".format(height_mean,height_median,height_mode))
print("Mean,median and mode of weight is {},{} and {} respectively".format(weight_mean,weight_median,weight_mode))



height_first_standard_deviation_start,height_first_standard_deviation_end = height_mean - height_standard_deviation ,height_mean + height_standard_deviation 
height_second_standard_deviation_start,height_second_standard_deviation_end = height_mean - (2*height_standard_deviation) ,height_mean + (2*height_standard_deviation) 
height_third_standard_deviation_start,height_third_standard_deviation_end = height_mean - (3*height_standard_deviation) ,height_mean + (3*height_standard_deviation)

height_list_of_data_within_1_standard_deviation = [result for result in height_list if result>height_first_standard_deviation_start and result < height_first_standard_deviation_end]
height_list_of_data_within_2_standard_deviation = [result for result in height_list if result > height_second_standard_deviation_start and result < height_second_standard_deviation_end]
height_list_of_data_within_3_standard_deviation = [result for result in height_list if result>height_third_standard_deviation_start and result < height_third_standard_deviation_end]

print("{}% of data for height  lies within 1 standard deviation".format(len(height_list_of_data_within_1_standard_deviation)*100.0 / len(height_list)))
print("{}% of data for height  lies within 2 standard deviation".format(len(height_list_of_data_within_2_standard_deviation)*100.0 / len(height_list)))
print("{}% of data for height  lies within 3 standard deviation".format(len(height_list_of_data_within_3_standard_deviation)*100.0 / len(height_list)))
 
weight_first_standard_deviation_start,weight_first_standard_deviation_end = weight_mean - weight_standard_deviation ,weight_mean + weight_standard_deviation 
weight_second_standard_deviation_start,weight_second_standard_deviation_end = weight_mean - (2*weight_standard_deviation) ,weight_mean + (2*weight_standard_deviation) 
weight_third_standard_deviation_start,weight_third_standard_deviation_end = weight_mean - (3*weight_standard_deviation) ,weight_mean + (3*weight_standard_deviation)

weight_list_of_data_within_1_standard_deviation = [result for result in weight_list if result>weight_first_standard_deviation_start and result < weight_first_standard_deviation_end]
weight_list_of_data_within_2_standard_deviation = [result for result in weight_list if result>weight_second_standard_deviation_start and result < weight_second_standard_deviation_end]
weight_list_of_data_within_3_standard_deviation = [result for result in weight_list if result>weight_third_standard_deviation_start and result < weight_third_standard_deviation_end]

print("{}% of data for weight  lies within 1 standard deviation".format(len(weight_list_of_data_within_1_standard_deviation)*100.0 / len(weight_list)))
print("{}% of data for weight  lies within 2 standard deviation".format(len(weight_list_of_data_within_2_standard_deviation)*100.0 / len(weight_list)))
print("{}% of data for weight  lies within 3 standard deviation".format(len(weight_list_of_data_within_3_standard_deviation)*100.0 / len(weight_list)))


