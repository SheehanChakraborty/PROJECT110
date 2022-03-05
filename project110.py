import csv
import statistics
import plotly.figure_factory as ff
import random
import pandas as pd
import plotly.graph_objects as go
df = pd.read_csv("project110.csv")
data=df["average"].tolist()
#population_mean=statistics.mean(data)

#fig = ff.create_distplot([data],["average"],show_hist=False)

#fig.show()

def random_set_data(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0, len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    std_dev=statistics.stdev(dataset)
#    print("Standard daviation of sample :-",std_dev,mean)
    return mean

#function to plot mean on the graph

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(mean_list)

    fig = ff.create_distplot([df],["temp"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

#pass the number of the time you want the mean of the data point  as parameter 
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_data(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)

    print("mean of sampling distribution :-",mean)
setup()

#code to find the mean of the raw data("population.data")
population_mean=statistics.mean(data)
print("population of mean :-:",population_mean)
#code to find the standard daviation
def standard_daviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_mean=random_set_data(100)
        mean_list.append(set_of_mean)
    std_dev=statistics.stdev(mean_list)
    print("Standard daviation of sampling distribution :-",std_dev)
standard_daviation()
