import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

file_pyserial=open('data_from_uart/data_pyserial.txt',mode='r',encoding='utf8')
file_custom=open('data_from_uart/data_custom_uart.txt',mode='r',encoding='utf8')
pyserial_data=[]
custom_data=[]
len_str=30


while True:
    line_pyserial=file_pyserial.readline()
    line_custom=file_custom.readline()
    if not line_pyserial or not line_custom:
        break

    pyserial_data.append(round(float(line_pyserial),3))
    custom_data.append(round(float(line_custom),3))

times_custom=np.array(custom_data)
times_pyserial=np.array(pyserial_data)
speed_custom=np.array(1/(times_custom/len_str/8),dtype='int')
speed_pyserial=np.array(1/(times_pyserial/len_str/8),dtype='int')


file_pyserial.close()
file_custom.close()

print(speed_custom)
print(speed_pyserial)

fig=plt.figure(figsize=(11,8))
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)



ax1.plot(times_custom,label='custom')
ax2.plot(times_pyserial,label='pyserial')
ax3.plot(speed_custom,label='custom')
ax4.plot(speed_pyserial,label='pyserial')

ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()

fig.suptitle('data transmission statistics for a 15 byte string')

ax1.set(xlim=(0,15),ylim=(0,0.05))
ax1.xaxis.set_major_locator(MultipleLocator(base=1))
ax1.set_xlabel('number of iteration')
ax1.set_ylabel('time in sec')
ax1.grid()

ax2.set(xlim=(0,15),ylim=(1.5,3))
ax2.xaxis.set_major_locator(MultipleLocator(base=1))
ax2.set_xlabel('number of iteration')
ax2.set_ylabel('time in sec')
ax2.grid()

ax3.set(xlim=(0,15),ylim=(0,17000))
ax3.xaxis.set_major_locator(MultipleLocator(base=1))
ax3.set_xlabel('number of iteration')
ax3.set_ylabel('speed in bits/second')
ax3.grid()

ax4.set(xlim=(0,15),ylim=(0,150))
ax4.xaxis.set_major_locator(MultipleLocator(base=1))
ax4.set_xlabel('number of iteration')
ax4.set_ylabel('speed in bits/second')
ax4.grid()


plt.show()