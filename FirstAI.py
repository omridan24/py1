import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
time_studied = np.array([18,25,40,60,75,80]).reshape(-1,1)
scores = np.array([46,60,70,85,90,20]).reshape(-1,1)
model = LinearRegression()
model.fit(time_studied , scores)

print(model.predict(np.array([5]).reshape(-1,1)))

plt.scatter(time_studied , scores)
plt.plot(np.linspace(0,70,100).reshape(-1,1), model.predict(np.linspace(0,70,100).reshape(-1,1)),'r')
plt.ylim(0,100)
plt.show()
