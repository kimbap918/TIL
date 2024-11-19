# [Bronze II] 맥주 99병 - 17293 

[문제 링크](https://www.acmicpc.net/problem/17293) 

### 성능 요약

메모리: 31252 KB, 시간: 32 ms

### 분류

구현

### 제출 일자

2024년 11월 19일 23:01:07

### 문제 설명

<blockquote>
<p><em>99 bottles of beer on the wall, 99 bottles of beer. Take one down and pass it around, 98 bottles of beer on the wall.</em></p>

<p><em>98 bottles of beer on the wall, 98 bottles of beer. Take one down and pass it around, 97 bottles of beer on the wall.</em></p>

<p><em>(중략)</em></p>

<p><em>1 bottle of beer on the wall, 1 bottle of beer. Take one down and pass it around, no more bottles of beer on the wall.</em></p>

<p><em>No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.</em></p>
</blockquote>

<p>99 Bottles of Beer라는 노래의 가사는 Hello World처럼 프로그래밍 연습 예제로 자주 쓰인다. 우리의 목표는 <em>N</em> Bottles of Beer를 부르는 것이다. 고등학생이 맥주를 마시는 것은 <strong>세계로 미래로 꿈을 펼치는</strong> 선린인의 준법정신에 맞지 않지만 정말로 맥주를 마시는 게 아니라 노래만 부르면 되므로 상관은 없다.</p>

<p><em>N</em> Bottles of Beer의 가사는 다음 과정을 통해 만들어진다. 현재 벽에 <em>K</em>병의 맥주가 있다고 하자. 맨 처음에는 <em>K</em> = <em>N</em>이다. 이때 맥주 한 병을 따면서 다음을 출력한다.</p>

<pre><em>K</em><code> bottles of beer on the wall, </code><em>K</em><code> bottles of beer.
Take one down and pass it around, </code><em>K-1</em><code> bottles of beer on the wall.</code></pre>

<p>단, 맥주가 한 병만 있음을 표현하려면 <code>1 bottles</code>가 아니라 <code>1 bottle</code>이라고 해야 한다. 또한 맥주가 한 병도 없음을 표현하려면 <code>0 bottles</code>가 아니라 <code>no more bottles</code>라고 해야 한다.</p>

<p>맥주가 아직 남아있으면 위 과정을 반복하고, 더 이상 남아있지 않으면 다음을 출력하고 종료한다. 마찬가지로 맥주를 한 병만 사오는 경우 <code>1 bottles</code>가 아니라 <code>1 bottle</code>이라고 해야 한다.</p>

<pre><code>No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, </code><em>N</em><code> bottles of beer on the wall.</code></pre>

### 입력 

 <p>1 이상 99 이하의 자연수 <em>N</em>이 주어진다.</p>

### 출력 

 <p><em>N</em> Bottles of Beer의 가사를 출력한다.</p>

