from sklearn import linear_model
clf = linear_model.LinearRegression()
clf.fit ([[59, 15,5,10], [-44, 8,15,-336], [7, 4,-6,15],[17, 42,-26,-15]] ,[13, 58, -66,45])
print(clf)
print(clf.coef_)
