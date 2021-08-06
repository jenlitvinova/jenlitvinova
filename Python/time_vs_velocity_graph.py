'''----------------------------------------------------------------------------------
 Script Name:   Time vs Velocity
 Author:        Yevgeniya Litvinova
 Required Arguments:
              Data Directory Path
              Shapefiles names

 Description: Creates a plot showing the distribution of velocity along the timeline

----------------------------------------------------------------------------------'''

import arcpy, os
from matplotlib import pyplot as plt
import datetime
import numpy as np

data_dir = "C:/Users/jenli/Google Drive/School/Python in GIS/EoT Data/EoT Data/smartphone_data/"
out_dir = "C:/Users/jenli/Google Drive/School/Python in GIS/EoT Data/"
shp = ["tp1_171711_nachabpfiff_Proje.shp", "tp2_171727_nachabpfiff_Proje.shp", "tp1_171729_nachabpfiff_Proje.shp"]

#Plot function creates time-velocity plots using matplotlib
def plot(data_dir, shp):
    #get velocity and time for each feature and store them as and array for plotting
    Velocity = []
    Time = []
    s_cursor = arcpy.SearchCursor(os.path.join(data_dir, shp))
    for row in s_cursor:
        Velocity.append(row.velocity)
        date, time = row.date.split("_")
        time = (datetime.datetime.strptime(time, "%H-%M-%S"))
        Time.append(datetime.datetime.strftime(time, "%H:%M:%S"))
    del s_cursor
    del row
    #creating and modifying the plot
    fig, ax = plt.subplots()
    data = {'velocity': Velocity, 'time': Time}
    ax.plot(data['velocity'])
    plt.xticks(range(len(data['time'])), data['time'], rotation = 45, fontsize = 9)
    for index, label in enumerate(ax.get_xticklabels()):
       if index % 100 != 0:
           label.set_visible(False)
    plt.title('Velocity vs Time')
    plt.xlabel('Timestamp (s)')
    plt.ylabel('Velocity (m/s)')
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    #saving the results
    savePath = os.path.join(out_dir, shp)+"_vel_time_.png"
    plt.savefig(savePath , dpi = 300, format = 'png')

#For loop to run Plot function for each of the shapefiles
for i in range(len(shp)):
    plot(data_dir, shp[i])
