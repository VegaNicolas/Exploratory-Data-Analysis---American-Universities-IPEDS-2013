import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
The goal of this project is to find out which are the most relevant features 
that students take into account to choose the favorite university. 
Some of the essential questions for developing this project are related to the 
number of applications, admissions, and enrollments, cost of tuition and fees, 
cost of living on campus, types of degrees offered, and features of the states 
where universities are located (population and GDP).



Answer the following hypotheses and questions:

-Do universities with a high number of applications are the preferred ones by students? 
in other words, could the number of applications tell us that a university is one of the most preferred by students?
-Do students prefer universities that have a high rate of admission? 
in other words, do students prefer a university where it is easier for them to be admitted?.
-Do students prefer public or private universities?
-Do students prefer universities with low tuition and fees?
-Do students prefer a university for its low on-campus cost of living?
-Do students prefer universities from highly populated states?
-Do students prefer a university because it belongs to a state with a high GDP per capita?
-Do students prefer a university based on the possibility of a higher, additional academic degree in the same university?


https://blog.jovian.com/what-makes-a-student-prefer-a-university-part-i-data-preparation-f581b699dcab
https://www.kaggle.com/code/akershishukla/eda-students-university-preference

"""


# definimos el dataframe

df_universities = pd.read_excel("IPEDS_data.xlsx")

# shape

print(df_universities.shape) # (1534, 145)

