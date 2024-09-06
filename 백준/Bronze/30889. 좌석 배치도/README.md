# [Bronze III] 좌석 배치도 - 30889 

[문제 링크](https://www.acmicpc.net/problem/30889) 

### 성능 요약

메모리: 31252 KB, 시간: 36 ms

### 분류

구현, 문자열

### 제출 일자

2024년 9월 6일 19:25:21

### 문제 설명

<p>희권이는 영화관에서 한 개의 상영관을 담당하고 있다. 상영관의 좌석은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>×</mo><mn>20</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10\times 20$</span></mjx-container> 형태이고, 좌석 번호는 다음과 같다.</p>

<p style="text-align: center;"><img alt="" src="https://u.acmicpc.net/53df96e2-59b5-4f0b-a537-783b6b0f0658/cinema.png" style="width: 711px; height: 400px;"></p>

<p>스크린을 기준으로 맨 앞이 A열, 맨 뒤가 J열이다. 좌석은 가장 왼쪽이 1번, 오른쪽이 20번이다.</p>

<p>갑자기 영화관의 컴퓨터가 고장이 나서 좌석 배치를 알 수 없게 되었다. 다행히 희권이에겐 손님들이 어떤 좌석을 예매했는지 정보가 남아있었다.</p>

<p>어떤 손님의 예매 정보가 A10이라면 A열 10번 좌석을 예매했다는 뜻이다.</p>

<p>희권이를 도와 영화관의 좌석 배치도를 만들어 보자. 단, 좌석이 중복되는 경우는 없다.</p>

### 입력 

 <p>첫 번째 줄에 영화를 예매한 손님 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>200</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(1 ≤ N ≤ 200)$</span> </mjx-container></p>

<p>두 번째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>줄 동안 각각의 손님이 예매한 좌석의 정보가 주어진다. </p>

### 출력 

 <p>상영관의 좌석 배치도를 출력한다. 사람이 있는 좌석은 <span style="color:#e74c3c;"><code>o</code></span>, 없는 좌석은 <span style="color:#e74c3c;"><code>.</code></span>으로 표기한다.</p>

