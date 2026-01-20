#파이차트
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  


# labels = ['Python','Java','C++','JavaScript']
# sizes = [ 45,30,15,10]

# plt.pie(sizes,labels=labels, autopct='%1.2f%%',startangle=90)
# plt.title("프로그래밍 언어 선호도(파이차트)")
# plt.axis('equal')
# plt.show()

labels = ['Apple','Banana','Mango','Blueberry']
sizes=[15,30,45,10] 

plt.pie(sizes,labels=labels,explode=(0,0.1,0,0), autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.show()