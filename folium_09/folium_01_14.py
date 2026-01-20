import folium
m=folium.Map(location=[37.547631,126.942463],zoom_start= 15 )

#근처 맛집
folium.Marker([37.610604, 126.916667],popup='맥도날드',
              icon=folium.Icon(color="balck",icon='info-sign')).add_to(m)

folium.Marker([37.610790, 126.916812],popup='김밥천국',
              icon=folium.Icon(color="balck",icon='info-sign')).add_to(m)

#popup - 클릭했을때 뜨는 말풍선
# color="lightblue" - 마커 색상
# 무산역
folium.Marker([37.611314, 126.917213],popup='subway',tooltip="구산역",
              icon=folium.Icon(color="lightblue",icon='fa-solid fa-train-subway',prefix="fa-solid")).add_to(m)
m.save("map.html")


