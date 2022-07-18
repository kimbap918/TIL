# numbers = map(int, input().split())
# print(sum(numbers))
# # 첫번째로 입력을 받을때 반환값이 str이지만 출력시에 sum()함수를 사용하고있다.
# # 따라서 int로의 형변환을 사용해야한다.
# # 두번째로 .split()을 통해 최종적으로 numbers는 리스트를 반환한다. 단순히 출력에서
# # int로 형변환은 리스트인 numbers에는 사용하지 못하기때문에 map을 사용해서 int로 형변환 후 입력받는다.

# words = list(map(str, input().split()))
# print(words)
# # 예시의 입력은 str을 입력하여 리스트로 반환받는것이나, int로 I'm tutor 6를
# # 입력했기 때문에 오류가 발생하였다. int를 str로 변경해준다.

# number = "22020718"
# print(len(number))
# # int 타입의 값은 len()함수에 들어갈 수 없다. 사용하려면 문자열을 사용해야한다.
 
# N = 10
# answer = []
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)
# # 튜플에는 새로운 값을 추가할 수 없기때문에 append를 사용할 수 없다!
# # 리스트를 사용하자.

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number # 1+2+3+4+5+6+7+8+9+10 = 55
#     count += 1 # 10
# print(total/count)
# # 첫 번째로 증가해야할 count가 for문 안에 들어있지 않아서 count = 1이 되었다.
# # count를 for 문 안에 넣고, 두번째로 total을 count로 나누어야하는데 몫을 구하고있다.
# # total/count로 바꾼다.

# word = "HappyHacking"
# count = 0

# for char in word:
#     if char in "aeiou":
#         count += 1
# print(count)
# # a, e, i, o, u 중에 하나라도 있으면 카운트가 늘어나게끔 했는데 이 경우엔
# # a만 있어도 문자열의 길이만큼 카운트가 증가한다.
# # 바꾼다면 차라리 char in "aeiou"로 하는게 나을것이다.

# from pprint import pprint

# fruits = [
#     "Soursop",
#     "Grapefruit",
#     "Apricot",
#     "Juniper berry",
#     "Feijoa",
#     "Blackcurrant",
#     "Cantaloupe",
#     "Salal berry",
# ]

# fruit_count = {}

# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count[fruit] = 1
#     else:
#         fruit_count[fruit] += 1

# pprint(fruit_count)

# number_list = [1, 23, 9, 6, 91, 59, 29]
# max1 = max(number_list)

# number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
# max2 = max(number_list2)

# if max1 > max2:
#     print("첫 번째 리스트의 최댓값이 더 큽니다.")

# elif max1 < max2:
#     print("두 번째 리스트의 최댓값이 더 큽니다.")

# else:
#     print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")
# # 변수 이름을 max로 지정해서 함수 max()가 변수로 인식

# from pprint import pprint


# def movie_info(movie, genres):
#     genres_names = []
#     genre_ids = movie["genre_ids"]
#     for genre_id in genre_ids:
#         for genre in genres:
#             if genre_id == genre["id"]:
#                 genre_name = genre["name"]
#                 genres_names.append(genre_name)

#     new_movie_info = {
#         "genre_names": genres_names,
#         "id": movie["id"],
#         "overview": movie["overview"],
#         "title": movie["title"],
#         "vote_average": movie["vote_average"],
#     }
#     return new_movie_info



# if __name__ == "__main__":
#     movie = {
#         "adult": False,
#         "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
#         "genre_ids": [18, 80],
#         "id": 278,
#         "original_language": "en",
#         "original_title": "The Shawshank Redemption",
#         "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
#         "popularity": 67.931,
#         "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
#         "release_date": "1995-01-28",
#         "title": "쇼생크 탈출",
#         "video": False,
#         "vote_average": 8.7,
#         "vote_count": 18040,
#     }

#     genres_list = [
#         {"id": 28, "name": "Action"},
#         {"id": 12, "name": "Adventure"},
#         {"id": 16, "name": "Animation"},
#         {"id": 35, "name": "Comedy"},
#         {"id": 80, "name": "Crime"},
#         {"id": 99, "name": "Documentary"},
#         {"id": 18, "name": "Drama"},
#         {"id": 10751, "name": "Family"},
#         {"id": 14, "name": "Fantasy"},
#         {"id": 36, "name": "History"},
#         {"id": 27, "name": "Horror"},
#         {"id": 10402, "name": "Music"},
#         {"id": 9648, "name": "Mystery"},
#         {"id": 10749, "name": "Romance"},
#         {"id": 878, "name": "Science Fiction"},
#         {"id": 10770, "name": "TV Movie"},
#         {"id": 53, "name": "Thriller"},
#         {"id": 10752, "name": "War"},
#         {"id": 37, "name": "Western"},
#     ]

#     pprint(movie_info(movie, genres_list))
# # 리턴이 없잖아!
n = int(input())
def length_no(n):
    cnt = 0
    while n:
        n //= 10
        cnt += 1

    return cnt
print(length_no(n))


# i = int(input())
# a = i // 100
# b = ( i - ( a * 100 )) // 10
# c = i % 10
# d = [a, b, c]

# print(d)

# import math

# n = int(input())
# x = [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
# print(x)

