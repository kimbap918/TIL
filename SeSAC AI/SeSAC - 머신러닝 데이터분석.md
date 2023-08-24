2023.08.24

<br>

Andrew Ng 

https://www.coursera.org/instructor/andrewng

<br>

서비스 모델을 만들 때 필요한것
* input data의 형식 : 입력이 무엇인가?
* output data의 형식  : 출력으로 무엇이 나올것인가?
* post function 

CRISP-DM의 단계에서 고려해봐야할것
1. 비즈니스 이해
* problem scoping : 윤리적으로 해도 되는것인가?

## 3-2 선형 회귀
###  k-최근접 이웃의 한계
``` python
import numpy as np

perch_length = np.array(
    [8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0,
     21.0, 21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5,
     22.5, 22.7, 23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5,
     27.3, 27.5, 27.5, 27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0,
     36.5, 36.0, 37.0, 37.0, 39.0, 39.0, 39.0, 40.0, 40.0, 40.0,
     40.0, 42.0, 43.0, 43.0, 43.5, 44.0]
     )
perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )
```
``` python
from sklearn.model_selection import train_test_split

# 훈련 세트와 테스트 세트로 나눕니다
train_input, test_input, train_target, test_target = train_test_split(
    perch_length, perch_weight, random_state=42)
# 훈련 세트와 테스트 세트를 2차원 배열로 바꿉니다
train_input = train_input.reshape(-1, 1)
test_input = test_input.reshape(-1, 1)
```
``` python
from sklearn.neighbors import KNeighborsRegressor

knr = KNeighborsRegressor(n_neighbors=3)
# k-최근접 이웃 회귀 모델을 훈련합니다
knr.fit(train_input, train_target)
```
``` python
print(knr.predict([[50]]))
-> [1033.33333333]
```
``` python
import matplotlib.pyplot as plt

# 50cm 농어의 이웃을 구합니다
distances, indexes = knr.kneighbors([[50]])

# 훈련 세트의 산점도를 그립니다
plt.scatter(train_input, train_target)
# 훈련 세트 중에서 이웃 샘플만 다시 그립니다
plt.scatter(train_input[indexes], train_target[indexes], marker='D')
# 50cm 농어 데이터
plt.scatter(50, 1033, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAkQAAAGwCAYAAABIC3rIAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA72UlEQVR4nO3de3xU5YH/8e8k5MItExJJJpGIEUSI4SIgGC9oS5RYzEpl21JBaOUHlYKKiBW8IVqMslUraqFWV9aiq3XXW3DNSrHAqpFgIEiIRcTUoGYSJTIJ0ASYOb8/4owZksAkmVvmfN6v17wg5zyZeR5Pec23z9ViGIYhAAAAE4sKdQUAAABCjUAEAABMj0AEAABMj0AEAABMj0AEAABMj0AEAABMj0AEAABMr0eoK9AduFwuffXVV+rbt68sFkuoqwMAAHxgGIYaGhqUnp6uqKiT9wERiHzw1VdfKSMjI9TVAAAAnbB//34NGDDgpGUIRD7o27evpOb/oAkJCSGuDQAA8EV9fb0yMjI83+MnQyDygXuYLCEhgUAEAEA348t0FyZVAwAA0yMQAQAA0yMQAQAA0yMQAQAA0yMQAQAA0yMQAQAA0yMQAQAA0yMQAQDgK+exUNcAAUIgAgDAF9v/LD2Q3vwnIg47VQMATMXpMlRSWafahkal9I3XuMwkRUedfCdjV+lzshTeJMmQ3rhRhmEoaszM4FQYQUEgAgCYRlF5tZYXVqja0ei5lmaN17L8LOVlp7X5O7sKn1B26Z2SIVkszSeoWwpv1K6v6jU8f0Gwqo4AY8gMAGAKReXVmrduu1cYkiS7o1Hz1m1XUXl1q9/ZVfiEzv3w+zAkffenIZ374Z3aVfhEEGqOYCAQAQAintNlaHlhhYw27rmvLS+skNP1fQlX6XPKLr1TFn0fhtwsFskiKbv0TrlKnwtQrRFMBCIAQMQrqaxr1TPUkiGp2tGoksq65gvb/9w8Z8hoHYbc3D1FlsKbmGgdAQhEAICIV9vQfhhqVc55THpzkSSj3TDk1nzfaC7PkvxujUAEAIh4KX3jfS8XHSNNfkSSRUZbY2wtNN+3NJePjulqNRFCBCIAQMQbl5mkNGu82uvwsah5tdm4zKTmC6Ovk5G/SrKo3VBkGM2/aOSvkkZfF4BaI5gIRACAiBcdZdGy/CxJahWK3D8vy8/y2o8oasxMlY9ZIUOtQ5FhNM87Kh+zgv2IIgSBCABgCnnZaVo9Y7RsVu/hM5s1XqtnjG5zH6Lh+Qu0e+wKr54id8/Q7rEr2IcoglgM41QjpKivr5fVapXD4VBCQkKoqwMA6IIu71Qti4z8VfQMdQMd+f5mp2oAgKlER1mUMyi5Q78TNWZm85KyNxdJkx+RhTlDEYdABACAL0ZfJ42cxmqyCMUcIgAAfEUYilgEIgAAYHoEIgAAYHoEIgAAYHoEIgAAYHoEIgAAYHoEIgAAYHoEIgAAYHoEIgAAEFKGYaj8m3KF8jQxAhEAAAip9Z+t18/f/LnWf7Y+ZHUgEAEAgJA57jquJ8uelCT9oewPOu46HpJ6EIgAAEDIvFX5lr489KUk6YtDX+ityrdCUg8CEQAACAl375BFFkmSRZaQ9RIRiAAAQEi4e4cMNU+mNmSErJeIQAQACCtOl6HifQf0etmXKt53QE5X6FYeIXBO7B1yC1UvUY+gfhoAACdRVF6t5YUVqnY0eq6lWeO1LD9LedlpIawZ/K3l3KGWWvYS5Q/KD1p96CECAISFovJqzVu33SsMSZLd0ah567arqLw6RDVrwXkssOVNor3eIbdQ9BIRiAAAIed0GVpeWKG2Bsfc15YXVoR2+Gz7n6UH0pv/DER5E9lRu8Nr7tCJ3L1EO2p3BK1ODJkBAEKupLKuVc9QS4akakejSirrlDMoOXgV+46r9DlZCm9qrskbN8owDEWNmem38mYzsv9I/e7S3+mo82i7ZWKjYzWy/8ig1YlABAAIudqG9sNQZ8r5067CJ5RdeqdkSBZL8zETlsIbteureg3PX9Dl8mYUGx2rSWdOCnU1vIR0yGzLli3Kz89Xenq6LBaLXnvtNa/7hmHonnvuUVpamnr27Knc3Fzt3bvXq0xdXZ2mT5+uhIQEJSYmavbs2Tp06JBXmY8++kiXXHKJ4uPjlZGRoZUrVwa6aQCADkjpG+/Xcv6yq/AJnfvh9+FG+u5PQzr3wzu1q/CJLpVH+AhpIDp8+LBGjhypJ598ss37K1eu1KpVq7RmzRpt3bpVvXv31qRJk9TY+P3/Q5g+fbp2796tDRs2aP369dqyZYvmzp3ruV9fX68rrrhCAwcOVGlpqf7t3/5N9957r5566qmAtw8A4JtxmUlKs8a3M8VWsqh5tdm4zKSg1clV+pyyS++URd+HG099LM11yi69U67S5zpVHuHFYoTyaNkWLBaLXn31VU2ZMkVSc+9Qenq6br31Vi1evFiS5HA4lJqaqrVr12ratGn6+OOPlZWVpW3btmns2LGSpKKiIv3oRz/SF198ofT0dK1evVp33nmn7Ha7YmNjJUlLlizRa6+9pr///e9t1qWpqUlNTU2en+vr65WRkSGHw6GEhIQA/lcAAPNyrzKT5DXV1p0tVs8YHbyl99v/LOONGyXDaBVuWjIMSRaLLKOulVH2gu/l/+VxafR1/q41TlBfXy+r1erT93fYrjKrrKyU3W5Xbm6u55rVatX48eNVXFwsSSouLlZiYqInDElSbm6uoqKitHXrVk+ZCRMmeMKQJE2aNEl79uzRt99+2+ZnFxQUyGq1el4ZGRmBaCIAoIW87DStnjFaNqv3sJjNGh/cMOQ8Jr25SNLJw43k7gkypLLnO1b+zUUsyQ8zYTup2m63S5JSU1O9rqempnru2e12paSkeN3v0aOHkpKSvMpkZma2eg/3vX79+rX67KVLl2rRokWen909RACAwMrLTtPlWTaVVNaptqFRKX2bh8mio06RNPwpOkaa/IhndZgvPT4ada1U9oLv5Sc/0vw5CBthG4hCKS4uTnFxcaGuBgCYUnSUJSRL672Mvs6zOswwWs8JktzhRjLyV8kyZqaMjAt8L89wWdgJ2yEzm80mSaqpqfG6XlNT47lns9lUW1vrdf/48eOqq6vzKtPWe7T8DAAAThQ1ZqbKx6yQoe/CTAuG0TzPqXzMCs/+Qh0tj/AStoEoMzNTNptNGzdu9Fyrr6/X1q1blZOTI0nKycnRwYMHVVpa6inzzjvvyOVyafz48Z4yW7Zs0bFj34/VbtiwQeecc06bw2UAALgNz1+g3WNXNPfsfBdy3D09u8euaLWvUEfLI3yENBAdOnRIZWVlKisrk9Q8kbqsrExVVVWyWCxauHChfvvb3+qNN97Qrl27NHPmTKWnp3tWog0bNkx5eXmaM2eOSkpK9N5772nBggWaNm2a0tPTJUnXXnutYmNjNXv2bO3evVsvvfSSHnvsMa85QgAAtGd4/gIZ+Y9LFkvz6jeLRUb+4+2Gm46WR5gwQuhvf/uboeZeRK/XrFmzDMMwDJfLZdx9991GamqqERcXZ0ycONHYs2eP13scOHDA+PnPf2706dPHSEhIMH75y18aDQ0NXmV27txpXHzxxUZcXJxx+umnGw8++GCH6ulwOAxJhsPh6FJ7AQDdWOlzhnHfac1/BqI8/K4j399hsw9ROOvIPgYAgAjmPNax1WEdLQ+/ioh9iAAACDsdDTeEoW6DQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyPQAQAAEyvR6grAABAS06XoZLKOtU2NCqlb7zGZSYpOsoS6mohwhGIAABho6i8WssLK1TtaPRcS7PGa1l+lvKy00JYM0Q6hswAAGGhqLxa89Zt9wpDkmR3NGreuu0qKq8OUc1gBgQiAEDIOV2GlhdWyGjjnvva8sIKOV1tlQC6jkAEAAi5ksq6Vj1DLRmSqh2NKqmsC16lYCoEIgBAyNU2tB+GOlMO6CgCEQAg5FL6xvu1HNBRBCIAQMiNy0xSmjVe7S2ut6h5tdm4zKRgVgsmQiACAIRcdJRFy/KzJKlVKHL/vCw/i/2IEDAEIgBAWMjLTtPqGaNls3oPi9ms8Vo9YzT7ECGg2JgRABA28rLTdHmWjZ2qEXQEIgBAWImOsihnUHKoqwGTYcgMAACYHoEIAACYHoEIAACYHoEIAACYHpOqAQBhxekyWGWGoCMQAQDCRlF5tZYXVngd9Jpmjdey/Cz2IUJAMWQGAAgLReXVmrdue6tT7+2ORs1bt11F5dUhqhnMgEAEAGHK6TJUvO+AXi/7UsX7DsjpMkJdpYBxugwtL6xQWy10X1teWBHR/w0QWgyZAUAYMtvQUUllXaueoZYMSdWORpVU1rFpIwKCHiIACDNmHDqqbWg/DHWmHNBRBCIACCNmHTpK6Rt/6kIdKAd0FIEIAMJIR4aOIsm4zCSlWePV3uJ6i5qHDMdlJgWzWjARAhEAhBGzDh1FR1m0LD9LklqFIvfPy/Kz2I8IAUMgAoAwEmlDRx1ZKZeXnabVM0bLZvVum80ar9UzRkfkZHKED1aZAUAYcQ8d2R2Nbc4jsqg5IHSHoaPOrJTLy07T5Vk2dqpG0NFDBABhJFKGjrqyUi46yqKcQcm6etTpyhmUHPZtRWQgEAFAmOnuQ0dmXSmH7o0hMwAIQ9156IhNFtEdEYgAIEy5h466G7OulEP3xpAZAMCvIm2lHMyBQAQA8Cs2WUR3FNaByOl06u6771ZmZqZ69uypQYMG6f7775dhfD8RzzAM3XPPPUpLS1PPnj2Vm5urvXv3er1PXV2dpk+froSEBCUmJmr27Nk6dOhQsJsDAKYQKSvlYC5hHYgeeughrV69Wk888YQ+/vhjPfTQQ1q5cqUef/xxT5mVK1dq1apVWrNmjbZu3arevXtr0qRJamz8fmx6+vTp2r17tzZs2KD169dry5Ytmjt3biiaBACm0N1XysF8LEbL7pYwc9VVVyk1NVXPPPOM59rUqVPVs2dPrVu3ToZhKD09XbfeeqsWL14sSXI4HEpNTdXatWs1bdo0ffzxx8rKytK2bds0duxYSVJRUZF+9KMf6YsvvlB6enqrz21qalJTU5Pn5/r6emVkZMjhcCghISHArQaAyOF0Gd1ypRwiQ319vaxWq0/f32HdQ3ThhRdq48aN+uSTTyRJO3fu1Lvvvqsrr7xSklRZWSm73a7c3FzP71itVo0fP17FxcWSpOLiYiUmJnrCkCTl5uYqKipKW7dubfNzCwoKZLVaPa+MjIxANREAIhqbLKK7COtl90uWLFF9fb2GDh2q6OhoOZ1OrVixQtOnT5ck2e12SVJqaqrX76Wmpnru2e12paSkeN3v0aOHkpKSPGVOtHTpUi1atMjzs7uHCAAARKawDkR/+ctf9Pzzz+uFF17Queeeq7KyMi1cuFDp6emaNWtWwD43Li5OcXFxAXt/AAAQXsI6EN12221asmSJpk2bJkkaPny4Pv/8cxUUFGjWrFmy2WySpJqaGqWlfT9Br6amRqNGjZIk2Ww21dbWer3v8ePHVVdX5/l9AABgbmE9h+jIkSOKivKuYnR0tFwulyQpMzNTNptNGzdu9Nyvr6/X1q1blZOTI0nKycnRwYMHVVpa6inzzjvvyOVyafz48UFoBQAACHdh3UOUn5+vFStW6IwzztC5556rHTt26JFHHtH1118vSbJYLFq4cKF++9vf6uyzz1ZmZqbuvvtupaena8qUKZKkYcOGKS8vT3PmzNGaNWt07NgxLViwQNOmTWtzhRkAADCfsA5Ejz/+uO6++279+te/Vm1trdLT0/WrX/1K99xzj6fMb37zGx0+fFhz587VwYMHdfHFF6uoqEjx8d/vffH8889rwYIFmjhxoqKiojR16lStWrUqFE0CAABhKKz3IQoXHdnHAAAAhIeI2YcIAAAgGAhEAADA9AhEAADA9AhEAADA9AhEAADA9AhEAADA9AhEAADA9AhEAADA9AhEAADA9AhEAADA9AhEAADA9AhEAADA9AhEAADA9AhEAADA9AhEAADA9AhEAADA9AhEAADA9AhEAADA9AhEAADA9HqEugIAAP9wugyVVNaptqFRKX3jNS4zSdFRFr+VByIZgQgAIkBRebWWF1ao2tHouZZmjdey/CzlZad1uTwQ6RgyA4Burqi8WvPWbfcKN5JkdzRq3rrtKiqv7lJ5wAwIRADQjTldhpYXVsho45772vLCCjldRqfKA2bBkBkAdGMllXWtenpaMiRVOxq19r1KndY3Tt80NPlUvqSyTjmDkv1fYSBMEYgAoBurbWg/3LR0/5sfB+R9gUjBkBkAdGMpfeMD8r6n9YkLyPsC4YpABADd2LjMJKVZ4+X3xfJMIYLJEIgAoBuLjrJoWX6WJPk1FH1zuMmP7waEPwIRAHRzedlpWj1jtGxW/w2fBWooDghXTKoGgAiQl52my7Nsnp2nv2lo6vBEaqm5l8lmbd61GjATAhEARIjoKItnqbzTZejpdytldzT6PB3IPeS2LD+LIzxgOgyZAUAEOtncIvfPib1ivK7brPFaPWM0R3fAlOghAoAI5Z5bdOKZZbbvzixrOcTG4a4wO4thGCyuPIX6+npZrVY5HA4lJCSEujoA0CGcag+z6sj3Nz1EABDhWs4tCjbCGLoLAhEAICCKyqtbDdelfTdcxzwlhBsmVQMA/K6ovFrz1m1vdZCs3dGoeeu2q6i8OkQ1A9pGIAIA+JXTZWh5YUWby/3d15YXVsjpYgorwgeBCADgVyWVda16hloyJFU7GlVSWRe8SgGnQCACAPhVbUP7Yagz5YBgIBABAPzK13PQOC8N4YRABADwq3GZSUqzxrfaIdvNoubVZpyXhnBCIAIA+JUvx4ZwXhrCDYEIAOB37mNDbFbvYTHOS0O4YmNGAEBA5GWncV4auo1O9RDdd999OnLkSKvr//znP3Xfffd1uVIAgMjgPjbk6lGnK2dQMmEIYatTh7tGR0erurpaKSkpXtcPHDiglJQUOZ1Ov1UwHHC4KwAA3U9Hvr871UNkGIYsltYpf+fOnUpKYtUAAADoXjo0h6hfv36yWCyyWCwaMmSIVyhyOp06dOiQbrjhBr9XEgAAIJA6FIh+//vfyzAMXX/99Vq+fLmsVqvnXmxsrM4880zl5OT4vZIAAACB1KFANGvWLElSZmamLrzwQsXExASkUgAAAMHUqWX3l156qVwulz755BPV1tbK5XJ53Z8wYYJfKgcAABAMnZpU/cEHH2jw4MEaNmyYJkyYoMsuu8zz+sEPfuDXCn755ZeaMWOGkpOT1bNnTw0fPlwffvih575hGLrnnnuUlpamnj17Kjc3V3v37vV6j7q6Ok2fPl0JCQlKTEzU7NmzdejQIb/WEwAAdF+dCkQ33HCDxo4dq/LyctXV1enbb7/1vOrq6vxWuW+//VYXXXSRYmJi9NZbb6miokIPP/yw+vXr5ymzcuVKrVq1SmvWrNHWrVvVu3dvTZo0SY2N35+iPH36dO3evVsbNmzQ+vXrtWXLFs2dO9dv9QQAAN1bp/Yh6t27t3bu3KnBgwcHok4eS5Ys0Xvvvaf/+7//a/O+YRhKT0/XrbfeqsWLF0uSHA6HUlNTtXbtWk2bNk0ff/yxsrKytG3bNo0dO1aSVFRUpB/96Ef64osvlJ6e3up9m5qa1NTU5Pm5vr5eGRkZ7EMEAEA3EvB9iMaPH69PP/20U5XriDfeeENjx47VT37yE6WkpOi8887Tn/70J8/9yspK2e125ebmeq5ZrVaNHz9excXFkqTi4mIlJiZ6wpAk5ebmKioqSlu3bm3zcwsKCmS1Wj2vjIyMALUQAACEA58nVX/00Ueev99444269dZbZbfbNXz48FarzUaMGOGXyn322WdavXq1Fi1apDvuuEPbtm3TTTfdpNjYWM2aNUt2u12SlJqa6vV7qampnnt2u73Vjto9evRQUlKSp8yJli5dqkWLFnl+dvcQAQCAyORzIBo1apQsFotajrBdf/31nr+771ksFr8d3eFyuTR27Fg98MADkqTzzjtP5eXlWrNmjWcLgECIi4tTXFxcwN4fAACEF58DUWVlZSDr0aa0tDRlZWV5XRs2bJj++7//W5Jks9kkSTU1NUpLS/OUqamp0ahRozxlamtrvd7j+PHjqqur8/w+AAAwN58D0cCBAwNZjzZddNFF2rNnj9e1Tz75xFOXzMxM2Ww2bdy40ROA6uvrtXXrVs2bN0+SlJOTo4MHD6q0tFRjxoyRJL3zzjtyuVwaP3588BoDAADCVqc2ZnzjjTfavG6xWBQfH6/BgwcrMzOzSxWTpFtuuUUXXnihHnjgAf30pz9VSUmJnnrqKT311FOez1u4cKF++9vf6uyzz1ZmZqbuvvtupaena8qUKZKae5Ty8vI0Z84crVmzRseOHdOCBQs0bdq0NleYAQAA8+nUsvuoqKhW84kk73lEF198sV577TWvPYM6Y/369Vq6dKn27t2rzMxMLVq0SHPmzPHcNwxDy5Yt01NPPaWDBw/q4osv1h/+8AcNGTLEU6aurk4LFixQYWGhoqKiNHXqVK1atUp9+vTxqQ4dWbYHAADCQ0e+vzsViDZu3Kg777xTK1as0Lhx4yRJJSUluvvuu3XXXXfJarXqV7/6lcaPH69nnnmmc60IIwQiAAC6n458f3dqyOzmm2/WU089pQsvvNBzbeLEiYqPj9fcuXO1e/du/f73v/dahQYAABCuOhWI9u3b12bSSkhI0GeffSZJOvvss/XNN990rXYAEOGcLkMllXWqbWhUSt94jctMUnSUJdTVAkynU4FozJgxuu222/Tcc8+pf//+kqSvv/5av/nNb3T++edLkvbu3ctmhgBwEkXl1VpeWKFqx/dnL6ZZ47UsP0t52Wkn+U0A/tapozueeeYZVVZWasCAARo8eLAGDx6sAQMG6B//+IeefvppSdKhQ4d01113+bWyABApisqrNW/ddq8wJEl2R6PmrduuovLqENUMMKdOTaqWmneRfvvtt/XJJ59Iks455xxdfvnliorqVMYKa0yqBuBPTpehix96p1UYcrNIslnj9e7tP2T4DOiCgE+qlpqX3ufl5SkvL6+zbwEAplRSWdduGJIkQ1K1o1EllXXKGZQcvIoBJuZzIFq1apXmzp2r+Ph4rVq16qRlb7rppi5XDAAiVW1D+2GoM+UAdJ3PgejRRx/V9OnTFR8fr0cffbTdchaLhUAEACeR0jfer+UAdF2nDncNxUGvABApxmUmKc0aL7ujUW1N4nTPIRqXmRTsqgGm1aUZ0EePHtWePXt0/Phxf9UHACJedJRFy/KzJDWHn5bcPy/Lz2JCNRBEnQpER44c0ezZs9WrVy+de+65qqqqkiTdeOONevDBB/1aQQCIRHnZaVo9Y7RsVu9hMZs1XqtnjGYfIiDIOrXKbOnSpdq5c6c2bdrktcosNzdX9957r5YsWeK3CgJApMrLTtPlWTZ2qgbCQKcC0WuvvaaXXnpJF1xwgSyW7//hnnvuudq3b5/fKgcAkS46ysLSeiAMdGrI7Ouvv1ZKSkqr64cPH/YKSAAAAN1BpwLR2LFj9eabb3p+doegp59+Wjk5Of6pGQCEGafLUPG+A3q97EsV7zsgp6tTG/0DCEOdGjJ74IEHdOWVV6qiokLHjx/XY489poqKCr3//vvavHmzv+sIACHHQaxAZOtUD9HFF1+snTt36vjx4xo+fLjefvttpaSkqLi4WGPGjPF3HQEgpDiIFYh8neohmjlzpn7wgx9oyZIlGjRokL/rBABhw+kytLywos0NFA017xu0vLBCl2fZWB0GdGOd6iGKjY1VQUGBhgwZooyMDM2YMUNPP/209u7d6+/6AUBIdeQgVgDdV6cC0dNPP61PPvlEVVVVWrlypfr06aOHH35YQ4cO1YABA/xdRwAIGQ5iBcyhS0d39OvXT8nJyerXr58SExPVo0cP9e/f3191A4CQ4yBWwBw6FYjuuOMOXXjhhUpOTtaSJUvU2NioJUuWyG63a8eOHf6uIwCEjPsg1vZmB1nUvNqMg1iB7s1iGEaHN9KIiopS//79dcstt+iaa67RkCFDAlG3sFFfXy+r1SqHw6GEhIRQVwdAkLlXmUnymlztDkmcPQaEp458f3eqh2jHjh268847VVJSoosuukinn366rr32Wj311FP65JNPOlVpAAhXHMQKRL5O9RCdaOfOnXr00Uf1/PPPy+Vyyel0+qNuYYMeIgBS8xJ8DmIFuo+OfH93ah8iwzC0Y8cObdq0SZs2bdK7776r+vp6jRgxQpdeemmnKg0A4Y6DWIHI1alAlJSUpEOHDmnkyJG69NJLNWfOHF1yySVKTEz0c/UAAAACr1OBaN26dbrkkksYPgIAABGhU4Fo8uTJ/q4HAABAyHRpY0YAAIBIQCACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACmRyACAACm160C0YMPPiiLxaKFCxd6rjU2Nmr+/PlKTk5Wnz59NHXqVNXU1Hj9XlVVlSZPnqxevXopJSVFt912m44fPx7k2gMAgHDVbQLRtm3b9Mc//lEjRozwun7LLbeo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ubi4OC1btsx0O2vTbtptFmZtO+2m3cHGpGoAAGB69BABAADTIxABAADTIxABAADTIxABAADTIxB1E1u2bFF+fr7S09NlsVj02muved3/xS9+IYvF4vXKy8sLTWX9pKCgQOeff7769u2rlJQUTZkyRXv27PEq09jYqPnz5ys5OVl9+vTR1KlTVVNTE6Ia+48vbb/ssstaPfMbbrghRDX2j9WrV2vEiBGezdlycnL01ltvee5H6vM+Vbsj8Vm35cEHH5TFYtHChQs91yL1mbfUVrsj8Znfe++9rdo0dOhQz/1QP2sCUTdx+PBhjRw5Uk8++WS7ZfLy8lRdXe15/ed//mcQa+h/mzdv1vz58/XBBx9ow4YNOnbsmK644godPnzYU+aWW25RYWGhXn75ZW3evFlfffWVrrnmmhDW2j98abskzZkzx+uZr1y5MkQ19o8BAwbowQcfVGlpqT788EP98Ic/1NVXX63du3dLitznfap2S5H3rE+0bds2/fGPf9SIESO8rkfqM3drr91SZD7zc88916tN7777rudeyJ+1gW5HkvHqq696XZs1a5Zx9dVXh6Q+wVJbW2tIMjZv3mwYhmEcPHjQiImJMV5++WVPmY8//tiQZBQXF4eqmgFxYtsNwzAuvfRS4+abbw5dpYKkX79+xtNPP22q520Y37fbMCL/WTc0NBhnn322sWHDBq+2Rvozb6/dhhGZz3zZsmXGyJEj27wXDs+aHqIIsmnTJqWkpOicc87RvHnzdODAgVBXya8cDockKSkpSZJUWlqqY8eOKTc311Nm6NChOuOMM1RcXBySOgbKiW13e/7553XaaacpOztbS5cu1ZEjR0JRvYBwOp168cUXdfjwYeXk5JjmeZ/YbrdIftbz58/X5MmTvZ6tFPn/xttrt1skPvO9e/cqPT1dZ511lqZPn66qqipJ4fGsOdw1QuTl5emaa65RZmam9u3bpzvuuENXXnmliouLFR0dHerqdZnL5dLChQt10UUXKTs7W5Jkt9sVGxurxMREr7Kpqamy2+0hqGVgtNV2Sbr22ms1cOBApaen66OPPtLtt9+uPXv26JVXXglhbbtu165dysnJUWNjo/r06aNXX31VWVlZKisri+jn3V67pch91pL04osvavv27dq2bVure5H8b/xk7ZYi85mPHz9ea9eu1TnnnKPq6motX75cl1xyicrLy8PiWROIIsS0adM8fx8+fLhGjBihQYMGadOmTZo4cWIIa+Yf8+fPV3l5udd4s1m01/a5c+d6/j58+HClpaVp4sSJ2rdvnwYNGhTsavrNOeeco7KyMjkcDv3Xf/2XZs2apc2bN4e6WgHXXruzsrIi9lnv379fN998szZs2KD4+PhQVydofGl3JD7zK6+80vP3ESNGaPz48Ro4cKD+8pe/qGfPniGsWTOGzCLUWWedpdNOO02ffvppqKvSZQsWLND69ev1t7/9TQMGDPBct9lsOnr0qA4ePOhVvqamRjabLci1DIz22t6W8ePHS1K3f+axsbEaPHiwxowZo4KCAo0cOVKPPfZYxD/v9trdlkh51qWlpaqtrdXo0aPVo0cP9ejRQ5s3b9aqVavUo0cPpaamRuQzP1W7nU5nq9+JlGfeUmJiooYMGaJPP/00LP59E4gi1BdffKEDBw4oLS0t1FXpNMMwtGDBAr366qt65513lJmZ6XV/zJgxiomJ0caNGz3X9uzZo6qqKq+5F93RqdrelrKyMknq1s+8LS6XS01NTRH9vNvibndbIuVZT5w4Ubt27VJZWZnnNXbsWE2fPt3z90h85qdqd1vTHCLlmbd06NAh7du3T2lpaeHx7zsoU7fRZQ0NDcaOHTuMHTt2GJKMRx55xNixY4fx+eefGw0NDcbixYuN4uJio7Ky0vjrX/9qjB492jj77LONxsbGUFe90+bNm2dYrVZj06ZNRnV1ted15MgRT5kbbrjBOOOMM4x33nnH+PDDD42cnBwjJycnhLX2j1O1/dNPPzXuu+8+48MPPzQqKyuN119/3TjrrLOMCRMmhLjmXbNkyRJj8+bNRmVlpfHRRx8ZS5YsMSwWi/H2228bhhG5z/tk7Y7UZ92eE1dXReozP1HLdkfqM7/11luNTZs2GZWVlcZ7771n5ObmGqeddppRW1trGEbonzWBqJv429/+Zkhq9Zo1a5Zx5MgR44orrjD69+9vxMTEGAMHDjTmzJlj2O32UFe7S9pqryTj2Wef9ZT55z//afz61782+vXrZ/Tq1cv48Y9/bFRXV4eu0n5yqrZXVVUZEyZMMJKSkoy4uDhj8ODBxm233WY4HI7QVryLrr/+emPgwIFGbGys0b9/f2PixImeMGQYkfu8T9buSH3W7TkxEEXqMz9Ry3ZH6jP/2c9+ZqSlpRmxsbHG6aefbvzsZz8zPv30U8/9UD9ri2EYRnD6ogAAAMITc4gAAIDpEYgAAIDpEYgAAIDpEYgAAIDpEYgAAIDpEYgAAIDpEYgAAIDpEYgAAIDpEYgAdDuXXXaZFi5cGOpqaNOmTbJYLK0OpATQ/RCIAMAH4RLCAAQGgQgAAJgegQhAt9bU1KTFixfr9NNPV+/evTV+/Hht2rTJc3/t2rVKTEzU//7v/2rYsGHq06eP8vLyVF1d7Slz/Phx3XTTTUpMTFRycrJuv/12zZo1S1OmTJEk/eIXv9DmzZv12GOPyWKxyGKx6B//+Ifn90tLSzV27Fj16tVLF154ofbs2ROk1gPwFwIRgG5twYIFKi4u1osvvqiPPvpIP/nJT5SXl6e9e/d6yhw5ckS/+93v9Oc//1lbtmxRVVWVFi9e7Ln/0EMP6fnnn9ezzz6r9957T/X19Xrttdc89x977DHl5ORozpw5qq6uVnV1tTIyMjz377zzTj388MP68MMP1aNHD11//fVBaTsA/+kR6goAQGdVVVXp2WefVVVVldLT0yVJixcvVlFRkZ599lk98MADkqRjx45pzZo1GjRokKTmEHXfffd53ufxxx/X0qVL9eMf/1iS9MQTT+h//ud/PPetVqtiY2PVq1cv2Wy2VvVYsWKFLr30UknSkiVLNHnyZDU2Nio+Pj4wDQfgdwQiAN3Wrl275HQ6NWTIEK/rTU1NSk5O9vzcq1cvTxiSpLS0NNXW1kqSHA6HampqNG7cOM/96OhojRkzRi6Xy6d6jBgxwuu9Jam2tlZnnHFGxxsFICQIRAC6rUOHDik6OlqlpaWKjo72utenTx/P32NiYrzuWSwWGYbht3q0fH+LxSJJPocpAOGBOUQAuq3zzjtPTqdTtbW1Gjx4sNerraGttlitVqWmpmrbtm2ea06nU9u3b/cqFxsbK6fT6df6Awgf9BAB6LaGDBmi6dOna+bMmXr44Yd13nnn6euvv9bGjRs1YsQITZ482af3ufHGG1VQUKDBgwdr6NChevzxx/Xtt996ensk6cwzz9TWrVv1j3/8Q3369FFSUlKgmgUgBOghAtCtPfvss5o5c6ZuvfVWnXPOOZoyZYq2bdvWofk7t99+u37+859r5syZysnJUZ8+fTRp0iSvSdGLFy9WdHS0srKy1L9/f1VVVQWiOQBCxGL4cyAdACKAy+XSsGHD9NOf/lT3339/qKsDIAgYMgNgep9//rnefvttXXrppWpqatITTzyhyspKXXvttaGuGoAgYcgMgOlFRUVp7dq1Ov/883XRRRdp165d+utf/6phw4aFumoAgoQhMwAAYHr0EAEAANMjEAEAANMjEAEAANMjEAEAANMjEAEAANMjEAEAANMjEAEAANMjEAEAANP7/1hYCorWMVVTAAAAAElFTkSuQmCC)

선형회귀는 오차 베이스
* 2차원 평면에서 직선은 몇개나 그릴 수 있을까? -> 무한대를 그릴 수 있다.
* 그렇다면 선형회귀는 원본 데이터와 가장 오차가 작은 직선을 그리는것
![](https://i.imgur.com/2S7b7P7.png)
위의 분홍색 선은 검정색 선보다 원본 데이터를 더 잘 나타내고 있다고 볼수 있다.

<br>


``` python
# 50센치 물고기의 가장 가까운 3 물고기의 평균 무게
print(np.mean(train_target[indexes]))
# -> 1033.3333333333333

