

## 🌐 서버 정보

- **서버 IP**: `116.125.140.113`
  
- **DB 포트**: `3306`
  
- **서비스 포트 사용범위**: `8000 ~ 12000`
  

---

## 📁 프로젝트 구조 및 주요 파일

### 📌 Django 백엔드

- **프로젝트 디렉토리**: `back/`
  
- **내부 설정 디렉토리**: `config/` 또는 `backend/`
  
- **기본 실행 포트 예시**: `8890`
  

### 📌 주요 Python 파일

|파일명|설명|
|---|---|
|`001_chatbot_gemini.py`|메인 챗봇 실행 파일|
|`chatbot_gemini_lib.py`|핵심 라이브러리 분리|
|`002_chatbot_chatgpt.py`|ChatGPT 버전 챗봇|
|`gradio_main.py`|Gradio 인터페이스 실행|
|`chatbot_run.sh`|서버에서 챗봇 백그라운드 실행용 스크립트|

---

## 🧩 `chatbot_gemini_lib.py` 기능

1. `vectordb_save(pdf경로)`
   
    - 문서 로드 → 분할 → 임베딩 → 벡터DB 저장
      
    - `pip install pymupdf`
      
    - `pip install faiss-cpu`
    
2. `vectordb_load(벡터DB 경로)`
   
    - 저장된 벡터DB 로드
    
3. `chat_query(질문)`
   
    - 로드된 벡터DB를 기반으로 질의 응답 수행
      

---

## 💻 리눅스 서버 명령어 요약

### 📁 디렉토리 관련

bash

복사편집

`$ mkdir 디렉토리명        # 디렉토리 생성 `

$ cd 디렉토리명           # 이동 $ cd ..                   # 상위 디렉토리로 이동 $ ls                      # 디렉토리 리스트 $ ls -al                  # 숨김 파일 포함 리스트 $ rm 파일명               # 파일 삭제 $ rm -R 디렉토리명        # 디렉토리 전체 삭제 $ rmdir 디렉토리명        # 빈 디렉토리 삭제`

### 📄 파일 작업

bash

복사편집

`$ nano 파일명             # 새로 생성 또는 열기 # 저장: Ctrl + O, 종료: Ctrl + X $ cat 파일명              # 파일 내용 보기`

### 💽 시스템 명령

bash

복사편집

`$ clear                   # 화면 클리어 $ df -h                   # 디스크 용량 확인 $ uname -a                # 커널/OS 정보 $ cat /etc/issue          # 배포판 버전 확인 $ cd ~                    # 홈 디렉토리로 이동`

---

## ⚙️ Django 프로젝트 생성 및 실행

bash

복사편집

`# 1. 가상환경 생성 및 활성화 $ python3.11 -m venv venv $ source ./venv/bin/activate  # 2. Django 설치 및 프로젝트 생성 (venv)$ pip install django (venv)$ django-admin startproject backend .  # 3. settings.py 수정 $ cd backend $ nano settings.py # ALLOWED_HOSTS = ['*'] 설정  # 4. 서버 실행 $ cd .. $ python manage.py runserver 0.0.0.0:8890`

- 접속: `http://116.125.140.113:8890`
  

---

## 🖥️ Gradio 서버 실행

### 백그라운드 실행

bash

복사편집

`$ nano chatbot_run.sh python gradio_main.py # 저장: Ctrl + O, 종료: Ctrl + X  # 실행 권한 부여 $ chmod 755 chatbot_run.sh  # 백그라운드 실행 $ nohup ./chatbot_run.sh > out.txt &`

### 실행 포트 지정 (코드 내)

python

복사편집

`demo.launch(server_port=8890, server_name="0.0.0.0")`

---

## 🧑‍💻 Node.js 예시 (React/Next.js 준비)

bash

복사편집

`$ npm i express $ nano app.js # 저장: Ctrl + O, 종료: Ctrl + X $ node app.js`

---

## 🔐 원격 접속 (VS Code + SSH)

1. **VS Code 열기**
   
2. **확장 설치**: `Remote Development`
   
3. **Command Palette 열기**: `Ctrl+Shift+P` → "Remote"
   
4. **접속하기**:
   
    nginx
    
    복사편집
    
    `ssh matalcross@116.125.140.113`
    

---

## 🔃 기타 유용한 팁

- `pip freeze > requirements.txt`: 설치된 패키지를 파일로 저장
  
- `pip install -r requirements.txt`: requirements 설치
  
- SFTP 파일 업로드 도구: **FileZilla**
  

---

## 🔚 접속 요약

|항목|정보|
|---|---|
|서버 IP|`116.125.140.113`|
|포트 예시|`8890` (`8000~12000` 중 자유롭게 사용 가능)|
|DB 포트|`3306`|
|웹 접속|`http://116.125.140.113:8890`|