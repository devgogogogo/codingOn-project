import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  

x= np.linspace(2,100,20)
y= np.linspace(10,35,20)

y_nosiy= y + np.random.uniform(-5,5,size=20)

plt.scatter(x,y, color= 'green', marker='o')

plt.title("linspace +  난수로 불규칙한 산점도")
plt.xlabel("x 값")
plt.ylabel("y 값")
plt.grid(linestyle=':', alpha=0.5)
plt.show()