print(knr.predict([[100]]))
# -> [1033.33333333]
# -> 문제가 있다. 그렇다면?
```
``` python
# 100cm 농어의 이웃을 구합니다
distances, indexes = knr.kneighbors([[100]])

# 훈련 세트의 산점도를 그립니다
plt.scatter(train_input, train_target)
# 훈련 세트 중에서 이웃 샘플만 다시 그립니다
plt.scatter(train_input[indexes], train_target[indexes], marker='D')
# 100cm 농어 데이터
plt.scatter(100, 1033, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```
![](https://i.imgur.com/RB1L1el.png)


<br>

### 선형 회귀

``` python
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
# 선형 회귀 모델 훈련
lr.fit(train_input, train_target)

# 50cm 농어에 대한 예측
print(lr.predict([[50]]))
# -> [1241.83860323]
```
``` pyhton
# 기울기와 절편
# 만약, 0cm짜리 물고기가 있다면, 그 물고기의 무게는 -709.01그램이다.
print(lr.coef_, lr.intercept_)
# -> [39.01714496] -709.0186449535477
```
``` python
# 훈련 세트의 산점도를 그립니다
plt.scatter(train_input, train_target)
# 15에서 50까지 1차 방정식 그래프를 그립니다
plt.plot([15, 50], [15*lr.coef_+lr.intercept_, 50*lr.coef_+lr.intercept_])
# 50cm 농어 데이터
plt.scatter(50, 1241.8, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
```
![](https://i.imgur.com/qpIYoTc.png)

<br>

``` python
print(lr.score(train_input, train_target))
print(lr.score(test_input, test_target))

# 과적합 되어있다. 곡선이라면 어떨까?
# 0.939846333997604
# 0.8247503123313558
```

<br>

### 다항 회귀
``` python
# 곡선으로 측정
# 입력값에 임의로 제곱항을 만들어 2차함수를 만든다
train_poly = np.column_stack((train_input ** 2, train_input))
test_poly = np.column_stack((test_input ** 2, test_input))
```
``` python
# 2차원 데이터
print(train_poly.shape, test_poly.shape)
# -> (42, 2) (14, 2)
```
``` python
lr = LinearRegression()
lr.fit(train_poly, train_target)

# 입력 또한 제곱을 넣어준다.
print(lr.predict([[50**2, 50]]))
# -> [1573.98423528]

print(lr.coef_, lr.intercept_)
# -> [1.01433211 -21.55792498] 116.0502107827827

  
print(lr.score(train_poly, train_target)) 
print(lr.score(test_poly, test_target))
# 0.9706807451768623
# 0.9775935108325122

```
![](https://i.imgur.com/UdmaEHY.png)

다항회귀가 선형회귀보다 훨씬 정확한데도 왜 사용하지 않을까?
1. 과적합을 피하기 위해서
2. 원본 데이터의 기하학적 특성을 파악할 수 없다. = 차원이 높아지면 우리는 볼수없기 때문에(실제 데이터를 시각화 할 수 없다)

<br>


## 3-3 특성 공학과 규제

<br>

### 데이터 준비

``` python
import pandas as pd

df = pd.read_csv('https://bit.ly/perch_csv_data')

# 데이터프레임을 넘파이 행렬로 바꾼다.
perch_full = df.to_numpy()

print(perch_full)
# 물고기의 길이, 높이, 두께
[[ 8.4   2.11  1.41]
 [13.7   3.53  2.  ]
 [15.    3.82  2.43]
 [16.2   4.59  2.63]
 [17.4   4.59  2.94]
 [18.    5.22  3.32]
 [18.7   5.2   3.12]
 [19.    5.64  3.05]
 [19.6   5.14  3.04]
 [20.    5.08  2.77]
 [21.    5.69  3.56]
 [21.    5.92  3.31]
 [21.    5.69  3.67]
 [21.3   6.38  3.53]
 [22.    6.11  3.41]
 [22.    5.64  3.52]
 [22.    6.11  3.52]
 [22.    5.88  3.52]
 [22.    5.52  4.  ]
 [22.5   5.86  3.62]
 [22.5   6.79  3.62]
 [22.7   5.95  3.63]
 [23.    5.22  3.63]
 [23.5   6.28  3.72]
 [24.    7.29  3.72]
 [24.    6.38  3.82]
 [24.6   6.73  4.17]
 [25.    6.44  3.68]
 [25.6   6.56  4.24]
 [26.5   7.17  4.14]
 [27.3   8.32  5.14]
 [27.5   7.17  4.34]
 [27.5   7.05  4.34]
 [27.5   7.28  4.57]
 [28.    7.82  4.2 ]
 [28.7   7.59  4.64]
 [30.    7.62  4.77]
 [32.8  10.03  6.02]
 [34.5  10.26  6.39]
 [35.   11.49  7.8 ]
 [36.5  10.88  6.86]
 [36.   10.61  6.74]
 [37.   10.84  6.26]
 [37.   10.57  6.37]
 [39.   11.14  7.49]
 [39.   11.14  6.  ]
 [39.   12.43  7.35]
 [40.   11.93  7.11]
 [40.   11.73  7.22]
 [40.   12.38  7.46]
 [40.   11.14  6.63]
 [42.   12.8   6.87]
 [43.   11.93  7.28]
 [43.   12.51  7.42]
 [43.5  12.6   8.14]
 [44.   12.49  7.6 ]]
```

``` python
import numpy as np

perch_weight = np.array(
    [5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0,
     110.0, 115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0,
     130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
     197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0,
     514.0, 556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0,
     820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
     1000.0, 1000.0]
     )
```
``` python
from sklearn.model_selection import train_test_split

# train_test_split default 값 75 : 25
train_input, test_input, train_target, test_target = train_test_split(perch_full, perch_weight, random_state=42)
```

<br>

### 사이킷런의 변환기

```python
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures()
poly.fit([[2, 3]])
print(poly.transform([[2, 3]]))  
# PolynomialFeatures = 임의의 값을 주면 자동으로 다항식을 만들어 준다.
# 1, 2^1, 3^1, 2^2, 2*3, 3^2
# -> [[1. 2. 3. 4. 6. 9.]]

poly = PolynomialFeatures(include_bias=False)
poly.fit([[2, 3]])
print(poly.transform([[2, 3]])) 

# -> [[2. 3. 4. 6. 9.]]

poly = PolynomialFeatures(include_bias=False)

poly.fit(train_input)
train_poly = poly.transform(train_input)

print(train_poly.shape)  

# -> (42, 9)

poly.get_feature_names_out()

test_poly = poly.transform(test_input)
```

<br>

### 다중 회귀 모델 훈련하기
``` python
from sklearn.linear_model import LinearRegression

  

lr = LinearRegression()

lr.fit(train_poly, train_target)

print(lr.score(train_poly, train_target))
# -> 0.9903183436982125
```

``` python
print(lr.score(test_poly, test_target))
# -> 0.9714559911594111
```
``` python
poly = PolynomialFeatures(degree=5, include_bias=False)

  

poly.fit(train_input)

train_poly = poly.transform(train_input)

test_poly = poly.transform(test_input)
```
``` python
print(train_poly.shape)
# -> (42, 55)
```
``` python
lr.fit(train_poly, train_target)

# 트레이닝 데이터는 거의 1에 가까운 값이 됐지만
print(lr.score(train_poly, train_target))
# -> 0.9999999999996433

# 테스트 데이터는 엉망이 됐다
# 과적합(overfitting)
# -> 그냥 직선을 써라!
print(lr.score(test_poly, test_target))
# -> -144.40579436844948
```

<br>

### 규제(regularization)
* 릿지(Ridge)
* 라쏘(Lasso)
* 두가지 다 과적합을 막는 방법이다

<br>

미분이 불가능 함수
* x값이 0일때 미분할 수 없다
* 모든 꺾이는(특이점이 있는) 함수는 미분할 수 없다

![](https://i.imgur.com/H1kUOvb.png)

https://m.blog.naver.com/alwaysneoi/100135882596

* 실제값(y)과 예측값($\widehat{y}$)의 차이 = 오차
* 오차를 구할 때 부호의 문제를 해결하려면? 절대값을 씌워야한다.
* 하지만 절대값을 사용하지 못하는 이유는 위의 이유와 같다.


### 선형회귀의 Cost function

<br>

### 평균 제곱근 오차, Root Mean Square Error, RMSE

 $\sqrt{\frac{1}{n}\sum_{i=1}^{n}((y_{i}-\widehat{y_{i}})^2)}$

1. $n$: 데이터 포인트의 개수를 나타낸다.
2. $y_{i}$: 실제 관측된 값(데이터 포인트), 여기서 $i$는 데이터 포인트의 인덱스를 나타낸다.
3. $\widehat{y_{i}}$: 모델이 예측한 값,  실제 관측된 값과 모델이 예측한 값 사이의 차이를 나타낸다.
4. $(y_{i}-\widehat{y_{i}})^2$: 각 데이터 포인트에 대한 오차의 제곱을 나타낸다. 이것은 실제 값과 예측 값의 차이를 제곱한 값이다.
5. $\sum_{i=1}^{n}$: 모든 데이터 포인트에 대해 오차 제곱을 합산하는 부분이다. $i$는 1부터 $n$까지 변화한다.
6. $\frac{1}{n}$: 데이터 포인트의 개수로 나눠줌으로써 오차 제곱의 평균을 계산한다.
7. $\sqrt{\text{...}}$: 앞서 계산한 평균 오차 제곱을 제곱근을 취해 RMSE를 계산한다. 이것은 오차의 제곱 평균의 제곱근으로, 실제 값과 예측 값 사이의 평균적인 오차 크기를 나타낸다.

<br>

### 평균 제곱 오차, Mean Square Error, MSE
* 선형회귀 모델의 예측 성능 평가 지표
* RMSE에 제곱근을 취하지 않은것

$\frac{1}{n}\sum_{i=1}^{n}((y_{i}-\widehat{y_{i}})^2)$

<br>

1. 릿지 (Ridge) 회귀: 
* 목적 함수: $\text{MSE} + \alpha \sum_{j=1}^{p} \beta_j^2$

여기서 $\text{MSE}$는 평균 제곱 오차(Mean Squared Error)를 나타내고, $\beta_j$는 모델의 가중치(weight)입니다. $\alpha$는 정규화 강도를 조절하는 매개변수로, 릿지 회귀에서는 이 값이 커질수록 가중치의 크기를 줄이는 역할을 한다.

<br>

2. 라쏘 (Lasso) 회귀: 
* 목적 함수: $\text{MSE} + \alpha \sum_{j=1}^{p} |\beta_j|$

 마찬가지로 $\text{MSE}$는 평균 제곱 오차이고, $\beta_j$는 가중치다. 라쏘 회귀에서는 가중치의 절댓값을 사용하며, $\alpha$ 역시 정규화 강도를 조절하는 매개변수로 정규화 강도를 조절한다. 라쏘는 가중치를 0으로 만들 수 있어 변수 선택의 역할을 하며, 특성 선택에 유용하다.


``` python
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_poly)

train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)
```

<br>

### 릿지(Ridge)
``` python
from sklearn.linear_model import Ridge

