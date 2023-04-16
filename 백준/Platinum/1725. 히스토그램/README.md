# [Platinum V] 히스토그램 - 1725 

[문제 링크](https://www.acmicpc.net/problem/1725) 

### 성능 요약

메모리: 42836 KB, 시간: 132 ms

### 분류

자료 구조, 세그먼트 트리, 분할 정복, 스택

### 문제 설명

<p>히스토그램에 대해서 알고 있는가? 히스토그램은 아래와 같은 막대그래프를 말한다.</p>

<p style="text-align: center;"><img alt="" height="168" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/upload/201006/hist.PNG" width="231"></p>

<p>각 칸의 간격은 일정하고, 높이는 어떤 정수로 주어진다. 위 그림의 경우 높이가 각각 2 1 4 5 1 3 3이다.</p>

<p>이러한 히스토그램의 내부에 가장 넓이가 큰 직사각형을 그리려고 한다. 아래 그림의 빗금 친 부분이 그 예이다. 이 직사각형의 밑변은 항상 히스토그램의 아랫변에 평행하게 그려져야 한다.</p>

<p style="text-align: center;"><img alt="" height="166" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/upload/201006/histo.PNG" width="236"></p>

<p>주어진 히스토그램에 대해, 가장 큰 직사각형의 넓이를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 행에는 N (1 ≤ N ≤ 100,000) 이 주어진다. N은 히스토그램의 가로 칸의 수이다. 다음 N 행에 걸쳐 각 칸의 높이가 왼쪽에서부터 차례대로 주어진다. 각 칸의 높이는 1,000,000,000보다 작거나 같은 자연수 또는 0이다.</p>

### 출력 

 <p>첫째 줄에 가장 큰 직사각형의 넓이를 출력한다. 이 값은 20억을 넘지 않는다.</p>

