from django.shortcuts import render
import json

# f = open("/Users/mac/Desktop/api/apis/static/data.csv", "r", encoding="cp949")
# lines = f.readlines()
# l = []
# x = []
# y = []
# for line in lines:
#     l.append(line.split(","))
# f.close()
# date = l[1:10]
# for i in range(9):
#     x.append(date[i][5]), y.append(date[i][6])

latitude = []
longitude = []

# with open("/Users/mac/Desktop/api/apis/static/data.json", "r") as file:
#     json_data = json.load(file)
#     json_test = json_data["records"]
#     print(type(json_test))
#     for lat in json_test:
#         latitude.append(lat["위도"])
#     for long in json_test:
#         longitude.append(long["경도"])
    # arr = []
    # for data in json_data:
    #     arr.append(data.split(","))
    #     file.close()
    # # print(json.dumps(json_data, indent=2, ensure_ascii=False))

# with open("/Users/mac/Desktop/api/apis/static/data.json", encoding='utf-8') as file:
#     park_data = json.load(file)
#     park_test = park_data["records"]
#     park_dict = []
#     for park in park_test:
#         context = {
#             "lat": park['위도'],
#             "long": park['경도'],
#             "addr": park['소재지지번주소'],
#             "name": park['공원명'],
#         }
#         park_dict.append(context)
#     parkJson = json.dumps(park_dict, ensure_ascii=False)
#     print(parkJson)

# Create your views here.
def index(req):

    return render(req, "apis/index.html")


def test(req):
    with open("/Users/mac/Desktop/api/apis/static/data.json", encoding='utf-8') as file:
        park_data = json.load(file)
        park_test = park_data["records"]
        park_dict = []
        for park in park_test:
            context = {
                "lat": park['위도'],
                "long": park['경도'],
                "addr": park['소재지지번주소'],
                "name": park['공원명'],
            }
            park_dict.append(context)
        parkJson = json.dumps(park_dict, ensure_ascii=False)
    return render(req, "apis/test.html", {'parkJson': parkJson})


def test2(req):
    context = {
        "x": x,
        "y": y,
        "date": date,
    }
    return render(req, "apis/test2.html", context)


# from django.shortcuts import render
# import requests

# # f = open('C:/Users/이주용/Desktop/KDT해커톤/pjt/map/static/csv/datatarere.csv', 'r', encoding='cp949')
# f = open('D:/10-12/apis/static/data.csv', 'r', encoding='cp949')
# lines = f.readlines()
# f2 = open('D:/10-12/apis/static/data.csv', 'r', encoding='cp949')
# lines2 = f2.readlines()
# l = []
# key = '87CF7527-F440-36B2-83BD-8B2EABF87D2B'
# for i in range(1, len(lines)):
#     d = lines[i].strip().split(',')
#     for j in range(len(d[3])):
#         if d[3][j] == '(':
#             d[3] = d[3][:j]
#             break
#     # print(d)
#     address = d[3]
#     url1 = 'http://api.vworld.kr/req/address?service=address&request=getcoord&version=2.0&crs=epsg:4326&address=' + address + '&refine=true&simple=false&format=json&type=road&key=' + key
#     url2 = 'http://api.vworld.kr/req/address?service=address&request=getcoord&version=2.0&crs=epsg:4326&address=' + address + '&refine=true&simple=false&format=json&type=parcel&key=' + key
#     result1 = requests.get(url1)
#     result2 = requests.get(url2)
#     json_data1 = result1.json()
#     json_data2 = result2.json()

#     if json_data1['response']['status'] == 'OK':
#         x = json_data1['response']['result']['point']['x']
#         y = json_data1['response']['result']['point']['y']
#         l.append([x, y, d[3], '공공쓰레기통'])
#     if json_data2['response']['status'] == 'OK':
#         x = json_data2['response']['result']['point']['x']
#         y = json_data2['response']['result']['point']['y']
#         l.append([x, y, d[3], '공공쓰레기통'])
# f.close()

# for i in range(1, len(lines2)):
#     d = lines2[i].strip().split(',')
#     l.append([d[1], d[0], d[2], d[4]])

# f2.close()
# # Create your views here.
# def index(request):
#     data = l
#     context = {'data' : data}
#     return render(request, 'map/index.html', context)