ridge = Ridge()
ridge.fit(train_scaled, train_target)
print(ridge.score(train_scaled, train_target))
# -> 0.9896101671037343 

print(ridge.score(test_scaled, test_target))
# -> 0.9790693977615387
```

``` python
import matplotlib.pyplot as plt

train_score = []
test_score = []
```

``` python
alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
for alpha in alpha_list:
    # 릿지 모델을 만듭니다
    ridge = Ridge(alpha=alpha)
    # 릿지 모델을 훈련합니다
    ridge.fit(train_scaled, train_target)
    # 훈련 점수와 테스트 점수를 저장합니다
    train_score.append(ridge.score(train_scaled, train_target))
    test_score.append(ridge.score(test_scaled, test_target))
```

``` python
plt.plot(np.log10(alpha_list), train_score)
plt.plot(np.log10(alpha_list), test_score)
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.show()
```
![](https://i.imgur.com/h61vGa9.png)

``` python
ridge = Ridge(alpha=0.1)
ridge.fit(train_scaled, train_target)

print(ridge.score(train_scaled, train_target))
print(ridge.score(test_scaled, test_target))
# 0.9903815817570367
# 0.9827976465386928
```

<br>

### 라쏘(Lasso)
``` python
from sklearn.linear_model import Lasso

lasso = Lasso()
lasso.fit(train_scaled, train_target)
print(lasso.score(train_scaled, train_target))
# -> 0.989789897208096

