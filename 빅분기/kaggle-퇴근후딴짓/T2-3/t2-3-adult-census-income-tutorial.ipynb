{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "58f59f13",
   "metadata": {
    "papermill": {
     "duration": 0.031295,
     "end_time": "2021-12-01T23:49:30.884218",
     "exception": false,
     "start_time": "2021-12-01T23:49:30.852923",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 성인 인구조사 소득 예측\n",
    "\n",
    "- age: 나이\n",
    "- workclass: 고용 형태\n",
    "- fnlwgt: 사람의 대표성을 나타내는 가중치(final weight)\n",
    "- education: 교육 수준\n",
    "- education.num: 교육 수준 수치\n",
    "- marital.status: 결혼 상태\n",
    "- occupation: 업종\n",
    "- relationship: 가족 관계\n",
    "- race: 인종\n",
    "- sex: 성별\n",
    "- capital.gain: 양도 소득\n",
    "- capital.loss: 양도 손실\n",
    "- hours.per.week: 주당 근무 시간\n",
    "- native.country: 국적\n",
    "- income: 수익 (예측해야 하는 값)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "67ee4766",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:30.951259Z",
     "iopub.status.busy": "2021-12-01T23:49:30.950547Z",
     "iopub.status.idle": "2021-12-01T23:49:32.193084Z",
     "shell.execute_reply": "2021-12-01T23:49:32.193690Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.031045Z"
    },
    "papermill": {
     "duration": 1.281389,
     "end_time": "2021-12-01T23:49:32.193988",
     "exception": false,
     "start_time": "2021-12-01T23:49:30.912599",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((26048, 15), (6513, 15), (26048, 2), (6513, 2))"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 시험환경 세팅 (코드 변경 X)\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "def exam_data_load(df, target, id_name=\"\", null_name=\"\"):\n",
    "    if id_name == \"\":\n",
    "        df = df.reset_index().rename(columns={\"index\": \"id\"})\n",
    "        id_name = 'id'\n",
    "    else:\n",
    "        id_name = id_name\n",
    "    \n",
    "    if null_name != \"\":\n",
    "        df[df == null_name] = np.nan\n",
    "    \n",
    "    X_train, X_test = train_test_split(df, test_size=0.2, random_state=2021)\n",
    "    \n",
    "    y_train = X_train[[id_name, target]]\n",
    "    X_train = X_train.drop(columns=[target])\n",
    "\n",
    "    \n",
    "    y_test = X_test[[id_name, target]]\n",
    "    X_test = X_test.drop(columns=[target])\n",
    "    return X_train, X_test, y_train, y_test \n",
    "    \n",
    "df = pd.read_csv(\"../input/adult-census-income/adult.csv\")\n",
    "X_train, X_test, y_train, y_test = exam_data_load(df, target='income', null_name='?')\n",
    "\n",
    "X_train.shape, X_test.shape, y_train.shape, y_test.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5ba2c690",
   "metadata": {
    "papermill": {
     "duration": 0.02913,
     "end_time": "2021-12-01T23:49:32.252692",
     "exception": false,
     "start_time": "2021-12-01T23:49:32.223562",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# 사용자 코딩"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4b6c9a30",
   "metadata": {
    "papermill": {
     "duration": 0.028531,
     "end_time": "2021-12-01T23:49:32.310121",
     "exception": false,
     "start_time": "2021-12-01T23:49:32.281590",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## 라이브러리 불러오기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6e9491f6",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:32.371006Z",
     "iopub.status.busy": "2021-12-01T23:49:32.370005Z",
     "iopub.status.idle": "2021-12-01T23:49:32.373223Z",
     "shell.execute_reply": "2021-12-01T23:49:32.373784Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.135332Z"
    },
    "papermill": {
     "duration": 0.035631,
     "end_time": "2021-12-01T23:49:32.373947",
     "exception": false,
     "start_time": "2021-12-01T23:49:32.338316",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e8251af1",
   "metadata": {
    "papermill": {
     "duration": 0.027787,
     "end_time": "2021-12-01T23:49:32.429938",
     "exception": false,
     "start_time": "2021-12-01T23:49:32.402151",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## 데이터 불러오기(생략)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "38fe3f37",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:32.490914Z",
     "iopub.status.busy": "2021-12-01T23:49:32.490138Z",
     "iopub.status.idle": "2021-12-01T23:49:32.493092Z",
     "shell.execute_reply": "2021-12-01T23:49:32.493680Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.140423Z"
    },
    "papermill": {
     "duration": 0.035524,
     "end_time": "2021-12-01T23:49:32.493856",
     "exception": false,
     "start_time": "2021-12-01T23:49:32.458332",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# 시험환경에서는 아래와 같이 제공된다고 함\n",
    "# import pandas as pd\n",
    "# X_test = pd.read_csv(\"data/X_test.csv\")\n",
    "# X_train = pd.read_csv(\"data/X_train.csv\")\n",
    "# y_train = pd.read_csv(\"data/y_train.csv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e1b5b84f",
   "metadata": {
    "papermill": {
     "duration": 0.027878,
     "end_time": "2021-12-01T23:49:32.550301",
     "exception": false,
     "start_time": "2021-12-01T23:49:32.522423",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## EDA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5df01f89",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:32.611682Z",
     "iopub.status.busy": "2021-12-01T23:49:32.610980Z",
     "iopub.status.idle": "2021-12-01T23:49:32.617230Z",
     "shell.execute_reply": "2021-12-01T23:49:32.617890Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.154760Z"
    },
    "papermill": {
     "duration": 0.039399,
     "end_time": "2021-12-01T23:49:32.618185",
     "exception": false,
     "start_time": "2021-12-01T23:49:32.578786",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((26048, 15), (6513, 15), (26048, 2))"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 데이터 크기 확인\n",
    "X_train.shape, X_test.shape, y_train.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c9db0ba9",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:32.680397Z",
     "iopub.status.busy": "2021-12-01T23:49:32.679740Z",
     "iopub.status.idle": "2021-12-01T23:49:32.698910Z",
     "shell.execute_reply": "2021-12-01T23:49:32.699445Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.170992Z"
    },
    "papermill": {
     "duration": 0.051234,
     "end_time": "2021-12-01T23:49:32.699626",
     "exception": false,
     "start_time": "2021-12-01T23:49:32.648392",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>age</th>\n",
       "      <th>workclass</th>\n",
       "      <th>fnlwgt</th>\n",
       "      <th>education</th>\n",
       "      <th>education.num</th>\n",
       "      <th>marital.status</th>\n",
       "      <th>occupation</th>\n",
       "      <th>relationship</th>\n",
       "      <th>race</th>\n",
       "      <th>sex</th>\n",
       "      <th>capital.gain</th>\n",
       "      <th>capital.loss</th>\n",
       "      <th>hours.per.week</th>\n",
       "      <th>native.country</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>21851</th>\n",
       "      <td>21851</td>\n",
       "      <td>36</td>\n",
       "      <td>Private</td>\n",
       "      <td>241998</td>\n",
       "      <td>Bachelors</td>\n",
       "      <td>13</td>\n",
       "      <td>Married-civ-spouse</td>\n",
       "      <td>Craft-repair</td>\n",
       "      <td>Husband</td>\n",
       "      <td>White</td>\n",
       "      <td>Male</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>United-States</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7632</th>\n",
       "      <td>7632</td>\n",
       "      <td>53</td>\n",
       "      <td>Private</td>\n",
       "      <td>103950</td>\n",
       "      <td>Masters</td>\n",
       "      <td>14</td>\n",
       "      <td>Divorced</td>\n",
       "      <td>Prof-specialty</td>\n",
       "      <td>Not-in-family</td>\n",
       "      <td>White</td>\n",
       "      <td>Female</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>United-States</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27878</th>\n",
       "      <td>27878</td>\n",
       "      <td>19</td>\n",
       "      <td>Private</td>\n",
       "      <td>203061</td>\n",
       "      <td>Some-college</td>\n",
       "      <td>10</td>\n",
       "      <td>Never-married</td>\n",
       "      <td>Tech-support</td>\n",
       "      <td>Not-in-family</td>\n",
       "      <td>White</td>\n",
       "      <td>Female</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>25</td>\n",
       "      <td>United-States</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14121</th>\n",
       "      <td>14121</td>\n",
       "      <td>20</td>\n",
       "      <td>Private</td>\n",
       "      <td>102607</td>\n",
       "      <td>HS-grad</td>\n",
       "      <td>9</td>\n",
       "      <td>Never-married</td>\n",
       "      <td>Handlers-cleaners</td>\n",
       "      <td>Own-child</td>\n",
       "      <td>White</td>\n",
       "      <td>Male</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>30</td>\n",
       "      <td>United-States</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32345</th>\n",
       "      <td>32345</td>\n",
       "      <td>54</td>\n",
       "      <td>State-gov</td>\n",
       "      <td>138852</td>\n",
       "      <td>HS-grad</td>\n",
       "      <td>9</td>\n",
       "      <td>Married-civ-spouse</td>\n",
       "      <td>Prof-specialty</td>\n",
       "      <td>Husband</td>\n",
       "      <td>White</td>\n",
       "      <td>Male</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>United-States</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          id  age  workclass  fnlwgt     education  education.num  \\\n",
       "21851  21851   36    Private  241998     Bachelors             13   \n",
       "7632    7632   53    Private  103950       Masters             14   \n",
       "27878  27878   19    Private  203061  Some-college             10   \n",
       "14121  14121   20    Private  102607       HS-grad              9   \n",
       "32345  32345   54  State-gov  138852       HS-grad              9   \n",
       "\n",
       "           marital.status         occupation   relationship   race     sex  \\\n",
       "21851  Married-civ-spouse       Craft-repair        Husband  White    Male   \n",
       "7632             Divorced     Prof-specialty  Not-in-family  White  Female   \n",
       "27878       Never-married       Tech-support  Not-in-family  White  Female   \n",
       "14121       Never-married  Handlers-cleaners      Own-child  White    Male   \n",
       "32345  Married-civ-spouse     Prof-specialty        Husband  White    Male   \n",
       "\n",
       "       capital.gain  capital.loss  hours.per.week native.country  \n",
       "21851             0             0              50  United-States  \n",
       "7632              0             0              40  United-States  \n",
       "27878             0             0              25  United-States  \n",
       "14121             0             0              30  United-States  \n",
       "32345             0             0              40  United-States  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 데이터 확인\n",
    "X_train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "719d808a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:32.763062Z",
     "iopub.status.busy": "2021-12-01T23:49:32.762357Z",
     "iopub.status.idle": "2021-12-01T23:49:32.775779Z",
     "shell.execute_reply": "2021-12-01T23:49:32.776322Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.195139Z"
    },
    "papermill": {
     "duration": 0.046232,
     "end_time": "2021-12-01T23:49:32.776529",
     "exception": false,
     "start_time": "2021-12-01T23:49:32.730297",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<=50K    19756\n",
       ">50K      6292\n",
       "Name: income, dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 타겟 수 확인\n",
    "y_train['income'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f565e121",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:32.840626Z",
     "iopub.status.busy": "2021-12-01T23:49:32.839917Z",
     "iopub.status.idle": "2021-12-01T23:49:32.879401Z",
     "shell.execute_reply": "2021-12-01T23:49:32.880127Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.205843Z"
    },
    "papermill": {
     "duration": 0.073832,
     "end_time": "2021-12-01T23:49:32.880368",
     "exception": false,
     "start_time": "2021-12-01T23:49:32.806536",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 26048 entries, 21851 to 25716\n",
      "Data columns (total 15 columns):\n",
      " #   Column          Non-Null Count  Dtype \n",
      "---  ------          --------------  ----- \n",
      " 0   id              26048 non-null  int64 \n",
      " 1   age             26048 non-null  int64 \n",
      " 2   workclass       24592 non-null  object\n",
      " 3   fnlwgt          26048 non-null  int64 \n",
      " 4   education       26048 non-null  object\n",
      " 5   education.num   26048 non-null  int64 \n",
      " 6   marital.status  26048 non-null  object\n",
      " 7   occupation      24585 non-null  object\n",
      " 8   relationship    26048 non-null  object\n",
      " 9   race            26048 non-null  object\n",
      " 10  sex             26048 non-null  object\n",
      " 11  capital.gain    26048 non-null  int64 \n",
      " 12  capital.loss    26048 non-null  int64 \n",
      " 13  hours.per.week  26048 non-null  int64 \n",
      " 14  native.country  25587 non-null  object\n",
      "dtypes: int64(7), object(8)\n",
      "memory usage: 3.2+ MB\n"
     ]
    }
   ],
   "source": [
    "# type확인\n",
    "X_train.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a4f2f575",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:32.948523Z",
     "iopub.status.busy": "2021-12-01T23:49:32.947606Z",
     "iopub.status.idle": "2021-12-01T23:49:32.950590Z",
     "shell.execute_reply": "2021-12-01T23:49:32.950024Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.247165Z"
    },
    "papermill": {
     "duration": 0.039261,
     "end_time": "2021-12-01T23:49:32.950747",
     "exception": false,
     "start_time": "2021-12-01T23:49:32.911486",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# 피처 구분\n",
    "# Numeric features\n",
    "numeric_features = [\n",
    "                    'age',\n",
    "                    'fnlwgt', \n",
    "                    'education.num',\n",
    "                    'capital.gain', \n",
    "                    'capital.loss', \n",
    "                    'hours.per.week',                     \n",
    "                   ]\n",
    "\n",
    "# Categorical features\n",
    "cat_features = [\n",
    "                 'workclass',              \n",
    "                 'education',            \n",
    "                 'marital.status', \n",
    "                 'occupation', \n",
    "                 'relationship', \n",
    "                 'race', \n",
    "                 'sex',\n",
    "                 'native.country'\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "37d099cd",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:33.022283Z",
     "iopub.status.busy": "2021-12-01T23:49:33.021592Z",
     "iopub.status.idle": "2021-12-01T23:49:33.050530Z",
     "shell.execute_reply": "2021-12-01T23:49:33.051193Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.255072Z"
    },
    "papermill": {
     "duration": 0.070353,
     "end_time": "2021-12-01T23:49:33.051390",
     "exception": false,
     "start_time": "2021-12-01T23:49:32.981037",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>fnlwgt</th>\n",
       "      <th>education.num</th>\n",
       "      <th>capital.gain</th>\n",
       "      <th>capital.loss</th>\n",
       "      <th>hours.per.week</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>26048.000000</td>\n",
       "      <td>2.604800e+04</td>\n",
       "      <td>26048.000000</td>\n",
       "      <td>26048.000000</td>\n",
       "      <td>26048.000000</td>\n",
       "      <td>26048.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>38.610335</td>\n",
       "      <td>1.895741e+05</td>\n",
       "      <td>10.082118</td>\n",
       "      <td>1081.193796</td>\n",
       "      <td>88.477695</td>\n",
       "      <td>40.420224</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>13.628346</td>\n",
       "      <td>1.043848e+05</td>\n",
       "      <td>2.574608</td>\n",
       "      <td>7404.962675</td>\n",
       "      <td>404.689981</td>\n",
       "      <td>12.354707</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>17.000000</td>\n",
       "      <td>1.228500e+04</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>28.000000</td>\n",
       "      <td>1.182472e+05</td>\n",
       "      <td>9.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>40.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>37.000000</td>\n",
       "      <td>1.785755e+05</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>40.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>48.000000</td>\n",
       "      <td>2.365968e+05</td>\n",
       "      <td>12.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>45.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>90.000000</td>\n",
       "      <td>1.484705e+06</td>\n",
       "      <td>16.000000</td>\n",
       "      <td>99999.000000</td>\n",
       "      <td>4356.000000</td>\n",
       "      <td>99.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                age        fnlwgt  education.num  capital.gain  capital.loss  \\\n",
       "count  26048.000000  2.604800e+04   26048.000000  26048.000000  26048.000000   \n",
       "mean      38.610335  1.895741e+05      10.082118   1081.193796     88.477695   \n",
       "std       13.628346  1.043848e+05       2.574608   7404.962675    404.689981   \n",
       "min       17.000000  1.228500e+04       1.000000      0.000000      0.000000   \n",
       "25%       28.000000  1.182472e+05       9.000000      0.000000      0.000000   \n",
       "50%       37.000000  1.785755e+05      10.000000      0.000000      0.000000   \n",
       "75%       48.000000  2.365968e+05      12.000000      0.000000      0.000000   \n",
       "max       90.000000  1.484705e+06      16.000000  99999.000000   4356.000000   \n",
       "\n",
       "       hours.per.week  \n",
       "count    26048.000000  \n",
       "mean        40.420224  \n",
       "std         12.354707  \n",
       "min          1.000000  \n",
       "25%         40.000000  \n",
       "50%         40.000000  \n",
       "75%         45.000000  \n",
       "max         99.000000  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train[numeric_features].describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a5b19fac",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:33.119763Z",
     "iopub.status.busy": "2021-12-01T23:49:33.118779Z",
     "iopub.status.idle": "2021-12-01T23:49:33.192211Z",
     "shell.execute_reply": "2021-12-01T23:49:33.191577Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.288451Z"
    },
    "papermill": {
     "duration": 0.10972,
     "end_time": "2021-12-01T23:49:33.192380",
     "exception": false,
     "start_time": "2021-12-01T23:49:33.082660",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>workclass</th>\n",
       "      <th>education</th>\n",
       "      <th>marital.status</th>\n",
       "      <th>occupation</th>\n",
       "      <th>relationship</th>\n",
       "      <th>race</th>\n",
       "      <th>sex</th>\n",
       "      <th>native.country</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>24592</td>\n",
       "      <td>26048</td>\n",
       "      <td>26048</td>\n",
       "      <td>24585</td>\n",
       "      <td>26048</td>\n",
       "      <td>26048</td>\n",
       "      <td>26048</td>\n",
       "      <td>25587</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>8</td>\n",
       "      <td>16</td>\n",
       "      <td>7</td>\n",
       "      <td>14</td>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "      <td>41</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>Private</td>\n",
       "      <td>HS-grad</td>\n",
       "      <td>Married-civ-spouse</td>\n",
       "      <td>Exec-managerial</td>\n",
       "      <td>Husband</td>\n",
       "      <td>White</td>\n",
       "      <td>Male</td>\n",
       "      <td>United-States</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>18160</td>\n",
       "      <td>8408</td>\n",
       "      <td>11987</td>\n",
       "      <td>3323</td>\n",
       "      <td>10558</td>\n",
       "      <td>22270</td>\n",
       "      <td>17400</td>\n",
       "      <td>23381</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       workclass education      marital.status       occupation relationship  \\\n",
       "count      24592     26048               26048            24585        26048   \n",
       "unique         8        16                   7               14            6   \n",
       "top      Private   HS-grad  Married-civ-spouse  Exec-managerial      Husband   \n",
       "freq       18160      8408               11987             3323        10558   \n",
       "\n",
       "         race    sex native.country  \n",
       "count   26048  26048          25587  \n",
       "unique      5      2             41  \n",
       "top     White   Male  United-States  \n",
       "freq    22270  17400          23381  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train[cat_features].describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "35caa4b0",
   "metadata": {
    "papermill": {
     "duration": 0.032992,
     "end_time": "2021-12-01T23:49:33.257998",
     "exception": false,
     "start_time": "2021-12-01T23:49:33.225006",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## 결측치 처리"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "8921e25d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:33.350474Z",
     "iopub.status.busy": "2021-12-01T23:49:33.349447Z",
     "iopub.status.idle": "2021-12-01T23:49:33.357331Z",
     "shell.execute_reply": "2021-12-01T23:49:33.356604Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.329546Z"
    },
    "papermill": {
     "duration": 0.066836,
     "end_time": "2021-12-01T23:49:33.357519",
     "exception": false,
     "start_time": "2021-12-01T23:49:33.290683",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id                   0\n",
       "age                  0\n",
       "workclass         1456\n",
       "fnlwgt               0\n",
       "education            0\n",
       "education.num        0\n",
       "marital.status       0\n",
       "occupation        1463\n",
       "relationship         0\n",
       "race                 0\n",
       "sex                  0\n",
       "capital.gain         0\n",
       "capital.loss         0\n",
       "hours.per.week       0\n",
       "native.country     461\n",
       "dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "5c331b9a",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:33.424360Z",
     "iopub.status.busy": "2021-12-01T23:49:33.423719Z",
     "iopub.status.idle": "2021-12-01T23:49:33.437491Z",
     "shell.execute_reply": "2021-12-01T23:49:33.437959Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.358079Z"
    },
    "papermill": {
     "duration": 0.048467,
     "end_time": "2021-12-01T23:49:33.438143",
     "exception": false,
     "start_time": "2021-12-01T23:49:33.389676",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id                  0\n",
       "age                 0\n",
       "workclass         380\n",
       "fnlwgt              0\n",
       "education           0\n",
       "education.num       0\n",
       "marital.status      0\n",
       "occupation        380\n",
       "relationship        0\n",
       "race                0\n",
       "sex                 0\n",
       "capital.gain        0\n",
       "capital.loss        0\n",
       "hours.per.week      0\n",
       "native.country    122\n",
       "dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "4e23b597",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:33.512299Z",
     "iopub.status.busy": "2021-12-01T23:49:33.511488Z",
     "iopub.status.idle": "2021-12-01T23:49:33.514596Z",
     "shell.execute_reply": "2021-12-01T23:49:33.515080Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.380415Z"
    },
    "papermill": {
     "duration": 0.045432,
     "end_time": "2021-12-01T23:49:33.515256",
     "exception": false,
     "start_time": "2021-12-01T23:49:33.469824",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Private             18160\n",
       "Self-emp-not-inc     2049\n",
       "Local-gov            1648\n",
       "State-gov            1037\n",
       "Self-emp-inc          909\n",
       "Federal-gov           770\n",
       "Without-pay            12\n",
       "Never-worked            7\n",
       "Name: workclass, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train['workclass'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2c7b6cf5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:33.590602Z",
     "iopub.status.busy": "2021-12-01T23:49:33.589892Z",
     "iopub.status.idle": "2021-12-01T23:49:33.592418Z",
     "shell.execute_reply": "2021-12-01T23:49:33.592955Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.392710Z"
    },
    "papermill": {
     "duration": 0.045574,
     "end_time": "2021-12-01T23:49:33.593125",
     "exception": false,
     "start_time": "2021-12-01T23:49:33.547551",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Exec-managerial      3323\n",
       "Prof-specialty       3306\n",
       "Craft-repair         3296\n",
       "Adm-clerical         3037\n",
       "Sales                2898\n",
       "Other-service        2624\n",
       "Machine-op-inspct    1584\n",
       "Transport-moving     1257\n",
       "Handlers-cleaners    1080\n",
       "Farming-fishing       786\n",
       "Tech-support          746\n",
       "Protective-serv       521\n",
       "Priv-house-serv       119\n",
       "Armed-Forces            8\n",
       "Name: occupation, dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train['occupation'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "2b9a9a1b",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:33.662738Z",
     "iopub.status.busy": "2021-12-01T23:49:33.662026Z",
     "iopub.status.idle": "2021-12-01T23:49:33.672772Z",
     "shell.execute_reply": "2021-12-01T23:49:33.673360Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.403529Z"
    },
    "papermill": {
     "duration": 0.047577,
     "end_time": "2021-12-01T23:49:33.673537",
     "exception": false,
     "start_time": "2021-12-01T23:49:33.625960",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "United-States                 23381\n",
       "Mexico                          516\n",
       "Philippines                     158\n",
       "Germany                         108\n",
       "Canada                           88\n",
       "Puerto-Rico                      87\n",
       "El-Salvador                      76\n",
       "India                            73\n",
       "Cuba                             73\n",
       "England                          69\n",
       "Italy                            63\n",
       "South                            62\n",
       "Jamaica                          59\n",
       "Vietnam                          57\n",
       "China                            57\n",
       "Guatemala                        54\n",
       "Dominican-Republic               51\n",
       "Japan                            49\n",
       "Poland                           47\n",
       "Columbia                         44\n",
       "Taiwan                           37\n",
       "Haiti                            37\n",
       "Iran                             34\n",
       "Portugal                         32\n",
       "Peru                             29\n",
       "Nicaragua                        27\n",
       "Ecuador                          25\n",
       "Greece                           24\n",
       "France                           23\n",
       "Ireland                          19\n",
       "Cambodia                         18\n",
       "Hong                             17\n",
       "Trinadad&Tobago                  17\n",
       "Thailand                         16\n",
       "Laos                             13\n",
       "Outlying-US(Guam-USVI-etc)       11\n",
       "Yugoslavia                       11\n",
       "Honduras                          9\n",
       "Hungary                           8\n",
       "Scotland                          7\n",
       "Holand-Netherlands                1\n",
       "Name: native.country, dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_train['native.country'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3b14860f",
   "metadata": {
    "papermill": {
     "duration": 0.034535,
     "end_time": "2021-12-01T23:49:33.741228",
     "exception": false,
     "start_time": "2021-12-01T23:49:33.706693",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "- 결측치는 최빈값과 차이가 크면 최빈값으로 값이 비슷하면 별도의 값으로 대체함"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "fae66f1f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:33.814961Z",
     "iopub.status.busy": "2021-12-01T23:49:33.814278Z",
     "iopub.status.idle": "2021-12-01T23:49:33.871132Z",
     "shell.execute_reply": "2021-12-01T23:49:33.871759Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.415250Z"
    },
    "papermill": {
     "duration": 0.094211,
     "end_time": "2021-12-01T23:49:33.871931",
     "exception": false,
     "start_time": "2021-12-01T23:49:33.777720",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "id                0\n",
       "age               0\n",
       "workclass         0\n",
       "fnlwgt            0\n",
       "education         0\n",
       "education.num     0\n",
       "marital.status    0\n",
       "occupation        0\n",
       "relationship      0\n",
       "race              0\n",
       "sex               0\n",
       "capital.gain      0\n",
       "capital.loss      0\n",
       "hours.per.week    0\n",
       "native.country    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def data_fillna(df):\n",
    "    df['workclass'] = df['workclass'].fillna(df['workclass'].mode()[0])\n",
    "    df['occupation'] = df['occupation'].fillna(\"null\")\n",
    "    df['native.country'] = df[\"native.country\"].fillna(df['native.country'].mode()[0])\n",
    "    return df\n",
    "\n",
    "X_train = data_fillna(X_train)\n",
    "X_test = data_fillna(X_test)\n",
    "\n",
    "X_train.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1e387911",
   "metadata": {
    "papermill": {
     "duration": 0.034915,
     "end_time": "2021-12-01T23:49:33.941188",
     "exception": false,
     "start_time": "2021-12-01T23:49:33.906273",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## 피처엔지니어링"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "2e08cd69",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:34.012926Z",
     "iopub.status.busy": "2021-12-01T23:49:34.012176Z",
     "iopub.status.idle": "2021-12-01T23:49:34.175138Z",
     "shell.execute_reply": "2021-12-01T23:49:34.175704Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.449897Z"
    },
    "papermill": {
     "duration": 0.199909,
     "end_time": "2021-12-01T23:49:34.175881",
     "exception": false,
     "start_time": "2021-12-01T23:49:33.975972",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>age</th>\n",
       "      <th>workclass</th>\n",
       "      <th>fnlwgt</th>\n",
       "      <th>education</th>\n",
       "      <th>education.num</th>\n",
       "      <th>marital.status</th>\n",
       "      <th>occupation</th>\n",
       "      <th>relationship</th>\n",
       "      <th>race</th>\n",
       "      <th>sex</th>\n",
       "      <th>capital.gain</th>\n",
       "      <th>capital.loss</th>\n",
       "      <th>hours.per.week</th>\n",
       "      <th>native.country</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>20901</th>\n",
       "      <td>20901</td>\n",
       "      <td>58</td>\n",
       "      <td>3</td>\n",
       "      <td>114495</td>\n",
       "      <td>11</td>\n",
       "      <td>9</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14170</th>\n",
       "      <td>14170</td>\n",
       "      <td>46</td>\n",
       "      <td>3</td>\n",
       "      <td>247043</td>\n",
       "      <td>11</td>\n",
       "      <td>9</td>\n",
       "      <td>2</td>\n",
       "      <td>13</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1776</th>\n",
       "      <td>1776</td>\n",
       "      <td>67</td>\n",
       "      <td>1</td>\n",
       "      <td>103315</td>\n",
       "      <td>12</td>\n",
       "      <td>14</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>15831</td>\n",
       "      <td>0</td>\n",
       "      <td>72</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30428</th>\n",
       "      <td>30428</td>\n",
       "      <td>18</td>\n",
       "      <td>3</td>\n",
       "      <td>165532</td>\n",
       "      <td>15</td>\n",
       "      <td>10</td>\n",
       "      <td>4</td>\n",
       "      <td>11</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>15</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8602</th>\n",
       "      <td>8602</td>\n",
       "      <td>26</td>\n",
       "      <td>6</td>\n",
       "      <td>58039</td>\n",
       "      <td>15</td>\n",
       "      <td>10</td>\n",
       "      <td>2</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31222</th>\n",
       "      <td>31222</td>\n",
       "      <td>22</td>\n",
       "      <td>3</td>\n",
       "      <td>199426</td>\n",
       "      <td>15</td>\n",
       "      <td>10</td>\n",
       "      <td>4</td>\n",
       "      <td>14</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10861</th>\n",
       "      <td>10861</td>\n",
       "      <td>41</td>\n",
       "      <td>3</td>\n",
       "      <td>155106</td>\n",
       "      <td>11</td>\n",
       "      <td>9</td>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8929</th>\n",
       "      <td>8929</td>\n",
       "      <td>32</td>\n",
       "      <td>3</td>\n",
       "      <td>153078</td>\n",
       "      <td>9</td>\n",
       "      <td>13</td>\n",
       "      <td>4</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "      <td>34</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2066</th>\n",
       "      <td>2066</td>\n",
       "      <td>48</td>\n",
       "      <td>6</td>\n",
       "      <td>171926</td>\n",
       "      <td>14</td>\n",
       "      <td>15</td>\n",
       "      <td>2</td>\n",
       "      <td>9</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>15024</td>\n",
       "      <td>0</td>\n",
       "      <td>50</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25782</th>\n",
       "      <td>25782</td>\n",
       "      <td>42</td>\n",
       "      <td>3</td>\n",
       "      <td>433170</td>\n",
       "      <td>15</td>\n",
       "      <td>10</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>60</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>6513 rows × 15 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          id  age  workclass  fnlwgt  education  education.num  \\\n",
       "20901  20901   58          3  114495         11              9   \n",
       "14170  14170   46          3  247043         11              9   \n",
       "1776    1776   67          1  103315         12             14   \n",
       "30428  30428   18          3  165532         15             10   \n",
       "8602    8602   26          6   58039         15             10   \n",
       "...      ...  ...        ...     ...        ...            ...   \n",
       "31222  31222   22          3  199426         15             10   \n",
       "10861  10861   41          3  155106         11              9   \n",
       "8929    8929   32          3  153078          9             13   \n",
       "2066    2066   48          6  171926         14             15   \n",
       "25782  25782   42          3  433170         15             10   \n",
       "\n",
       "       marital.status  occupation  relationship  race  sex  capital.gain  \\\n",
       "20901               2           3             0     4    1             0   \n",
       "14170               2          13             0     4    1             0   \n",
       "1776                4           3             2     4    0         15831   \n",
       "30428               4          11             3     4    1             0   \n",
       "8602                2           7             0     4    1             0   \n",
       "...               ...         ...           ...   ...  ...           ...   \n",
       "31222               4          14             1     4    0             0   \n",
       "10861               2           5             0     4    1             0   \n",
       "8929                4           7             1     1    1             0   \n",
       "2066                2           9             0     4    1         15024   \n",
       "25782               2           2             0     4    1             0   \n",
       "\n",
       "       capital.loss  hours.per.week  native.country  \n",
       "20901             0              40              38  \n",
       "14170             0              40              38  \n",
       "1776              0              72              38  \n",
       "30428             0              15              38  \n",
       "8602              0              40              38  \n",
       "...             ...             ...             ...  \n",
       "31222             0              40              38  \n",
       "10861             0              40              38  \n",
       "8929              0              40              34  \n",
       "2066              0              50              38  \n",
       "25782             0              60              38  \n",
       "\n",
       "[6513 rows x 15 columns]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 라벨인코딩\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "all_df = pd.concat([X_train.assign(ind=\"train\"), X_test.assign(ind=\"test\")])\n",
    "le = LabelEncoder()\n",
    "all_df[cat_features] = all_df[cat_features].apply(le.fit_transform)\n",
    "\n",
    "X_train = all_df[all_df['ind'] == 'train']\n",
    "X_train = X_train.drop('ind',axis=1)\n",
    "X_train\n",
    "\n",
    "X_test = all_df[all_df['ind'] == 'test']\n",
    "X_test = X_test.drop('ind',axis=1)\n",
    "X_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "dc62481d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:34.250268Z",
     "iopub.status.busy": "2021-12-01T23:49:34.249589Z",
     "iopub.status.idle": "2021-12-01T23:49:34.289958Z",
     "shell.execute_reply": "2021-12-01T23:49:34.289329Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.541500Z"
    },
    "papermill": {
     "duration": 0.077931,
     "end_time": "2021-12-01T23:49:34.290104",
     "exception": false,
     "start_time": "2021-12-01T23:49:34.212173",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>age</th>\n",
       "      <th>workclass</th>\n",
       "      <th>fnlwgt</th>\n",
       "      <th>education</th>\n",
       "      <th>education.num</th>\n",
       "      <th>marital.status</th>\n",
       "      <th>occupation</th>\n",
       "      <th>relationship</th>\n",
       "      <th>race</th>\n",
       "      <th>sex</th>\n",
       "      <th>capital.gain</th>\n",
       "      <th>capital.loss</th>\n",
       "      <th>hours.per.week</th>\n",
       "      <th>native.country</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>21851</th>\n",
       "      <td>21851</td>\n",
       "      <td>0.260274</td>\n",
       "      <td>3</td>\n",
       "      <td>0.156011</td>\n",
       "      <td>9</td>\n",
       "      <td>0.800000</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.500000</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7632</th>\n",
       "      <td>7632</td>\n",
       "      <td>0.493151</td>\n",
       "      <td>3</td>\n",
       "      <td>0.062255</td>\n",
       "      <td>12</td>\n",
       "      <td>0.866667</td>\n",
       "      <td>0</td>\n",
       "      <td>9</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.397959</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27878</th>\n",
       "      <td>27878</td>\n",
       "      <td>0.027397</td>\n",
       "      <td>3</td>\n",
       "      <td>0.129566</td>\n",
       "      <td>15</td>\n",
       "      <td>0.600000</td>\n",
       "      <td>4</td>\n",
       "      <td>12</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.244898</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14121</th>\n",
       "      <td>14121</td>\n",
       "      <td>0.041096</td>\n",
       "      <td>3</td>\n",
       "      <td>0.061343</td>\n",
       "      <td>11</td>\n",
       "      <td>0.533333</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.295918</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32345</th>\n",
       "      <td>32345</td>\n",
       "      <td>0.506849</td>\n",
       "      <td>6</td>\n",
       "      <td>0.085958</td>\n",
       "      <td>11</td>\n",
       "      <td>0.533333</td>\n",
       "      <td>2</td>\n",
       "      <td>9</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.397959</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2669</th>\n",
       "      <td>2669</td>\n",
       "      <td>0.383562</td>\n",
       "      <td>3</td>\n",
       "      <td>0.118910</td>\n",
       "      <td>12</td>\n",
       "      <td>0.866667</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0.074301</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.704082</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17536</th>\n",
       "      <td>17536</td>\n",
       "      <td>0.260274</td>\n",
       "      <td>3</td>\n",
       "      <td>0.110039</td>\n",
       "      <td>1</td>\n",
       "      <td>0.400000</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.397959</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6201</th>\n",
       "      <td>6201</td>\n",
       "      <td>0.410959</td>\n",
       "      <td>3</td>\n",
       "      <td>0.178669</td>\n",
       "      <td>7</td>\n",
       "      <td>0.733333</td>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.346939</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27989</th>\n",
       "      <td>27989</td>\n",
       "      <td>0.452055</td>\n",
       "      <td>5</td>\n",
       "      <td>0.125113</td>\n",
       "      <td>10</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>2</td>\n",
       "      <td>9</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.224490</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25716</th>\n",
       "      <td>25716</td>\n",
       "      <td>0.027397</td>\n",
       "      <td>3</td>\n",
       "      <td>0.270479</td>\n",
       "      <td>11</td>\n",
       "      <td>0.533333</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.397959</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>26048 rows × 15 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          id       age  workclass    fnlwgt  education  education.num  \\\n",
       "21851  21851  0.260274          3  0.156011          9       0.800000   \n",
       "7632    7632  0.493151          3  0.062255         12       0.866667   \n",
       "27878  27878  0.027397          3  0.129566         15       0.600000   \n",
       "14121  14121  0.041096          3  0.061343         11       0.533333   \n",
       "32345  32345  0.506849          6  0.085958         11       0.533333   \n",
       "...      ...       ...        ...       ...        ...            ...   \n",
       "2669    2669  0.383562          3  0.118910         12       0.866667   \n",
       "17536  17536  0.260274          3  0.110039          1       0.400000   \n",
       "6201    6201  0.410959          3  0.178669          7       0.733333   \n",
       "27989  27989  0.452055          5  0.125113         10       1.000000   \n",
       "25716  25716  0.027397          3  0.270479         11       0.533333   \n",
       "\n",
       "       marital.status  occupation  relationship  race  sex  capital.gain  \\\n",
       "21851               2           2             0     4    1      0.000000   \n",
       "7632                0           9             1     4    0      0.000000   \n",
       "27878               4          12             1     4    0      0.000000   \n",
       "14121               4           5             3     4    1      0.000000   \n",
       "32345               2           9             0     4    1      0.000000   \n",
       "...               ...         ...           ...   ...  ...           ...   \n",
       "2669                0           3             4     4    1      0.074301   \n",
       "17536               0          13             1     4    1      0.000000   \n",
       "6201                6           7             3     4    0      0.000000   \n",
       "27989               2           9             0     4    1      0.000000   \n",
       "25716               4           0             1     4    0      0.000000   \n",
       "\n",
       "       capital.loss  hours.per.week  native.country  \n",
       "21851           0.0        0.500000              38  \n",
       "7632            0.0        0.397959              38  \n",
       "27878           0.0        0.244898              38  \n",
       "14121           0.0        0.295918              38  \n",
       "32345           0.0        0.397959              38  \n",
       "...             ...             ...             ...  \n",
       "2669            0.0        0.704082              38  \n",
       "17536           0.0        0.397959              38  \n",
       "6201            0.0        0.346939              38  \n",
       "27989           0.0        0.224490              38  \n",
       "25716           0.0        0.397959              38  \n",
       "\n",
       "[26048 rows x 15 columns]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 스케일링\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "\n",
    "scaler = MinMaxScaler()\n",
    "X_train[numeric_features] = scaler.fit_transform(X_train[numeric_features])\n",
    "X_test[numeric_features] = scaler.transform(X_test[numeric_features])\n",
    "X_train"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "2c283900",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:34.370914Z",
     "iopub.status.busy": "2021-12-01T23:49:34.370108Z",
     "iopub.status.idle": "2021-12-01T23:49:34.375200Z",
     "shell.execute_reply": "2021-12-01T23:49:34.375860Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.583236Z"
    },
    "papermill": {
     "duration": 0.05049,
     "end_time": "2021-12-01T23:49:34.376037",
     "exception": false,
     "start_time": "2021-12-01T23:49:34.325547",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "21851    1\n",
       "7632     0\n",
       "27878    0\n",
       "14121    0\n",
       "32345    0\n",
       "Name: income, dtype: int64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# target값 변경\n",
    "y = (y_train['income'] != '<=50K').astype(int)\n",
    "y[:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "795459f2",
   "metadata": {
    "papermill": {
     "duration": 0.034649,
     "end_time": "2021-12-01T23:49:34.447181",
     "exception": false,
     "start_time": "2021-12-01T23:49:34.412532",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## 검증용 데이터 분리"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "9403e615",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:34.520726Z",
     "iopub.status.busy": "2021-12-01T23:49:34.520023Z",
     "iopub.status.idle": "2021-12-01T23:49:34.531984Z",
     "shell.execute_reply": "2021-12-01T23:49:34.532652Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.596578Z"
    },
    "papermill": {
     "duration": 0.05038,
     "end_time": "2021-12-01T23:49:34.532835",
     "exception": false,
     "start_time": "2021-12-01T23:49:34.482455",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "((22140, 15), (3908, 15), (22140,), (3908,))"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 학습용 데이터와 검증용 데이터로 구분\n",
    "from sklearn.model_selection import train_test_split\n",
    "X_tr, X_val, y_tr, y_val = train_test_split(X_train, y, test_size=0.15, random_state=2021)\n",
    "X_tr.shape, X_val.shape, y_tr.shape, y_val.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "72ebec15",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:34.608093Z",
     "iopub.status.busy": "2021-12-01T23:49:34.607425Z",
     "iopub.status.idle": "2021-12-01T23:49:34.623615Z",
     "shell.execute_reply": "2021-12-01T23:49:34.624226Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.609965Z"
    },
    "papermill": {
     "duration": 0.055928,
     "end_time": "2021-12-01T23:49:34.624423",
     "exception": false,
     "start_time": "2021-12-01T23:49:34.568495",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>age</th>\n",
       "      <th>workclass</th>\n",
       "      <th>fnlwgt</th>\n",
       "      <th>education</th>\n",
       "      <th>education.num</th>\n",
       "      <th>marital.status</th>\n",
       "      <th>occupation</th>\n",
       "      <th>relationship</th>\n",
       "      <th>race</th>\n",
       "      <th>sex</th>\n",
       "      <th>capital.gain</th>\n",
       "      <th>capital.loss</th>\n",
       "      <th>hours.per.week</th>\n",
       "      <th>native.country</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1437</th>\n",
       "      <td>1437</td>\n",
       "      <td>0.191781</td>\n",
       "      <td>3</td>\n",
       "      <td>0.216501</td>\n",
       "      <td>9</td>\n",
       "      <td>0.800000</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.323232</td>\n",
       "      <td>0.397959</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7151</th>\n",
       "      <td>7151</td>\n",
       "      <td>0.287671</td>\n",
       "      <td>5</td>\n",
       "      <td>0.127591</td>\n",
       "      <td>11</td>\n",
       "      <td>0.533333</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.602041</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30296</th>\n",
       "      <td>30296</td>\n",
       "      <td>0.424658</td>\n",
       "      <td>3</td>\n",
       "      <td>0.217452</td>\n",
       "      <td>9</td>\n",
       "      <td>0.800000</td>\n",
       "      <td>2</td>\n",
       "      <td>9</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.346939</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15372</th>\n",
       "      <td>15372</td>\n",
       "      <td>0.452055</td>\n",
       "      <td>3</td>\n",
       "      <td>0.142442</td>\n",
       "      <td>11</td>\n",
       "      <td>0.533333</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.397959</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13800</th>\n",
       "      <td>13800</td>\n",
       "      <td>0.178082</td>\n",
       "      <td>3</td>\n",
       "      <td>0.187243</td>\n",
       "      <td>15</td>\n",
       "      <td>0.600000</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.397959</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          id       age  workclass    fnlwgt  education  education.num  \\\n",
       "1437    1437  0.191781          3  0.216501          9       0.800000   \n",
       "7151    7151  0.287671          5  0.127591         11       0.533333   \n",
       "30296  30296  0.424658          3  0.217452          9       0.800000   \n",
       "15372  15372  0.452055          3  0.142442         11       0.533333   \n",
       "13800  13800  0.178082          3  0.187243         15       0.600000   \n",
       "\n",
       "       marital.status  occupation  relationship  race  sex  capital.gain  \\\n",
       "1437                4           3             1     4    0           0.0   \n",
       "7151                2           2             0     4    1           0.0   \n",
       "30296               2           9             0     4    1           0.0   \n",
       "15372               2           2             0     4    1           0.0   \n",
       "13800               4           5             1     4    1           0.0   \n",
       "\n",
       "       capital.loss  hours.per.week  native.country  \n",
       "1437       0.323232        0.397959              38  \n",
       "7151       0.000000        0.602041              38  \n",
       "30296      0.000000        0.346939              38  \n",
       "15372      0.000000        0.397959              38  \n",
       "13800      0.000000        0.397959              38  "
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_tr.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c3d205f7",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:34.761396Z",
     "iopub.status.busy": "2021-12-01T23:49:34.760638Z",
     "iopub.status.idle": "2021-12-01T23:49:34.767280Z",
     "shell.execute_reply": "2021-12-01T23:49:34.767853Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.623821Z"
    },
    "papermill": {
     "duration": 0.046587,
     "end_time": "2021-12-01T23:49:34.768046",
     "exception": false,
     "start_time": "2021-12-01T23:49:34.721459",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# id 삭제\n",
    "X_tr = X_tr.drop('id', axis=1)\n",
    "X_val = X_val.drop('id', axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "07bfdb66",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:34.844639Z",
     "iopub.status.busy": "2021-12-01T23:49:34.843853Z",
     "iopub.status.idle": "2021-12-01T23:49:34.857084Z",
     "shell.execute_reply": "2021-12-01T23:49:34.857770Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.632400Z"
    },
    "papermill": {
     "duration": 0.05339,
     "end_time": "2021-12-01T23:49:34.857950",
     "exception": false,
     "start_time": "2021-12-01T23:49:34.804560",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>age</th>\n",
       "      <th>workclass</th>\n",
       "      <th>fnlwgt</th>\n",
       "      <th>education</th>\n",
       "      <th>education.num</th>\n",
       "      <th>marital.status</th>\n",
       "      <th>occupation</th>\n",
       "      <th>relationship</th>\n",
       "      <th>race</th>\n",
       "      <th>sex</th>\n",
       "      <th>capital.gain</th>\n",
       "      <th>capital.loss</th>\n",
       "      <th>hours.per.week</th>\n",
       "      <th>native.country</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1437</th>\n",
       "      <td>0.191781</td>\n",
       "      <td>3</td>\n",
       "      <td>0.216501</td>\n",
       "      <td>9</td>\n",
       "      <td>0.8</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.323232</td>\n",
       "      <td>0.397959</td>\n",
       "      <td>38</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           age  workclass    fnlwgt  education  education.num  marital.status  \\\n",
       "1437  0.191781          3  0.216501          9            0.8               4   \n",
       "\n",
       "      occupation  relationship  race  sex  capital.gain  capital.loss  \\\n",
       "1437           3             1     4    0           0.0      0.323232   \n",
       "\n",
       "      hours.per.week  native.country  \n",
       "1437        0.397959              38  "
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# id 삭제된 것 확인\n",
    "X_tr.head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "95fca160",
   "metadata": {
    "papermill": {
     "duration": 0.0369,
     "end_time": "2021-12-01T23:49:34.931730",
     "exception": false,
     "start_time": "2021-12-01T23:49:34.894830",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## 모델 & 평가"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "f47d5c49",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:35.011184Z",
     "iopub.status.busy": "2021-12-01T23:49:35.010511Z",
     "iopub.status.idle": "2021-12-01T23:49:35.439592Z",
     "shell.execute_reply": "2021-12-01T23:49:35.440052Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.652542Z"
    },
    "papermill": {
     "duration": 0.469305,
     "end_time": "2021-12-01T23:49:35.440225",
     "exception": false,
     "start_time": "2021-12-01T23:49:34.970920",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "accuracy score: 0.8119242579324463\n"
     ]
    }
   ],
   "source": [
    "# 의사결정나무\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "model = DecisionTreeClassifier(random_state = 2022)\n",
    "model.fit(X_tr, y_tr)\n",
    "pred = model.predict(X_val)\n",
    "print('accuracy score:', (accuracy_score(y_val, pred)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "97f07645",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:35.521146Z",
     "iopub.status.busy": "2021-12-01T23:49:35.520456Z",
     "iopub.status.idle": "2021-12-01T23:49:38.064608Z",
     "shell.execute_reply": "2021-12-01T23:49:38.064016Z",
     "shell.execute_reply.started": "2021-12-01T23:48:26.792447Z"
    },
    "papermill": {
     "duration": 2.587149,
     "end_time": "2021-12-01T23:49:38.064763",
     "exception": false,
     "start_time": "2021-12-01T23:49:35.477614",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "accuracy score: 0.8480040941658137\n"
     ]
    }
   ],
   "source": [
    "# 랜덤포레스트\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "\n",
    "model = RandomForestClassifier(random_state = 2022)\n",
    "model.fit(X_tr, y_tr)\n",
    "pred = model.predict(X_val)\n",
    "print('accuracy score:', (accuracy_score(y_val, pred)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "fb63bc67",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:38.143618Z",
     "iopub.status.busy": "2021-12-01T23:49:38.142936Z",
     "iopub.status.idle": "2021-12-01T23:49:38.295400Z",
     "shell.execute_reply": "2021-12-01T23:49:38.294813Z",
     "shell.execute_reply.started": "2021-12-01T23:48:29.844732Z"
    },
    "papermill": {
     "duration": 0.19287,
     "end_time": "2021-12-01T23:49:38.295558",
     "exception": false,
     "start_time": "2021-12-01T23:49:38.102688",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# test데이터 예측 (pop을 활용하면 값을 넘겨주고 삭제 됨)\n",
    "X_test_id = X_test.pop('id')\n",
    "pred = model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "159f04c6",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:38.374752Z",
     "iopub.status.busy": "2021-12-01T23:49:38.374080Z",
     "iopub.status.idle": "2021-12-01T23:49:38.399637Z",
     "shell.execute_reply": "2021-12-01T23:49:38.398990Z",
     "shell.execute_reply.started": "2021-12-01T23:48:29.994226Z"
    },
    "papermill": {
     "duration": 0.065585,
     "end_time": "2021-12-01T23:49:38.399776",
     "exception": false,
     "start_time": "2021-12-01T23:49:38.334191",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>income</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>20901</th>\n",
       "      <td>20901</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14170</th>\n",
       "      <td>14170</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1776</th>\n",
       "      <td>1776</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30428</th>\n",
       "      <td>30428</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8602</th>\n",
       "      <td>8602</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          id  income\n",
       "20901  20901       0\n",
       "14170  14170       0\n",
       "1776    1776       1\n",
       "30428  30428       0\n",
       "8602    8602       0"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# csv생성\n",
    "output = pd.DataFrame({'id': X_test_id, 'income':pred})\n",
    "output.to_csv(\"000000.csv\", index=False)\n",
    "output.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3107e85e",
   "metadata": {
    "papermill": {
     "duration": 0.037643,
     "end_time": "2021-12-01T23:49:38.475223",
     "exception": false,
     "start_time": "2021-12-01T23:49:38.437580",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "## 채점 (수험자는 확인 불가)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "c8f4a44e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2021-12-01T23:49:38.559103Z",
     "iopub.status.busy": "2021-12-01T23:49:38.558324Z",
     "iopub.status.idle": "2021-12-01T23:49:38.562992Z",
     "shell.execute_reply": "2021-12-01T23:49:38.562309Z",
     "shell.execute_reply.started": "2021-12-01T23:48:30.017330Z"
    },
    "papermill": {
     "duration": 0.050015,
     "end_time": "2021-12-01T23:49:38.563140",
     "exception": false,
     "start_time": "2021-12-01T23:49:38.513125",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "accuracy score: 0.8569015814524796\n"
     ]
    }
   ],
   "source": [
    "y_test = (y_test['income'] != '<=50K').astype(int)\n",
    "from sklearn.metrics import accuracy_score\n",
    "print('accuracy score:', (accuracy_score(y_test, pred)))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.10"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 18.152093,
   "end_time": "2021-12-01T23:49:39.312448",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2021-12-01T23:49:21.160355",
   "version": "2.3.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
