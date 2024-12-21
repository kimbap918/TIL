from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# 서울시 실시간 교통정보 API 호출
@app.route('/traffic_data')
def get_traffic_data():
    api_key = '2eN3N3H0I5Ztq6NNKW/71v3BSC2dkFcjR3AK5HhrLkqzDymS5jqFK9b45czjb4K2JCxkI4zAjMudwftUgxKa0g=='
    url = f"http://openapi.seoul.go.kr:8088/{api_key}/json/TrafficInfo/1/10/"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        traffic_data = response.json()
        return jsonify(traffic_data)
    else:
        return jsonify({'error': 'Failed to fetch traffic data'}), 500

# HTML 파일을 제공하는 라우트
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
