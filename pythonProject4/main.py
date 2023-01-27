import pandas as pd
import math
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import life
from life import theAnswer
data = pd.read_csv("cost_revenue_clean.csv")
import math
# print(data.describe())

X = DataFrame(data, columns=['production_budget_usd'])
y = DataFrame(data, columns=['worldwide_gross_usd'])
# LinearRegression
regression = LinearRegression()
regression.fit(X, y)

# Slope Coefficient
# print(regression.coef_)  # theta_1

# Intercept
# print(regression.intercept_)

# print(regression.score(X, y))


# plt.figure(figsize=(10, 6))
# plt.scatter(X, y, alpha=0.3)
# plt.plot(X, regression.predict(X), color='red', linewidth=4)
# plt.title('Film Cost vs Global Revenue')
# plt.xlabel('Production Budget $')
# plt.ylabel('Worldwide Gross $')
# plt.ylim(0,3000000000)
# plt.xlim(0,450000000)
# plt.show()

# lsd_math_score_data.csv
data = pd.read_csv('lsd_math_score_data.csv')
print(data)
print(" ")
print(type(data.Time_Delay_in_Minutes))
print(" ")
onlyMathScores = data['Avg_Math_Test_Score']
print(onlyMathScores)

data['Test_Subject'] = 'Jennifer Lopez'
print(" ")
print(data)
print(" ")
data['High_Score'] = 100
print(data)
# Challenge: Overwrite values in rows for High_score to equal average score + 100
# for i in range(len(data.Avg_Math_Test_Score)):
#     data.High_Score[i] = float(data.High_Score[i] + data.Avg_Math_Test_Score[i])
#     # print(i)
# print(data)
# print(" ")
data['High_Score'] = data['High_Score'] + data['Avg_Math_Test_Score']
print(data)
print(" ")
# Challenge: Square the values stored inside High_Score
data['High_Score'] = data['High_Score']**2
print(data)
print(type(onlyMathScores))
print(" ")
# Challenge: Create a list called columnist. Put 'LSD_ppm' and 'Avg_Math_Test_Score' inside.
columnList = ['LSD_ppm', 'Avg_Math_Test_Score']
print(columnList)
# cleanData = data[columnList]
cleanData = data[['LSD_ppm', 'Avg_Math_Test_Score']]
print(cleanData)
print(type(cleanData))

print(" ")
# y = data[[Avg_Math_Test_Score]]
# print(type(y))
y = data['Avg_Math_Test_Score']
print(type(y))
print(" ")
# Challenge: 1) Create a variable called X
# Set X equal to the values of LSD_ppm
X = data[['LSD_ppm']]
# Make sure X is a dataframe
# 2) print the value of X
print(X)
# 3) show the type of X
print(type(X))

print(" ")
# Delete test challenge
del data['Test_Subject']
print(data)
print(" ")

# Challenge: Delete the High_Score column from data
del data['High_Score']
print(data)

# # import life.py
# # print(type(life.py))
print(" ")
print('theAnswer' , theAnswer)



print(" ")
# 1) Import math module into notebook
# 2) Print out value of pi
# 3) Print out value of e
print(math.pi)
print(math.e)

print(" ")
def get_milk():
    print('Open door')
    print('Walk to the store')
    print('Buy milk on hte ground floor')
    print('Return with milk galore')

get_milk()
print(" ")
def fill_the_fridge(amount):
    print('Open door')
    print('Walk to the store')
    print('Buy ' + amount + ' cartons on the ground floor')
    print('Return with milk galore')
fill_the_fridge('five')
print(" ")
fill_the_fridge("one thousand")

print(" ")
def milk_mission(amount, destination):
    print('Open door')
    print('Walk to the  ' + destination)
    print('Buy ' + amount + ' cartons on the ground floor')
    print('Return with milk galore')
milk_mission('twenty', 'department store')

print(" ")
def times(a,y):
    # result = a * y
    return a * y
print(times(3.14, 5.09))
print(" ")
life.quote_marvin()

print(" ")
print(life.square_root(63.14))
print(" ")
print(data)
print(" ")
time = data[['Time_Delay_in_Minutes']]
print(time)
print(" ")
LSD = data[['LSD_ppm']]
print(" ")
score = data[['Avg_Math_Test_Score']]
print(score)
print(" ")
# %matplotlib inline
# plt.title("Tissue concentration of LSD over time", fontsize=17)
# plt.xlabel('Time in Minutes', fontsize=14)
# plt.ylabel('Tissue LSD ppm', fontsize = 14)
#
# plt.text(x=0, y=0, s='Wagner et al.(1968)', fontsize = 12)
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)
#
# plt.ylim(1,7)
# plt.xlim(0,500)
#
# plt.style.use('classic')


# plt.plot(time,LSD, color='#5D4037', linewidth=10)
# plt.show()

regr = LinearRegression()
regr.fit(LSD,score)
print(type(LSD))
print(" ")
print(regr.coef_)
print(regr.coef_[0])
print('Theta1:', regr.coef_[0][0])
print(" ")
print('Intercept: ', regr.intercept_[0])
print(" ")
print('R-Square: ' ,regr.score(LSD,score))
predicted_score = regr.predict(LSD)
print(" ")
plt.title('Arithmetic vs LSD-25', fontsize=17)
plt.xlabel('Tissue LSD ppm', fontsize=14)
plt.ylabel('Performance Score', fontsize=14)
plt.ylim(25,85)
plt.xlim(1,6.5)
plt.style.use('fivethirtyeight')
plt.scatter(LSD, score, color='blue', s=100 , alpha=0.7)
plt.plot(LSD,predicted_score, color='red', linewidth=3)
plt.show()