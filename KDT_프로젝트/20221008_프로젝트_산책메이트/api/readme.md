## Django 카카오 API 전국 공원정보 연동작업

#### urls.py

``` python
from django.urls import path
from . import views

app_name = 'apis'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
]
```

#### views.py

* 전체 json 파일을 통째로 넘기면 불러올 때 너무 오래걸리므로 필요한 정보만 가져온다.
* 조회에 필요한 공원정보 : 위도, 경도, 소재지의주소, 공원명
* 필요한 데이터를 json형식으로 js 코드가 있는 test.html에 렌더링한다.

``` python
import json

def test(req):
    with open("/Users/mac/Desktop/api/apis/static/data.json", encoding='utf-8') as file:
        park_data = json.load(file)
        park_test = park_data["records"] # data.json에 records 내에 공원에 대한 정보가 있다.
        park_dict = [] # context를 dict에 저장
        for park in park_test:
          	# 우리가 필요한 정보
            context = {
                "lat": park['위도'],
                "long": park['경도'],
                "addr": park['소재지지번주소'],
                "name": park['공원명'],
            }
            park_dict.append(context)
        parkJson = json.dumps(park_dict, ensure_ascii=False)
    return render(req, "apis/test.html", {'parkJson': parkJson})
```

<br>

#### test.html

* views에서 정의한 전국공원데이터의 값을 가져와 JSON으로 파싱
* escapejs로 유니코드 문자를 제거

* 전국 공원정보가 저장된 parks의 길이만큼 반복문을 돌면서 공원 데이터를 positions에 저장
* 마커를 생성하고 저장된 좌표값을 출력

``` html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>마커 생성하기</title>
  </head>

  <body>
    <div id="map" style="width:500px;height:600px;"></div>

    <script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=c262112c4811d99bb369cd08f0c8ef80&libraries=clusterer&libraries=services"></script>
    <script>
      var mapContainer = document.getElementById('map'), // 지도를 표시할 div
        mapOption = {
          center: new kakao
            .maps
            .LatLng(37.4849620, 126.933577), // 지도의 중심좌표
          level: 3 // 지도의 확대 레벨
        };

      var map = new kakao
        .maps
        .Map(mapContainer, mapOption); // 지도를 생성합니다
    </script>
    <script>
      <!-- views에서 저장한 parkJson을 JSON으로 파싱하여 저장, escapejs를 이용해 유니코드 문자를 제거 -->
      var parks = JSON.parse("{{ parkJson|escapejs }}")
      console.log(parks) <!-- 테스트 출력용 -->
      var positions = []
      for (var i = 0; i < Object.keys(parks).length; i++) {
        var context = {
          name: parks[i].name,
          latlng: new kakao 
            .maps
            .LatLng(parks[i].lat, parks[i].long), <!-- 위도와 경도 정보를 카카오 LatLng함수 형식에 맞게 저장 -->
          addr: parks[i].addr
        }
        positions.push(context)
      }
      console.log(positions);

      // 마커 이미지의 이미지 주소입니다
      var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
      for (var i = 0; i < positions.length; i++) {
        // 마커 이미지의 이미지 크기 입니다
        var imageSize = new kakao
          .maps
          .Size(24, 35);
        // 마커 이미지를 생성합니다
        var markerImage = new kakao
          .maps
          .MarkerImage(imageSrc, imageSize);
        // 마커를 생성합니다
        var marker = new kakao
          .maps
          .Marker({
            map: map, // 마커를 표시할 지도
            position: positions[i].latlng, // 마커를 표시할 위치
            title: positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
            image: markerImage // 마커 이미지
          });
      };

      // 아래 코드는 지도 위의 마커를 제거하는 코드입니다
      // marker.setMap(null);
    </script>
  </body>
</html>
```

<br>

