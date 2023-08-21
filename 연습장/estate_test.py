import requests
import json
import pandas as pd
import os
import random
import time
import datetime
from tqdm.auto import tqdm
from pprint import pprint

# 여러 개의 User-Agent 추가
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/94.0.992.38",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/94.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/94.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 Edg/94.0.992.38",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
]

# 요청 헤더 설정
headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE2NTk5MzcxNTIsImV4cCI6MTY1OTk0Nzk1Mn0.PD7SqZO7z8f97uGQpfSKYMPbrLy6YtRl9XYHWaHiVVE",
    "Host": "new.land.naver.com",
    "Referer": "https://new.land.naver.com/...",
    "sec-ch-ua": "\".Not\/A)Brand\";v=\"99\", \"Google Chrome\";v=\"103\", \"Chromium\";v=\"103\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": random.choice(user_agents)
    }

# 요청 간격 설정 (랜덤한 간격)
def delay_request():
    time.sleep(random.uniform(2, 4))  # 2초에서 4초 사이의 랜덤한 시간 대기
    
# 데이터 가져오는 함수
def get_data(url):
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8-sig"
    data = json.loads(response.text)
    return data

# 아파트 정보 가져오는 함수
def get_apt_info(apt_code):
    url = f'https://new.land.naver.com/api/complexes/{apt_code}?sameAddressGroup=false'
    data = get_data(url)
    return data

# 학교 정보 가져오는 함수
def get_school_info(apt_code):
    url = f'https://new.land.naver.com/api/complexes/{apt_code}/schools'
    data = get_data(url)
    return data

# 가격 정보 가져오는 함수
def get_price_info(apt_code, index):
    p_num = data["complexPyeongDetailList"][index]["pyeongNo"]
    url = f'https://new.land.naver.com/api/complexes/{apt_code}/prices?complexNo={apt_code}&tradeType=A1&year=5&priceChartChange=true&areaNo={p_num}&areaChange=true&type=table'
    price_data = get_data(url)
    return price_data

# https://new.land.naver.com/api/complexes/3800/prices/real?complexNo=3800&tradeType=A1&year=5&priceChartChange=false&areaNo=0&type=table
# https://new.land.naver.com/api/complexes/3800/prices?complexNo=3800&tradeType=A1&year=5&priceChartChange=false&type=summary
# https://new.land.naver.com/api/articles/complex/3800?realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=true&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page=1&complexNo=3800&buildingNos=&areaNos=&type=list&order=rank

# 최상위 지역 정보 가져오기
sido_list = get_data('https://new.land.naver.com/api/regions/list?cortarNo=0000000000')
# 오늘 날짜 받아오기
today_date = datetime.datetime.now().strftime("%Y-%m-%d")

# 최상위 폴더를 오늘 날짜로 생성
top_level_dir = os.path.join('output', today_date)
os.makedirs(top_level_dir, exist_ok=True)

# 아파트 정보를 저장할 리스트 초기화s
# all_data = []

# 시도 정보 반복 처리

