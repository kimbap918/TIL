# min-max스케일링 기준 상하위 5% 구하기
# 주어진 데이터에서 'f5'컬럼을 min-max 스케일 변환한 후, 상위 5%와 하위 5% 값의 합을 구하시오

# - 데이터셋 : basic1.csv
# - 오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
# - File -> Editor Type -> Script


# 라이브러리 및 데이터 불러오기
import pandas as pd
import numpy as np

df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')


# EDA
print(df.head(5))
print(df.isnull().sum())    #결측치 확인


# min-max scale 방법1
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['f5_1'] = scaler.fit_transform(df[['f5']])

# min-max scale 방법2
df['f5_2'] = df['f5'].transform(lambda x: ((x - x.min()) / (x.max() - x.min())))


# 방법1과 2 비교
print(df.head())


# 하위 5%, 상위 5% 값 구하기
lower = df['f5_1'].quantile(0.05)
print(lower)

upper = df['f5_1'].quantile(0.95)
print(upper)

print(lower + upper)