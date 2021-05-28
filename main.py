import plotly.figure_factory as ff
#import plotly.graph_object as go
import random
import statistics

#import plotly.express as px

dice_result = []


for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)
    #count.append(i)

mean = sum(dice_result)/len(dice_result)
standard_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)

first_standard_deviation_start,first_standard_deviation_end = mean - standard_deviation , mean + standard_deviation
second_standard_deviation_start,second_standard_deviation_end = mean - (2*standard_deviation)  ,mean + (2*standard_deviation)
third_standard_deviation_start,third_standard_deviation_end = mean - (3*standard_deviation) , mean + (3*standard_deviation) 

list_of_data_within_1_standard_deviation = [result for result in dice_result if result>first_standard_deviation_start and result < first_standard_deviation_end]
list_of_data_within_2_standard_deviation = [result for result in dice_result if result>second_standard_deviation_start and result < second_standard_deviation_end]
list_of_data_within_3_standard_deviation = [result for result in dice_result if result>third_standard_deviation_start and result < third_standard_deviation_end]

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_standard_deviation)*100.0 / len(dice_result)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_standard_deviation)*100.0 / len(dice_result)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_standard_deviation)*100.0 / len(dice_result)))

# fig = px.bar(x=dice_result,y=count)
fig = ff.create_distplot([dice_result],["Result"],show_hist=False)
fig.show()

print("mean is {} ".format(mean))
print("median is {} ".format(median))
print("Mode is {} ".format(mode))
print("Standard deviation is {} ".format(standard_deviation))
#print(dice1,dice2)