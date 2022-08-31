## CSS position

#### CSS 원칙

* CSS 원칙 I, II : Normal flow
  * 모든 요소는 네모(박스모델), 좌측상단에 배치
  * display에 따라 크기와 배치가 달라짐
* CSS 원칙 III
  * **position으로 위치의 기준을 변경**

<br>

#### CSS position

* 문서 상에서 요소의 위치를 지정

* **static** : 모든 태그의 기본 값(기준 위치)

  * **일반적인 요소의 배치 순서에 따름(좌측 상단)**

  * 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨

    ``` CSS
    div {
      height: 100px;
      width: 100px;
      background-color: #9775fa;
      color: black;
      line-height: 100px;
      text-align: center;
    }
    ```

* 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능

  * 1. relative : 상대 위치

       * 자기 자신의 static 위치를 기준으로 이동(**normal flow 유지**)

       * 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음

         ``` CSS
         /* 기존 위치(normal position) 대비 offset이 일어남 */
         .relative {
           position: relative;
           top: 100px;
           left: 100px;
         }
         ```

         

    2. absolute : 절대 위치

       * 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(**normal flow에서 벗어남**)

       * static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 브라우저 화면 기준으로 이동)

         ``` CSS
         .parent {
           position: relative;
         }
         
         /* normal flow 에서 벗어나 부모/조상 요소를 기준으로 위치 */
         .absolute-child {
           position: absolute;
           top: 50px;
           left: 50px;
         }
         ```

         

    3. fixed : 고정 위치

       * 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
       * 부모 요소와 관계없이 **viewport**를 기준으로 이동
       * 스크롤 시에도 항상 같은 곳에 위치함

    4. sticky : 스크롤에 따라 static -> fixed로 변경

       * 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성

<br>

#### absolute는 언제 쓸까?

특정 영역 위에 존재하기 때문에 홈페이지 화면 사진 내의 버튼같이 부모를 기준으로 위치를 정할때 사용

#### fixed는 언제 쓸까?

브라우저를 기준으로 위치시키는 메뉴화면이나 상단이동 버튼등을 위치시킬때 사용



## CSS Layout

#### Float

* 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 wrapping 하도록 함

* 요소가 Normal flow를 벗어나도록 함

  ``` CSS
  .box {
    width: 150px;
    height: 150px;
    border: 1px solid black;
    background-color: crimson;
    color: white;
    margin-right: 30px;
  }
  
  .left {
    float: left;
  }
  ```

<br>

## Flex Box

#### Flex 속성

* 배치 설정

  * flex-direction
    * Main axis 기준 방향 설정
    * 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의(웹 접근성에 영향)
  * flex-wrap
    * 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
    * 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함
    * nowrap(기본 값) : 한 줄에 배치
    * wrap : 넘치면 그 다음줄로 배치

* 공간 나누기

  * justify-content(main axis)
    * Main axis를 기준으로 공간 배분
    * 1. flex-start
      2. flex-end
      3. center
      4. space-between
      5. space-around
      6. space-evenly

* 정렬

  * align-items(모든 아이템을 cross axis 기준으로)
    * 1. stretch
      2. flex-start
      3. flex-end
      4. center
      5. baseline
  * align-self
    * 개별 아이템을 cross axis 기준으로 정렬
    * **해당 속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용**
    * 1. stretch
      2. flex-start
      3. flex-end
      4. center

* 기타 속성

  * flex-grow 
    * 남은 영역을 아이템에 분배
  * order 
    * 배치 순서

  

  

  