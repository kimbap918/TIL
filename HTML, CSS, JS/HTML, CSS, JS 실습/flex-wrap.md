## flex-wrap

1. flex-wrap은 기본적으로 **display : flex; 가 적용된 요소**에 사용된다. flex-wrap은 플렉스 컨테이너 내의 아이템들의 줄 바꿈 동작을 제어하는데에 사용된다.

#### html
``` html
<div class="flex-items">내용</div>
<div class="flex-items">내용</div>  
<div class="flex-items">내용</div>  
```

#### css
``` css
.flex-items {  
   display: flex; /* 요소를 유연한(flexible) 박스 모델로 만드는데 사용된다. 이것을 flex container라고 한다. */
   flex-wrap: nowrap;  /* flex 속성 지정 */
   min-width: 110px;  
   height: 50px;  
   background: #999;  
   border-radius: 2px;  
   margin: 3px;  
}  
```


2. flex-wrap속성에는 세 가지 값이 존재한다.
 - nowrap(기본값) : 아이템들이 한 줄에 모두 배치된다. 화면이 너무 작은 경우 오버플로우가 생길수 있다.
![](https://i.imgur.com/RYmFj2s.png)

* wrap : 아이템들이 필요에 따라 여러 줄로 나뉘어 배치된다. 만약 아이템들이 가로 공간을 초과하면 다음 줄로 이동한다.

![](https://i.imgur.com/x3wUJ3g.png)


* wrap-reverse : 아이템들의 배치 순서가 역순으로 변경
![](https://i.imgur.com/NB0wNYT.png)
