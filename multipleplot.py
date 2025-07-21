import matplotlib.pyplot as plt
import numpy as np
#plot 1
x=np.array([0,1,2,3])
y=np.array([1,10,9,4])
plt.subplot(1,2,1)
plt.plot(x,y)
#plot2
x=np.array([1,4,4,7])
y=np.array([4,2,6,9])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("Image")
plt.show()