pbar_sido = tqdm(sido_list["regionList"][:1])
for sido in pbar_sido:
    print(sido)
    pbar_sido.set_postfix(current_sido=sido, refresh=False)
    sido_code = sido["cortarNo"]
    gungu_list = get_data(f'https://new.land.naver.com/api/regions/list?cortarNo={sido_code}')
    # gungu_list = get_data(f'https://new.land.naver.com/api/regions/list?cortarNo=2600000000')


    # 시도 폴더 생성
    sido_name = sido["cortarName"]
    pprint(sido_name)
    sido_dir = os.path.join(top_level_dir, sido_name)
    os.makedirs(sido_dir, exist_ok=True)

    # 1100000000 # 서울
    # 4100000000 # 경기
    # 2800000000 # 인천
    # 2600000000 # 부산
    # 3000000000 # 대전
    # 2700000000 # 대구
    # 3100000000 # 울산
    # 3600000000 # 세종
    # 2900000000 # 광주
    # 5100000000 # 강원
    # 4300000000 # 충북
    # 4400000000 # 충남
    # 4700000000 # 경북
    # 4800000000 # 경남
    # 4500000000 # 전북
    # 4600000000 # 전남
    # 5000000000 # 제주

    # 구 정보 반복 처리
    pbar_gu = tqdm(gungu_list["regionList"]) 
    for gungu in pbar_gu:
        print("\t", gungu)
        gungu_code = gungu["cortarNo"]
        dong_list = get_data(f'https://new.land.naver.com/api/regions/list?cortarNo={gungu_code}')

        # 구 폴더 생성
        gungu_name = gungu["cortarName"]
        gungu_dir = os.path.join(sido_dir, gungu_name)
        os.makedirs(gungu_dir, exist_ok=True)
        pbar_gu.set_postfix(current_gu=gungu['cortarName'], refresh=False)
        # 동 정보 반복 처리
        pbar_dong = tqdm(dong_list['regionList'])
        for dong in pbar_dong:
            dong_code = dong["cortarNo"]
            apt_list = get_data(f'https://new.land.naver.com/api/regions/complexes?cortarNo={dong_code}&realEstateType=APT&order=')
            dong_name = dong["cortarName"]

            # 아파트 정보를 저장할 리스트 초기화
            all_data = []

            pbar_dong.set_postfix(currnet_dong=dong['cortarName'], refresh=False)
            # 아파트 정보 반복 처리
            pbar_apt = tqdm(apt_list["complexList"])
            for apt in pbar_apt:

                apt_code = apt["complexNo"]
                data = get_apt_info(apt_code)
                temp_data = pd.DataFrame(columns=[
                    "아파트명", "면적", "법정동주소", "b_code", "지번주소", "도로명주소", "latitude", "longitude",
                    "세대수", "임대세대수", "최고층", "최저층", "용적률", "건폐율", "주차대수",
                    "건설사", "난방", "공급면적", "전용면적", "전용율", "방수", "욕실수",
                    "해당면적_세대수", "현관구조", "재산세", "재산세합계", "지방교육세", "재산세_도시지역분",
                    "종합부동산세", "결정세액", "농어촌특별세", "가격", "겨울관리비", "여름관리비",
                    "최소_매매호가", "최대_매매호가", "최소_전세호가", "최대_전세호가", "최소_월세호가", "최대_월세호가",
                    "최소_실거래가", "최대_실거래가", "초등학교_학군정보", "초등학교_설립정보", "초등학교_남학생수", "초등학교_여학생수"
                ])
                # pprint(apt_code)
                # pprint(data)
                # 데이터 가공 및 처리
                if "complexDetail" in data and "complexPyeongDetailList" in data:
                    try:
                        area_list = data["complexDetail"]["pyoengNames"].split(", ")
                        ex_flag = 1
                    except KeyError:
                        ex_flag = 0

                    if ex_flag == 1:
                        school_data = get_school_info(apt_code)

                        for i in range(len(area_list)):
                            
                            # 아파트 정보 정제
                            temp_data.loc[i, "아파트명"] = data["complexDetail"]["complexName"]
                            temp_data.loc[i, "면적"] = area_list[i]
                            try:
                                temp_data.loc[i, "법정동주소"] = data["complexDetail"]["address"]
                            except KeyError:
                                temp_data.loc[i,"법정동주소"] = data["complexDetail"]["roadAddressPrefix"]+" "+data["complexDetail"]["roadAddress"]
                            temp_data.loc[i,"b_code"] = data["complexDetail"]["cortarNo"]
                            temp_data.loc[i, "지번주소"] = data["complexDetail"]["detailAddress"]
                            try:
                                temp_data.loc[i,"도로명주소"] = data["complexDetail"]["roadAddressPrefix"]+" "+data["complexDetail"]["roadAddress"]
                            except KeyError:
                                temp_data.loc[i,"도로명주소"] = data["complexDetail"]["roadAddressPrefix"]
                            temp_data.loc[i,"latitude"] = data["complexDetail"]["latitude"]
                            temp_data.loc[i,"longitude"] = data["complexDetail"]["longitude"]
                            temp_data.loc[i,"세대수"] = data["complexDetail"]["totalHouseholdCount"]
                            temp_data.loc[i,"임대세대수"] = data["complexDetail"]["totalLeaseHouseholdCount"]
                            temp_data.loc[i,"최고층"] = data["complexDetail"]["highFloor"]
                            temp_data.loc[i,"최저층"] = data["complexDetail"]["lowFloor"]
                            try:
                                temp_data.loc[i,"용적률"] = data["complexDetail"]["batlRatio"]
                            except KeyError:
                                temp_data.loc[i,"용적률"]=""
                            try:
                                temp_data.loc[i,"건폐율"] = data["complexDetail"]["btlRatio"]
                            except KeyError:
                                temp_data.loc[i,"건폐율"]=""
                            try:
                                temp_data.loc[i,"주차대수"] = data["complexDetail"]["parkingPossibleCount"]
                            except KeyError:
                                temp_data.loc[i,"주차대수"]=""
                            try:
                                temp_data.loc[i,"건설사"] = data["complexDetail"]["constructionCompanyName"]
                            except KeyError:
                                temp_data.loc[i,"건설사"] = ""
                            try:
                                temp_data.loc[i,"난방"] = data["complexDetail"]["heatMethodTypeCode"]
                            except KeyError:
                                temp_data.loc[i,"난방"]=""
                            try:
                                temp_data.loc[i,"공급면적"] = data["complexPyeongDetailList"][i]["supplyArea"]
                            except KeyError:
                                temp_data.loc[i,"공급면적"] = ""
                            try:
                                temp_data.loc[i,"전용면적"] = data["complexPyeongDetailList"][i]["exclusiveArea"]
                            except KeyError:
                                temp_data.loc[i,"전용면적"]=""
                            try:
                                temp_data.loc[i,"전용율"] = data["complexPyeongDetailList"][i]["exclusiveRate"]
                            except KeyError:
                                temp_data.loc[i,"전용율"] = ""
                            try:
                                temp_data.loc[i,"방수"] = data["complexPyeongDetailList"][i]["roomCnt"]
                            except KeyError:
                                temp_data.loc[i,"방수"] = ""
                            try:
                                temp_data.loc[i,"욕실수"] = data["complexPyeongDetailList"][i]["bathroomCnt"]
                            except KeyError:
                                temp_data.loc[i,"욕실수"] = ""
                            try:
                                temp_data.loc[i,"해당면적_세대수"] = data["complexPyeongDetailList"][i]["householdCountByPyeong"]
                            except KeyError:
                                temp_data.loc[i,"해당면적_세대수"] = ""
                            try:
                                temp_data.loc[i,"현관구조"] = data["complexPyeongDetailList"][i]["entranceType"]
                            except KeyError:
                                temp_data.loc[i,"현관구조"] = ""
                            try:
                                temp_data.loc[i,"재산세"] = data["complexPyeongDetailList"][i]["landPriceMaxByPtp"]["landPriceTax"]["propertyTax"]
                            except KeyError:
                                temp_data.loc[i,"재산세"] = ""
                            try:
                                temp_data.loc[i,"재산세합계"] = data["complexPyeongDetailList"][i]["landPriceMaxByPtp"]["landPriceTax"]["propertyTotalTax"]
                            except KeyError:
                                temp_data.loc[i,"재산세합계"] = ""
                            try:
                                temp_data.loc[i,"지방교육세"] = data["complexPyeongDetailList"][i]["landPriceMaxByPtp"]["landPriceTax"]["localEduTax"]
                            except KeyError:
                                temp_data.loc[i,"지방교육세"] = ""
                            try:
                                temp_data.loc[i,"재산세_도시지역분"] = data["complexPyeongDetailList"][i]["landPriceMaxByPtp"]["landPriceTax"]["cityAreaTax"]
                            except KeyError:
                                temp_data.loc[i,"재산세_도시지역분"] = ""
                            try:
                                temp_data.loc[i,"종합부동산세"] = data["complexPyeongDetailList"][i]["landPriceMaxByPtp"]["landPriceTax"]["realEstateTotalTax"]
                            except KeyError:
                                temp_data.loc[i,"종합부동산세"] = ""
                            try:
                                temp_data.loc[i,"결정세액"] = data["complexPyeongDetailList"][i]["landPriceMaxByPtp"]["landPriceTax"]["decisionTax"]
                            except KeyError:
                                temp_data.loc[i,"결정세액"] = ""
                            try:
                                temp_data.loc[i,"농어촌특별세"] = data["complexPyeongDetailList"][i]["landPriceMaxByPtp"]["landPriceTax"]["ruralSpecialTax"]
                            except KeyError:
                                temp_data.loc[i,"농어촌특별세"] = ""


                            # 가격 정보 정제
                            price_data = get_price_info(apt_code, i)
                            try:
                                temp_data.loc[i,"가격"] = data["marketPrices"][0]["dealAveragePrice"]
                            except KeyError:
                                temp_data.loc[i,"가격"]=""
                            try:
                                temp_data.loc[i,"겨울관리비"] = data["complexPyeongDetailList"][i]["averageMaintenanceCost"]["winterTotalPrice"]
                            except KeyError:
                                temp_data.loc[i,"겨울관리비"] = ""
                            try:
                                temp_data.loc[i,"여름관리비"] = data["complexPyeongDetailList"][i]["averageMaintenanceCost"]["summerTotalPrice"]
                            except KeyError:
                                temp_data.loc[i,"여름관리비"] = ""
                                
                            # 매매호가 정보 처리
                            try:
                                deal_price_string = data["complexPyeongDetailList"][i]["articleStatistics"]["dealPriceString"]
                                if "~" in deal_price_string:
                                    min_deal_price, max_deal_price = deal_price_string.split("~")
                                    temp_data.loc[i, "최소_매매호가"] = min_deal_price.strip()
                                    temp_data.loc[i, "최대_매매호가"] = max_deal_price.strip()
                                else:
                                    temp_data.loc[i, "최대_매매호가"] = deal_price_string.strip()
                            except KeyError:
                                pass
                                
                            # 전세호가 정보 처리
                            try:
                                deal_price_string = data["complexPyeongDetailList"][i]["articleStatistics"]["leasePriceString"]
                                if "~" in deal_price_string:
                                    min_deal_price, max_deal_price = deal_price_string.split("~")
                                    temp_data.loc[i, "최소_전세호가"] = min_deal_price.strip()
                                    temp_data.loc[i, "최대_전세호가"] = max_deal_price.strip()
                                else:
                                    temp_data.loc[i, "최대_전세호가"] = deal_price_string.strip()
                            except KeyError:
                                pass
                                
                            # 월세호가 정보 처리
                            try:
                                deal_price_string = data["complexPyeongDetailList"][i]["articleStatistics"]["rentPriceString"]
                                if "~" in deal_price_string:
                                    min_deal_price, max_deal_price = deal_price_string.split("~")
                                    temp_data.loc[i, "최소_월세호가"] = min_deal_price.strip()
                                    temp_data.loc[i, "최대_월세호가"] = max_deal_price.strip()
                                else:
                                    temp_data.loc[i, "최대_월세호가"] = deal_price_string.strip()
                            except KeyError:
                                pass
                                
                            # 실거래가 정보 처리
                            try:
                                deal_price_string = data["complexPyeongDetailList"][i]["articleStatistics"]["rentPriceString"]
                                if "~" in deal_price_string:
                                    min_deal_price, max_deal_price = deal_price_string.split("~")
                                    temp_data.loc[i, "최소_실거래가"] = min_deal_price.strip()
                                    temp_data.loc[i, "최대_실거래가"] = max_deal_price.strip()
                                else:
                                    temp_data.loc[i, "최대_실거래가"] = deal_price_string.strip()
                            except KeyError:
                                pass
                                
                            # 학교 정보
                            try:
                                temp_data.loc[i,"초등학교_학군정보"] = data['schools'][0]["schoolName"]
                            except KeyError:
                                temp_data.loc[i,"초등학교_학군정보"] = ""
                            except IndexError :
                                temp_data.loc[i,"초등학교_학군정보"] = ""
                            try:
                                temp_data.loc[i,"초등학교_설립정보"] = data['schools'][0]["organizationType"]
                            except KeyError:
                                temp_data.loc[i,"초등학교_설립정보"] = ""
                            except IndexError :
                                temp_data.loc[i,"초등학교_설립정보"] = ""
                            try:
                                temp_data.loc[i,"초등학교_남학생수"] = data['schools'][0]["maleStudentCount"]
                            except KeyError:
                                temp_data.loc[i,"초등학교_남학생수"] = ""
                            except IndexError :
                                temp_data.loc[i,"초등학교_남학생수"] = ""
                            try:
                                temp_data.loc[i,"초등학교_여학생수"] = data['schools'][0]["femaleStudentCount"]
                            except KeyError:
                                temp_data.loc[i,"초등학교_여학생수"] = ""
                            except IndexError :
                                temp_data.loc[i,"초등학교_여학생수"] = ""


                        # temp_data를 all_data에 추가
                        all_data.append(temp_data)
                        # 크롤링 요청 간격 조절
                        # delay_request()
                        pbar_apt.set_postfix(current_apt=apt['complexName'], refresh=False)

            
            # 모든 아파트 데이터를 하나의 DataFrame으로 합치고 CSV 파일로 저장
            if all_data:
                final_data = pd.concat(all_data)
            
                # CSV 파일로 저장
                csv_filename = f'{dong_name}.csv'
                csv_path = os.path.join(gungu_dir, csv_filename)
                final_data.to_csv(csv_path, encoding="CP949")
            else:
                print("No data to save.")