print(lasso.score(test_scaled, test_target))
# -> 0.9800593698421883
```

``` python
train_score = []
test_score = []

alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]
for alpha in alpha_list:
    # 라쏘 모델을 만듭니다
    lasso = Lasso(alpha=alpha, max_iter=10000)
    # 라쏘 모델을 훈련합니다
    lasso.fit(train_scaled, train_target)
    # 훈련 점수와 테스트 점수를 저장합니다
    train_score.append(lasso.score(train_scaled, train_target))
    test_score.append(lasso.score(test_scaled, test_target))
```

``` python
plt.plot(np.log10(alpha_list), train_score)
plt.plot(np.log10(alpha_list), test_score)
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.show()
```
![](https://i.imgur.com/7k4FySp.png)

``` python
lasso = Lasso(alpha=10)
lasso.fit(train_scaled, train_target)

print(lasso.score(train_scaled, train_target))
print(lasso.score(test_scaled, test_target))

# 0.9888067471131867
# 0.9824470598706695

print(np.sum(lasso.coef_ == 0))
# 40
```

<br>

## 로지스틱 회귀(Logistic Regression)
* 로지스틱 회귀는 '분류'다.
* 비선형적, 분류의 문제(0이냐 1이냐 등의 명목형 수치)

<br>

### 더미 변수 처리, 원핫 인코딩(GPT 참고)

**더미 변수 처리 (Dummy Variable Handling):**

더미 변수 처리는 범주형 변수를 수치형 변수로 변환하는 작업을 말합니다. 범주형 변수는 명목형이나 순서형 변수일 수 있습니다. 명목형 변수의 경우, 각 범주(category)를 0 또는 1로 인코딩하여 표현합니다. 예를 들어, "성별"이라는 범주형 변수가 있다면 "남성"을 1, "여성"을 0 또는 그 반대로 인코딩할 수 있습니다.

순서형 변수의 경우에도 마찬가지로 더미 변수 처리를 할 수 있습니다. 예를 들어, "학력"이라는 범주형 변수가 있다면 "고졸", "대학생", "석사" 등을 0 또는 1로 인코딩할 수 있습니다.

<br>

**원핫 인코딩 (One-Hot Encoding):**

원핫 인코딩은 범주형 변수의 각 범주를 이진(0 또는 1) 형태로 나타내는 방법 중 하나입니다. 각 범주에 대해 하나의 새로운 이진 변수(dummy variable)를 생성하고, 해당 범주에 해당하는 변수에 1을 할당하고 나머지 변수에는 0을 할당합니다.

예를 들어, "과일"이라는 범주형 변수가 "사과", "바나나", "딸기" 세 가지 범주를 가지고 있다면, 각각의 범주를 나타내는 세 개의 이진 변수를 생성하고 해당하는 곳에 1을 할당하고 나머지에는 0을 할당합니다. 이렇게 하면 각 과일이 해당하는 범주를 표현할 수 있습니다.

원핫 인코딩은 머신러닝 모델이 범주형 데이터를 이해하고 처리할 수 있도록 도와주며, 더미 변수와 비슷한 개념이지만 더 다양한 범주를 표현할 수 있습니다.


-> 명목형 수치들을 가중치를 가질 수 있게 바꿔주는것


### 로지스틱 함수(Logistic Function), 시그모이드 함수(Sigmoid Function)

https://ko.wikipedia.org/wiki/%EB%A1%9C%EC%A7%80%EC%8A%A4%ED%8B%B1_%ED%95%A8%EC%88%98

$f(z) = \frac{1}{1 + e^{-z}}$

* 이 로지스틱 함수의 z 자리에 선형회귀식을 넣는다
* 직선 함수를 z자리에 넣으면 곡선으로 바뀐다
* 로지스틱 함수의 값은 0에서 부터 1 사이의 값이 나온다

<br>

### 로지스틱 함수의 Cost function
$cost F = -(Plog_{e}\widehat{P})$

- $P$: 실제 관측값을 나타낸다. 이 값은 0 또는 1일 수 있으며, 각 데이터 포인트의 실제 클래스를 나타낸다.
- $\widehat{P}$: 모델의 예측 확률을 나타낸다. 이 값은 로지스틱 함수를 통해 계산된 예측 확률이며, 0과 1 사이의 값이다.
- $\log_e$: 자연 로그(natural logarithm)를 나타낸다. 자연 로그는 $e$ (2.71828...)를 밑으로 하는 로그를 의미한다.


<br>

### 럭키백의 확률

``` python
import pandas as pd

