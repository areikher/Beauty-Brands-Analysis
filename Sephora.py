import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
#from sklearn.linear_model import LinearRegression
import numpy as np
from statistics import mean

#creates the df
dfSephora = pd.read_csv(r'/Users/alison/Desktop/Sephora.csv')
#print(dfSephora)

corrMatrix = dfSephora.corr()
print(corrMatrix)
sn.heatmap(corrMatrix, annot=True)
plt.show()

femCnt = 0
pocCnt = 0
femPOCcnt = 0

for i in dfSephora.index:
    if dfSephora['Female'][i] == True:
        femCnt += 1
    if dfSephora['POC'][i] == True:
        pocCnt += 1
    if dfSephora['Female'][i] == True and dfSephora['POC'][i] == True:
        femPOCcnt += 1

print('Fem Count:', femCnt)
print('POC Count:', pocCnt)
print('POC and Fem:', femPOCcnt)
print()


plt.hist(dfSephora['Number of Products'])
plt.show()

plt.hist(dfSephora['Number of Clean'])
plt.show()

plt.hist(dfSephora['Percent Clean'])
plt.show()

plt.boxplot(dfSephora['Number of Products'])
plt.show()

plt.boxplot(dfSephora['Number of Clean'])
plt.show()

plt.boxplot(dfSephora['Percent Clean'])
plt.show()

plt.scatter(dfSephora['Percent Clean'], dfSephora['Number of Clean'])
plt.show()

plt.scatter(dfSephora['Number of Products'], dfSephora['Number of Clean'])
plt.show()

plt.scatter(dfSephora['Year Founded'], dfSephora['Number of Products'])
plt.show()

#model = LinearRegression()
#model.fit(dfSephora['Number of Products'], dfSephora['Number of Clean'])
#model = LinearRegression().fit(dfSephora['Number of Products'], dfSephora['Number of Clean'])
#r_sq = model.score(dfSephora['Number of Products'], dfSephora['Number of Clean'])
#print(r_sq)




def estimate_coef(x, y):
	# number of observations/points
	n = np.size(x)

	# mean of x and y vector
	m_x = np.mean(x)
	m_y = np.mean(y)

	# calculating cross-deviation and deviation about x
	SS_xy = np.sum(y*x) - n*m_y*m_x
	SS_xx = np.sum(x*x) - n*m_x*m_x

	# calculating regression coefficients
	b_1 = SS_xy / SS_xx
	b_0 = m_y - b_1*m_x

	return (b_0, b_1)

def plot_regression_line(x, y, b):
	# plotting the actual points as scatter plot
	plt.scatter(x, y, color = "m",
			marker = "o", s = 30)

	# predicted response vector
	y_pred = b[0] + b[1]*x

	# plotting the regression line
	plt.plot(x, y_pred, color = "g")

	# putting labels
	plt.xlabel('x')
	plt.ylabel('y')

	# function to show plot
	plt.show()

x = dfSephora['Number of Products']
y = dfSephora['Number of Clean']
b = estimate_coef(x, y)
print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
 
# plotting regression line
plot_regression_line(x, y, b)
print()
correlation_matrix = np.corrcoef(x, y)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2

print(r_squared)
print()

productDict = {}
for i in dfSephora.index:
    product = [x.strip() for x in dfSephora['Product Types'][i].split(',')]
    #product = dfSephora['Product Types'][i].split(',')
    #print(product)
    for item in product:
        if item in productDict:
            productDict[item] +=1
        else:
            productDict[item] =1

print(productDict)

print('Mean number of products:', round(mean(dfSephora['Number of Products']),2))
print('Mean number of clean products:', round(mean(dfSephora['Number of Clean']),2))
print('Mean percent of clean products:', round(mean(dfSephora['Percent Clean']),2))
print('Mean of Year Founded:', round(mean(dfSephora['Year Founded']),2))

oneOwner = 0
twoOwners = 0
threeOwners = 0
fourOwners = 0
for i in dfSephora.index:
	owner = dfSephora['Owner'][i]
	if 'and' in owner and ',' in owner:
		commasCnt = owner.count(",")
		if commasCnt == 2:
			threeOwners +=1
		elif commasCnt == 3:
			fourOwners +=1
	elif 'and' in owner:
		twoOwners += 1
	else:
		oneOwner += 1

print()
print('Number of 1 owner:', oneOwner)
print('Number of 2 owners:', twoOwners)
print('Number of 3 owners:', threeOwners)
print('Number of 4 owners:', fourOwners)

