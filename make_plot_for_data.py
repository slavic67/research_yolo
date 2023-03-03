import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

min_deviation=np.array([0,0.97,1.12,0.84])
average_deviation=np.array([3.98,4.15,3.47,3.0])
max_deviation=np.array([6.46,8.49,5.89,6.53])
x=np.array(range(1,5))
fig=plt.figure(figsize=(7,4))
ax1=plt.subplot()
# ax1.set_xlim(xmin=0,xmax=len(min_deviation))
# ax1.set_xlabel('frame number')
# ax1.xaxis.set_major_locator(MultipleLocator(base=1))
# ax1.plot(x,min_deviation,color='r')
# ax1.plot(x,average_deviation,color='y')
# ax1.plot(x,max_deviation,color='g')
w=0.1
ax1.bar(x-w/2,min_deviation,width=w,color='g',label='min deviation')
ax1.bar(x+w/2,average_deviation,width=w,color='y',label='average deviation')
ax1.bar(x+3*w/2,max_deviation,width=w,color='r',label='max deviation')
ax1.set_xlim(xmin=0,xmax=len(min_deviation)+1)
ax1.xaxis.set_major_locator(MultipleLocator(base=1))
ax1.set_xlabel('quantity of wheels')
ax1.set_ylabel('deviation in %')
fig.suptitle('center deviation in %')
ax1.legend()
plt.grid()
plt.show()