fish = pd.read_csv('https://bit.ly/fish_csv_data')
fish.head()
# 종, 무게, 길이, 직경, 높이, 두께
```
||Species|Weight|Length|Diagonal|Height|Width|
|---|---|---|---|---|---|---|
|0|Bream|242.0|25.4|30.0|11.5200|4.0200|
|1|Bream|290.0|26.3|31.2|12.4800|4.3056|
|2|Bream|340.0|26.5|31.1|12.3778|4.6961|
|3|Bream|363.0|29.0|33.5|12.7300|4.4555|
|4|Bream|430.0|29.0|34.0|12.4440|5.1340|


``` python
print(pd.unique(fish['Species'])
# 7가지 종류의 물고기
# ['Bream' 'Roach' 'Whitefish' 'Parkki' 'Perch' 'Pike' 'Smelt']
```

``` python
# 전체 중에 Species 값을 빼고 독립변수로 사용한다.
fish_input = fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()
print(fish_input[:5])

[[242. 25.4 30. 11.52 4.02 ] 
 [290. 26.3 31.2 12.48 4.3056] 
 [340. 26.5 31.1 12.3778 4.6961] 
 [363. 29. 33.5 12.73 4.4555] 
 [1. 29. 34. 12.444 5.134 ]]
```

``` python
# 실제론 글자로 되어있지만, 숫자로 만들어 처리한다
fish_target = fish['Species'].to_numpy()
```
``` python
from sklearn.model_selection import train_test_split

# 정규화를 한다.
# 모든 변수가 자신의 성질을 유지하되, 변수들 간에 비교를 할수 있게 -1에서 1사이의 값으로 바꾼다.
train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target, random_state=42)
```
``` python
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
trst_scaled = ss.transform(test_input)
```

<br>

### k-최근접 이웃 분류기의 확률 예측

``` python
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier(n_neighbors=3)
kn.fit(train_scaled, train_target)

