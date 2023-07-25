# [Gold III] 양팔저울 - 2629 

[문제 링크](https://www.acmicpc.net/problem/2629) 

### 성능 요약

메모리: 31256 KB, 시간: 56 ms

### 분류

다이나믹 프로그래밍, 배낭 문제

### 문제 설명

<p>양팔 저울과 몇 개의 추가 주어졌을 때, 이를 이용하여 입력으로 주어진 구슬의 무게를 확인할 수 있는지를 결정하려고 한다.</p>

<p>무게가 각각 1g과 4g인 두 개의 추가 있을 경우, 주어진 구슬과 1g 추 하나를 양팔 저울의 양쪽에 각각 올려놓아 수평을 이루면 구슬의 무게는 1g이다. 또 다른 구슬이 4g인지를 확인하려면 1g 추 대신 4g 추를 올려놓으면 된다.</p>

<p>구슬이 3g인 경우 아래 <그림 1>과 같이 구슬과 추를 올려놓으면 양팔 저울이 수평을 이루게 된다. 따라서 각각 1g과 4g인 추가 하나씩 있을 경우 주어진 구슬이 3g인지도 확인해 볼 수 있다.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/ce5b29f5-9e03-473b-97db-ce9fd740fde2/-/preview/" style="width: 255px; height: 163px;"></p>

<p style="text-align: center;"><그림 1> 구슬이 3g인지 확인하는 방법 (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-menclose><mjx-box style="border: 0.067em solid; padding: 0.2em;"><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-texatom texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-mstyle></mjx-texatom></mjx-box></mjx-menclose></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="box"><mrow data-mjx-texclass="ORD"><mstyle displaystyle="true" scriptlevel="0"><mrow data-mjx-texclass="ORD"><mn>1</mn></mrow></mstyle></mrow></menclose></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\boxed{1}$</span></mjx-container>은 1g인 추, <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-menclose><mjx-box style="border: 0.067em solid; padding: 0.2em;"><mjx-texatom texclass="ORD"><mjx-mstyle><mjx-texatom texclass="ORD"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-texatom></mjx-mstyle></mjx-texatom></mjx-box></mjx-menclose></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><menclose notation="box"><mrow data-mjx-texclass="ORD"><mstyle displaystyle="true" scriptlevel="0"><mrow data-mjx-texclass="ORD"><mn>4</mn></mrow></mstyle></mrow></menclose></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$\boxed{4}$</span></mjx-container>는 4g인 추, ●은 무게를 확인할 구슬)</p>

<p><그림 2>와 같은 방법을 사용하면 구슬이 5g인지도 확인할 수 있다. 구슬이 2g이면 주어진 추를 가지고는 확인할 수 없다.</p>

<p>추들의 무게와 확인할 구슬들의 무게가 입력되었을 때, 주어진 추만을 사용하여 구슬의 무게를 확인 할 수 있는지를 결정하는 프로그램을 작성하시오.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/883fb22a-7516-46e1-937d-2ddc4df94572/-/preview/" style="width: 255px; height: 163px;"></p>

<p style="text-align: center;"><그림 2> 구슬이 5g인지 확인하는 방법</p>

### 입력 

 <p>첫째 줄에는 추의 개수가 자연수로 주어진다. 추의 개수는 30 이하이다. 둘째 줄에는 추의 무게들이 자연수로 가벼운 것부터 차례로 주어진다. 같은 무게의 추가 여러 개 있을 수도 있다. 추의 무게는 500g이하이며, 입력되는 무게들 사이에는 빈칸이 하나씩 있다. 세 번째 줄에는 무게를 확인하고자 하는 구슬들의 개수가 주어진다. 확인할 구슬의 개수는 7이하이다. 네 번째 줄에는 확인하고자 하는 구슬들의 무게가 자연수로 주어지며, 입력되는 무게들 사이에는 빈 칸이 하나씩 있다. 확인하고자 하는 구슬의 무게는 40,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>주어진 각 구슬의 무게에 대하여 확인이 가능하면 Y, 아니면 N 을 차례로 출력한다. 출력은 한 개의 줄로 이루어지며, 각 구슬에 대한 답 사이에는 빈칸을 하나씩 둔다.</p>

