# 그래프를 그리기 위한 matplotlib 모듈 불러오기
import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [2,4,6,8,10]

# #x와 y값으로 선 그래프를 그리고 화면에 표시
# plt.plot(x,y)
# #제목 붙이기
# plt.title("my first graph")

# #축 이름 붙이기
# plt.xlabel("X")
# plt.ylabel("Y")

# # 범례 추가
# plt.plot(x,y,label="Linear")
# plt.plot(x,y2, label = "Square")

# #선 색생 바꾸기
# plt.plot(x,y, marker="o", label = "Don Line")

# #격자 표시
# plt.grid()
# # 범례 추가된 것 적용(범례 표시)
# plt.legend()
# # 표 보여주기
# plt.show()

#가장 많이 쓰는 기본 형태(암기하세요)

# x = [1,2,3,4,5]
# y = [10,20,30,40,50]

# plt.plot(x,y ,marker="o", label="Example")  # plt.plot()-> 그래프 그리기

# plt.title("Matplotlib Basic Example")
# plt.xlabel("X")
# plt.ylabel("Y") # label -> 범례 이름
# plt.grid() # plt. grid()-> 눈금
# plt.legend() # plt.legend()-> 범례 표시
# plt.show() # plt. show() -> 화면 출력


# 그래프를 그리기 위한 matplotlib 모듈 불러오기
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  
fig, axs = plt. subplots()
montths=["Jan","Feb","Mar","Apr","May","Jun","jul","Aug","Sep","Oct","Nov","Dec"]
sales_2019=[100,120,140,110,130,150,160,170,180,200,190,210]
sales_2020=[90,110,130,120,140,160,170,160,150,180,200,190]
axs.plot(montths,sales_2019,label="2019",color='b')
axs.plot(montths,sales_2020,label="2020",color='r')


plt.title("Monthly Sales Comparison(2019-2020)", color="blue")
plt.xlabel("Month 값")
plt.ylabel("Sales")
plt.legend()
plt.show()