print(kn.score(train_scaled, train_target))
print(kn.score(test_scaled, test_target))
# 0.8907563025210085 0.85
```
``` python
print(kn.classes_)
# ['Bream' 'Parkki' 'Perch' 'Pike' 'Roach' 'Smelt' 'Whitefish']

print(kn.predict(test_scaled[:5]))
# ['Perch' 'Smelt' 'Pike' 'Perch' 'Perch']
```
``` python
import numpy as np


proba = kn.predict_proba(test_scaled[:5])
print(np.round(proba, decimals=4))
# ['Bream' 'Parkki' 'Perch' 'Pike' 'Roach' 'Smelt' 'Whitefish']
[[0. 0. 1. 0. 0. 0. 0. ] # Perch 일 확률이 100%다
 [0. 0. 0. 0. 0. 1. 0. ] # Smelt 일 확률이 100%다
 [0. 0. 0. 1. 0. 0. 0. ] # Pike 일 확률이 100%다
 [0. 0. 0.6667 0. 0.3333 0. 0. ]  # Perch일 확률이 66%, Roach일 확률이 33%
 [0. 0. 0.6667 0. 0.3333 0. 0. ]]
```
``` python
# 4번째 데이터의 값을 넣었더니
distances, indexes = kn.kneighbors(test_scaled[3:4])
print(train_target[indexes])
# Roach 33% Perch 66%
# [['Roach' 'Perch' 'Perch']]
```

<br>

### 로지스틱 회귀

``` python
import numpy as np
import matplotlib.pyplot as plt

