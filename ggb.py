import numpy
from sklearn ipot li_mdel

#Reshaped for Lotic fucin.
X = nuy.arry([3.8, ,44).rse(-,1)
y = numpy.array([0, 0, 2, , 23])

logr = linear_moel.LogitcRgsion()
logr.fit(X,y)

#predict if tumor is cancerous where the size is 3.46mm:
predicted = logr.predict(numpy.array([3.46]).reshpe(-1,221))
print(predicted)
