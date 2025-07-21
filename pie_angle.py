import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,2,3,4])
mylabels=["A","B","C","D"]
plt.pie(y,labels=mylabels,startangle=90)
plt.show()
