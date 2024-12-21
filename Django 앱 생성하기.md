## 1. Django App생성하기

1. 가상 환경이 실행된 상태에서 작업합니다.
![](https://i.imgur.com/zEYn8pq.png)

<br>

2. 생성할 기능(앱)의 이름을 정해서 manage.py를 통해 생성합니다.

``` bash
python manage.py startapp maps # 'maps'라는 이름의 앱을 생성
```


3. maps 앱이 생성되었습니다.
![](https://i.imgur.com/Aw5cjG8.png)


4. 앱을 생성했으므로, **프로젝트 폴더(p2p)의 settings.py에 반드시 앱을 등록해야합니다.**
![](https://i.imgur.com/b65Odta.png)



5. maps 폴더에 urls.py를 생성하고 url을 정의합니다.
``` python
from django.urls import path
from . import views

urlpatterns = [	
	path('', views.map_view, name='map-view'),
]
```

<br>

## 2. 템플릿(Template) 정의하기 
1. templates > maps 폴더를 생성합니다.

![](https://i.imgur.com/3tVlLcy.png)
![](https://i.imgur.com/yczSBqk.png)




2. maps > map.html 파일을 생성하고 코드를 작성합니다.
``` html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>카카오 맵 API 예제</title>
    <script src="//dapi.kakao.com/v2/maps/sdk.js?appkey=YOUR_APP_KEY&libraries=services"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
</head>
<body>
    <div id="map" style="width:100%;height:500px;"></div>

    <script>
        var mapContainer = document.getElementById('map'),
            mapOption = { 
                center: new kakao.maps.LatLng(37.5665, 126.9780),
                level: 5
            };
        var map = new kakao.maps.Map(mapContainer, mapOption);

        var openInfoWindow = null;

        function toggleInfoWindow(marker, infowindow) {
            if (openInfoWindow) {
                openInfoWindow.close();
            }
            if (infowindow === openInfoWindow) {
                openInfoWindow = null;
            } else {
                infowindow.open(map, marker);
                openInfoWindow = infowindow;
            }
        }

        function loadParkingData() {
            Papa.parse("/static/data/parking.csv", {  // CSV 파일 경로를 설정
                download: true,
                header: true,
                complete: function(results) {
                    var parkingData = results.data;
                    parkingData.forEach(function(parking) {
                        var marker = new kakao.maps.Marker({
                            map: map,
                            position: new kakao.maps.LatLng(parking['위도'], parking['경도']),
                            title: parking['주차장명']
                        });

                        var infowindow = new kakao.maps.InfoWindow({
                            content: '<div style="padding:10px;">주차장명: ' + parking['주차장명'] + '<br>주소: ' + parking['주소'] + '</div>'
                        });

                        kakao.maps.event.addListener(marker, 'click', function() {
                            toggleInfoWindow(marker, infowindow);
                        });
                    });
                },
                error: function(error) {
                    console.error("CSV 파일을 로드할 수 없습니다:", error);
                }
            });
        }

        loadParkingData();
    </script>
</body>
</html>
```

<br>

## 3. 뷰(View) 생성하기 

1. maps의 views.py에 코드를 작성합니다.
![](https://i.imgur.com/ih7FSzJ.png)

``` python
from django.shortcuts import render

def map_view(request):
    return render(request, 'maps/map.html')

```


<br>

## 4. URL 구성하기
1. p2p/urls.py 에서 urlpattern을 구성합니다.
``` python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maps/', include('maps.urls')),
]
```



## 5. 실행 후 앱 동작 확인하기
가상환경 실행 후 manage.py가 있는 경로에서 실행합니다.
``` python
python manage.py runserver
```

![](https://i.imgur.com/OePsBw4.jpeg)
