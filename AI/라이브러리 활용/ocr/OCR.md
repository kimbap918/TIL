SOTA 모델
-> State-of-the-art : 특정 분야에서 현재 가장 높은 수준의 성능을 달성한 모델이나 기술

<OCR 활용도가 높은 프레임워크>
- 해외 : tesseract OCR
- 해외 : EasyOCR
- 국내 : 네이버 CLOVA OCR

1. 프로젝트 환경설정
   c:\ai_exam\015_ocr
   가상환경 : p38_cnn

   OCR -> tesseract -> 결과 ?

   google -> pypi tessetact
   pip install pytesseract
   => 엔진만 설치가 됨.
        언어학습된 데이터는 존재하지 않음.

2. 설치 프로그램(Pre-Trained모델)
   https://github.com/UB-Mannheim/tesseract/wiki

   OCR 저장 pdf
   korean -> OCR 처리 -> 일본어 -> PDF
   설치 후 언어데이터가 잘 설치되었는지 확인
   C:\Program Files\Tesseract-OCR\tessdata
   kor.traineddata



