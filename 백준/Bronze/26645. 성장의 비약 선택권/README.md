# [Bronze III] 성장의 비약 선택권 - 26645 

[문제 링크](https://www.acmicpc.net/problem/26645) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현

### 제출 일자

2025년 3월 19일 18:21:41

### 문제 설명

<p>지훈이가 즐겨 하는 게임인 ‘메이플스토리’에는 레벨과 경험치가 존재한다. 메이플스토리에서 캐릭터의 레벨을 올리기 위해서는 많은 몬스터를 사냥하여 경험치를 얻어야 하지만, 다행히도 레벨업의 난이도를 낮추기 위해 다량의 경험치를 얻을 수 있는 아이템 ‘성장의 비약’이 존재한다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/40b497a7-09e1-47da-b191-99d515242636/-/preview/" style="height: 395px; width: 360px;"></p>

<p>이벤트로 가끔 얻을 수 있는 ‘성장의 비약 선택권’을 사용하면 위 사진처럼 네 가지의 성장의 비약 중 한 가지를 선택하여 적힌 개수만큼 얻을 수 있다. 캐릭터의 현재 레벨을 포함하는 구간의 성장의 비약을 사용하면 캐릭터의 레벨이 정확히 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>만큼 오른다. 태풍 성장의 비약은 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c223C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>200</mn><mo>∼</mo><mn>239</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$200\sim 239$</span></mjx-container>레벨의 캐릭터를 정확히 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1$</span></mjx-container>레벨 올려준다. 모든 성장의 비약은 한번에 한 개씩 사용할 수 있고, <strong>캐릭터의 현재 레벨을 포함하지 않는 구간의 성장의 비약은 사용하지 못한다.</strong></p>

<p>지훈이가 성장의 비약을 사용할 캐릭터의 현재 레벨이 주어졌을 때, 어떤 성장의 비약을 선택해야 가장 높은 레벨에 도달할 수 있는지 알려주자!</p>

<p>만약 가장 높은 레벨에 도달할 수 있는 성장의 비약의 종류가 둘 이상이라면, 사진상 더 아래에 있는 성장의 비약을 선택한다.</p>

### 입력 

 <p>첫 번째 줄에 지훈이가 성장의 비약을 사용할 캐릭터의 현재 레벨을 나타내는 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c33"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>200</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>239</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(200 \leq N \leq 239)$</span> </mjx-container></p>

### 출력 

 <p>지훈이가 선택해야 할 성장의 비약이 '성장의 비약 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c223C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>200</mn><mo>∼</mo><mn>209</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(200\sim 209)$</span></mjx-container>'이라면 <span style="color:#e74c3c;"><code>1</code></span>, '성장의 비약 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c223C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>200</mn><mo>∼</mo><mn>219</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(200\sim 219)$</span></mjx-container>'이라면 <span style="color:#e74c3c;"><code>2</code></span>, '성장의 비약 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mo class="mjx-n"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c223C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c32"></mjx-c><mjx-c class="mjx-c39"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo stretchy="false">(</mo><mn>200</mn><mo>∼</mo><mn>229</mn><mo stretchy="false">)</mo></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$(200\sim 229)$</span></mjx-container>'이라면 <span style="color:#e74c3c;"><code>3</code></span>, '태풍 성장의 비약'이라면 <span style="color:#e74c3c;"><code>4</code></span>를 출력한다.</p>

