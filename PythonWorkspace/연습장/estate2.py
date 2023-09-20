import concurrent.futures
import requests
import json
import pandas as pd
from pprint import pprint

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

# 아파트 정보를 저장할 리스트 초기화
all_data = []

def process_apt(apt):
    apt_code = apt["complexNo"]
    data = get_apt_info(apt_code)
    temp_data = pd.DataFrame(columns=[
        "아파트명", "면적", "법정동주소", "지번주소", "도로명주소", "latitude", "longitude",
        "세대수", "임대세대수", "최고층", "최저층", "용적률", "건폐율", "주차대수",
        "건설사", "난방", "공급면적", "전용면적", "전용율", "방수", "욕실수",
        "해당면적_세대수", "현관구조", "재산세", "재산세합계", "지방교육세", "재산세_도시지역분",
        "종합부동산세", "결정세액", "농어촌특별세", "초등학교_학군정보", "초등학교_설립정보",
        "초등학교_남학생수", "초등학교_여학생수"
    ])
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
                temp_data.loc[i, "법정동주소"] = data["complexDetail"]["address"]+" "+data["complexDetail"]["roadAddress"]
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
                try:
                    temp_data.loc[i,"매매호가"] = data["complexPyeongDetailList"][i]["articleStatistics"]["dealPriceString"]
                except KeyError:   
                    temp_data.loc[i,"매매호가"] = ""
                try:
                    temp_data.loc[i,"전세호가"] = data["complexPyeongDetailList"][i]["articleStatistics"]["leasePriceString"]
                except KeyError:   
                    temp_data.loc[i,"전세호가"] = ""
                try:
                    temp_data.loc[i,"월세호가"] = data["complexPyeongDetailList"][i]["articleStatistics"]["rentPriceString"]
                except KeyError:   
                    temp_data.loc[i,"월세호가"] = ""
                try:
                    temp_data.loc[i,"실거래가"] = data["complexPyeongDetailList"][i]["articleStatistics"]["rentPriceString"]
                except KeyError:   
                    temp_data.loc[i,"실거래가"]=""
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
            pprint(temp_data)
            all_data.append(temp_data)

    return temp_data

# 최상위 지역 정보 가져오기
sido_list = get_data('https://new.land.naver.com/api/regions/list?cortarNo=0000000000')

# 아파트 정보를 병렬로 처리하여 all_data에 추가
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(process_apt, apt) for sido in sido_list["regionList"] for gungu in gungu_list["regionList"] for dong in dong_list["regionList"] for apt in apt_list["complexList"]]

    for future in concurrent.futures.as_completed(futures):
        result_data = future.result()
        all_data.append(result_data)
# 모든 아파트 데이터를 하나의 DataFrame으로 합치고 CSV 파일로 저장
final_data = pd.concat(all_data)
final_data.to_csv('all_apartments.csv', encoding="CP949")