z = np.arange(-5, 5, 0.1)
phi = 1 / (1 + np.exp(-z))
# phi = 1 / (1 + np.exp(10*-z))

plt.plot(z, phi)
plt.xlabel('z')
plt.ylabel('phi')
plt.show()
```
![](https://i.imgur.com/Uwp4wnS.png)

<br>

### 로지스틱 회귀로 이진 분류 수행하기

``` python
char_arr = np.array(['A', 'B', 'C', 'D', 'E'])
print(char_arr[[True, False, True, False, False]])
# ['A', 'C']
# True 값만 출력됐다.
```
``` python
# 7종류 중 2종류의 물고기만 따로 뽑았다
bream_smelt_indexes = (train_target == 'Bream') | (train_target == 'Smelt')
train_bream_smelt = train_scaled[bream_smelt_indexes]
target_bream_smelt = train_taget[bream_smelt_indexes]
```
``` python
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(train_bream_smelt, target_bream_smelt)
```
``` python

print(lr.predict(train_bream_smelt[:5]))
# ['Bream' 'Smelt' 'Bream' 'Bream' 'Bream']

# 이진분류는 그것일 확률이 맞냐 아니냐를 뽑는다.
print(lr.predict_proba(train_bream_smelt[:5]))
[[0.99759855 0.00240145] # 99.7% 확률로 bream
 [0.02735183 0.97264817] 
 [0.99486072 0.00513928] 
 [0.98584202 0.01415798] 
 [0.99767269 0.00232731]]

