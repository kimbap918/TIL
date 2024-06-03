# 상관관계 구하기
# 주어진 데이터에서 상관관계를 구하고, quality와의 상관관계가 가장 큰 값과, 가장 작은 값을 구한 다음 더하시오!
# 단, quality와 quality 상관관계 제외, 소수점 둘째 자리까지 출력

# - 데이터셋 : ../input/red-wine-quality-cortez-et-al-2009/winequality-red.csv
# - 오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
# - 스크립트 방식 권장: File -> Editor Type -> Script

import pandas as pd
import numpy as np

# 데이터 불러오기
df = pd.read_csv("../input/red-wine-quality-cortez-et-al-2009/winequality-red.csv")
#print(df.head())

# 상관관계 구하기 
df_corr = df.corr()
df_corr = df_corr[:-1] # quailiy-quailiy 상관관계 제거
# print(df_corr['quality'])

################# 풀이 수정 2022.6.21 ###################
# @b0ngb0ng 님 코드 반영

# 상관관계가 가장 큰 값과 가장 작은 값 (절대값으로 확인)
max_corr=abs(df.corr()['quality'][:-1]).max()  #0.47
min_corr=abs(df.corr()['quality'][:-1]).min()   #0.013

if max_corr not in df.corr()[['quality']][:-1].values:
    max_corr=-max_corr
if min_corr not in df.corr()[['quality']][:-1].values:
    min_corr=-min_corr
    
# 결과 출력
ans=round(max_corr+min_corr,2)
print(ans) 
# 0.49



