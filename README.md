# BikeShare_DataAnalysis
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

In this project, I made use of data provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. I compared the system usage between three large cities: Chicago, New York City, and Washington, DC.

![image](https://user-images.githubusercontent.com/45936612/118684510-925dd380-b802-11eb-8024-320bc4e08e4f.png)

# Overview
In this project, I make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. I wrote code to import the data and answer interesting questions about it by computing descriptive statistics. I also wrote a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

# The Datasets ([cities data](https://drive.google.com/drive/folders/1un5wJdwv-7ca3z8xNWPBfhoAzvqFiGMQ?usp=sharing))
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:<br />
Start Time (e.g., 2017-01-01 00:07:57)<br />
End Time (e.g., 2017-01-01 00:20:53)<br />
Trip Duration (in seconds - e.g., 776)<br />
Start Station (e.g., Broadway & Barry Ave)<br />
End Station (e.g., Sedgwick St & North Ave)<br />
User Type (Subscriber or Customer)<br />

The Chicago and New York City files also have the following two columns:<br />
Gender<br />
Birth Year<br />

![image](https://user-images.githubusercontent.com/45936612/118685217-30519e00-b803-11eb-81ac-bb407c22d256.png)
                          *Data for the first 10 rides in the new_york_city.csv file*

# Statistics Computed
You will learn about bike share use in Chicago, New York City, and Washington by computing a variety of descriptive statistics. In this project, you'll write code to provide the following information:

### 1 Popular times of travel (i.e., occurs most often in the start time) 

most common month <br />
most common day of week <br />
most common hour of day <br />

### 2 Popular stations and trip

most common start station <br />
most common end station <br />
most common trip from start to end (i.e., most frequent combination of start station and end station) <br />

### 3 Trip duration

total travel time <br />
average travel time <br />

### 4 User info

counts of each user type <br />
counts of each gender (only available for NYC and Chicago) <br />
earliest, most recent, most common year of birth (only available for NYC and Chicago) <br />

# Softwares needed:
* Python 3, NumPy, and Pandas installed using Anaconda <br />
* A text editor, like VS Code or Atom. <br />
* A terminal application (Terminal on Mac and Linux or Cygwin on Windows). <br />