print(lr.classes_)
# ['Bream' 'Smelt']

print(lr.coef_, lr.intercept_)
# [[-0.4037798 -0.57620209 -0.66280298 -1.01290277 -0.73168947]] [-2.16155132]

decisions = lr.decision_function(train_bream_smelt[:5])
print(decisions)
# [-6.02927744 3.57123907 -5.26568906 -4.24321775 -6.0607117 ]

from scipy.special import expit
print(expit(decisions))
# [0.00240145 0.97264817 0.00513928 0.01415798 0.00232731]
```

<br>

### 로지스틱 회귀로 다중 분류 수행하기

``` python
# `C`: 규제 강도를 나타내는 매개변수. 작은 값일수록 규제가 강화되며, 큰 값일수록 규제가 약화된다. 따라서 `C` 값이 20인 경우, 규제가 상대적으로 약화된 모델이 생성.

# `max_iter`: 최적화 알고리즘이 수렴하기 위한 최대 반복 횟수를 지정 1000으로 설정되어 있으므로, 최대 1000번의 반복을 통해 모델을 학습
lr = LogisticRegression(C=20, max_iter=1000)
lr.fit(train_scaled, train_target) 

print(lr.score(train_scaled, train_target))
print(lr.score(test_scaled, test_target))
# 0.9327731092436975 
# 0.925

print(lr.predict(test_scaled[:5]))
# ['Perch' 'Smelt' 'Pike' 'Roach' 'Perch']

# probability 계산
proba = lr.predict_proba(test_scaled[:5])
print(np.round(proba, decimals=3)
# softmax function을 거쳐서 아래의 값이 나온다.
# softmax function : 각 클래스에 대한 확률값을 0과 1 사이의 값으로 만들고, 모든 클래스에 대한 확률의 합이 1이 되도록 조정
[[0. 0.014 0.841 0. 0.136 0.007 0.003] # 84% 확률로 3번째 물고기
 [0. 0.003 0.044 0. 0.007 0.946 0. ] 
 [0. 0. 0.034 0.935 0.015 0.016 0. ] 
 [0.011 0.034 0.306 0.007 0.567 0. 0.076] 
 [0. 0. 0.904 0.002 0.089 0.002 0.001]]

print(lr.classes_)
# ['Bream' 'Parkki' 'Perch' 'Pike' 'Roach' 'Smelt' 'Whitefish']

# 기울기가 각각 7개의 logistic function 가중치가 5개, 절편이 7개
print(lr.coef_.shape, lr.intercept_.shape)
# (7, 5) (7,)

decision = lr.decision_function(test_scaled[:5])
print(np.round(decision, decimals=2))
[[ -6.5 1.03 5.16 -2.73 3.34 0.33 -0.63] 
 [-10.86 1.93 4.77 -2.4 2.98 7.84 -4.26] 
 [ -4.34 -6.23 3.17 6.49 2.36 2.42 -3.87] 
 [ -0.68 0.45 2.65 -1.19 3.26 -5.75 1.26] 
 [ -6.4 -1.99 5.82 -0.11 3.5 -0.11 -0.71]]
```

``` python
from scipy.special import softmax

proba = softmax(decision, axis=1)
print(np.round(proba, decimals=3))
[[0. 0.014 0.841 0. 0.136 0.007 0.003] 
 [0. 0.003 0.044 0. 0.007 0.946 0. ] 
 [0. 0. 0.034 0.935 0.015 0.016 0. ] 
 [0.011 0.034 0.306 0.007 0.567 0. 0.076] 
 [0. 0. 0.904 0.002 0.089 0.002 0.001]]
```


