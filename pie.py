import matplotlib.pyplot as plt
import numpy as np
y=np.array([1,2,3,4])
mylabels=["A","B","C","D"]
myexplode=[0.1,0.2,0.3,0.4]
plt.pie(y,labels=mylabels,explode=myexplode,shadow=True)
plt.show()
