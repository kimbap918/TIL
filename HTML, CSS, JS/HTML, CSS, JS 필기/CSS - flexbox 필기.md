## Flexbox

#### Flexible Box Module

* 인터페이스 내의 아이템 간 공간 배분과 정렬 기능을 제공하기 위한 1차원 레이아웃 모델

* 레이아웃을 다룰 때 한 번에 하나의 차원(행 or 열)만을 다루기때문에 flexbox는 1차원이며 CSS 그리드 레이아웃의 2차원 모델과는 대조됨.

<br>

#### Flexbox의 두 개의 축

1. 주축 : `flex-direction`에 의해 정의되며 4개의 값을 가질 수 있다.

   * row

   * row-reverse

     * row 혹은 row-reverse를 선택하면 주축은 **인라인 방향**으로 행을 따른다.

   * column

   * column-reverse

     * column 혹은 column-reverse를 선택하면 주축은 페이지 상단에서 하단으로 **블록 방향**을 따른다.

     ![flex-direction](CSS - flexbox 필기.assets/flex-direction.jpeg)

2. 교차축 

   * 교차축은 주축에 수직한다. 만약 주축이 row나 row-reverse라면 교차축은 열 방향을 따른다.
   * 주축이 column혹은 column-reverse라면 교차축은 행 방향을 따른다.

![cross-axis](CSS - flexbox 필기.assets/cross-axis.jpeg)

flex 요소를 정렬하고 맞추려면 어느 축이 어느 방향인지 이해하는것이 중요하다. flex는 주축, 교차축을 따라 항목을 정렬하고 끝을 맞추는 각종 속성들을 적용하는 방식으로 동작한다.

<br>

#### 시작선과 끝선

과거의 CSS는 왼쪽에서 오른쪽으로 향하는 가로 방향의 쓰기 방법에 치우쳐있었지만 현대의 레이아웃은 다양한 쓰기 방법을 포괄해야하므로 더 이상 텍스트가 문서의 왼쪽 상단에서 시작해서 오른쪽으로 향한다고 가정하지 않는다.

<br>

시작선과 끝선은 주 축이나 교차 축의 시작하는 지점과 끝나는 지점을 지칭하며 방향에 따라 시작선과 끝선이 달라진다.

![start-end](CSS - flexbox 필기.assets/start-end.jpeg)

<br>

#### flex 컨테이너

문서의 영역 중 flexbox가 놓여있는 영역을 **flex컨테이너** 라고 부른다. flex 컨테이너를 생성하려면 영역 내의 컨테이너 요소의 display 값을 `flex` 혹은 `inline-flex`로 지정한다.

flex 컨테이너를 생성하면 다른 flex 관련 속성들은 아래처럼 기본 값 지정된다.

* 항목은 행으로 나열(`flex-direction` 속성의 기본값 `row` 이기때문)
* 항목은 주축의 시작 선에서 시작됨
* 항목은 주 차원 위에서 늘어나지는 않지만 줄어들 수 있다
* 항목은 교차축의 크기를 채우기 위해 늘어난다
* `flex-basis` 속성은 auto로 지정된다
* `flex-wrap` 속성은 `nowrap` 으로 지정된다

<br>

#### flex-wrap

* Items의 여러 줄 묶음(줄바꿈)을 설정한다

| 값           | 의미                                           | 기본값  |
| ------------ | ---------------------------------------------- | ------- |
| nowrap       | 모든 Items를 여러 줄로 묶지 않음(한 줄에 표시) | no wrap |
| wrap         | Items를 여러 줄로 묶음                         |         |
| wrap-reverse | Items를 wrap의 역 방향으로 여러 줄로 묶음      |         |

기본적으로 items는 한 줄에서만 표시되고 줄 바꿈 되지 않는데 이는 지정된 크기(주 축에 따라 width나 height)를 무시하고 한 줄 안에서만 가변한다.

items를 줄 바꿈 하려면 값으로 wrap을 사용해야 한다.

![flex-wrap](CSS - flexbox 필기.assets/flex-wrap.jpeg)

<br>

#### justify-content

주 축(main-axis)의 정렬 방법을 설정한다

| 값            | 의미                                                         | 기본값     |
| ------------- | ------------------------------------------------------------ | ---------- |
| flex-start    | Items를 시작선(flex-start)으로 정렬                          | flex-start |
| flex-end      | Items를 끝선(flex-start)으로 정렬                            |            |
| center        | Items를 가운데 정렬                                          |            |
| space-between | 시작 Item은 시작점에, 마지막 Item은 끝점에 정렬되고 나머지 Items는 사이에 고르게 정렬됨 |            |
| space-around  | Items를 균등한 여백을 포함해서 정렬                          |            |

![justify-content](CSS - flexbox 필기.assets/justify-content.jpeg)

<br>

#### align-content

* 교차 축(cross-axis)의 정렬 방법을 설정한다.

* 주의할 점은 flex-wrap 속성을 통해 Items가 여러 줄(2줄 이상)이고 여백이 있을 경우만 사용할 수 있다.

* Items가 한 줄일 경우 align-items 속성을 사용해야한다.

| 값            | 의미                                                         | 기본값  |
| ------------- | ------------------------------------------------------------ | ------- |
| stretch       | Container의 교차 축을 채우기 위해 Items를 늘림               | stretch |
| flex-start    | Items를 시작점(flex-start)으로 정렬                          |         |
| flex-end      | Items를 끝점(flex-end)으로 정렬                              |         |
| center        | Items를 가운데 정렬                                          |         |
| space-between | 시작 item은 시작점에, 마지막 Item은 끝점에 정렬되고 나머지 Items는 사이에 고르게 정렬됨 |         |
| space-around  | Items를 균등한 여백을 포함하여 정렬                          |         |

align-content 정렬방법

값 stretch는 교차 축에 해당하는 너비(속성 width 혹은 height)가 값이 auto(기본값)일 경우 교차 축을 채우기 위해 자동으로 늘어난다.

![align-content](CSS - flexbox 필기.assets/align-content.jpeg)

<br>

#### align-items

* 교차 축(cross-axis)에서 Items의 정렬 방법을 설정한다

* Items가 한 줄일 경우 많이 사용한다.

<br>

주의할 점은 Items가 flex-wrap을 통해 여러 줄(2줄 이상)일 경우에는 align-content 속성이 우선한다. 따라서 align-items를 사용하려면 align-content 속성을 기본값(stretch)으로 설정해야한다.

| 값         | 의미                                           | 기본값  |
| ---------- | ---------------------------------------------- | ------- |
| stretch    | Container의 교차 축을 채우기 위해 Items를 늘림 | stretch |
| flex-start | Items를 각 줄의 시작점(flex-start)으로 정렬    |         |
| flex-end   | Items를 각 줄의 끝점(flex-end)으로 정렬        |         |
| center     | Items를 가운데 정렬                            |         |
| baseline   | Items를 문자 기준선에 정렬                     |         |

align-items 정렬방법

![align-item](CSS - flexbox 필기.assets/align-item.jpeg)

<br>

#### Flex Items

Flex Items를 위한 속성은 다음과 같다

| 속성         | 의미                                            |
| ------------ | ----------------------------------------------- |
| order        | Flex Item의 순서를 설정                         |
| flex         | flex-griw, flex-shrink, flex-basis의 단축 속성  |
| flex-grow    | Flex Item의 증가 너비 비율을 설정               |
| flex-shirink | Flex Item의 감소 너비 비율을 설정               |
| flex-basis   | Flex Item의 (공간 배분 전) 기본 너비 설정       |
| align-self   | 교차 축(cross-axis)에서 Item의 정렬 방법을 설정 |

<br>

#### order

* Item의 순서를 설정한다

* Item에 숫자를 지정하고 숫자가 클수록 순서가 밀린다.

* 음수가 허용된다

* HTML 구조와 상관없이 순서를 변경할수 있어 매우 유용하다

| 값   | 의미               | 기본값 |
| ---- | ------------------ | ------ |
| 숫자 | Item의 순서를 설정 | 0      |

![order](CSS - flexbox 필기.assets/order.jpeg)

<br>

#### flex

Item의 너비(증가, 감소, 기본)를 설정하는 단축 속성

| 값          | 의미                         | 기본값 |
| ----------- | ---------------------------- | ------ |
| flex-grow   | Item의 증가 너비 비율을 설정 | 0      |
| flex-shrink | Item의 감소 너비 비율을 설정 | 1      |
| flex-basis  | Item                         | auto   |

``` CSS
.item {
  flex: 1 1 20px; /* 증가너비, 감소너비, 기본너비 */
 	flex: 1 1; /* 증가너비, 감소너비 */
  flex: 1 20px; /* 증가너비, 기본너비 */
  
  flex-grow: 증가너비;
  flex-shrink: 감소너비;
  flex-basis: 기본너비;
}
```

[flex-grow]

![flex-grow](CSS - flexbox 필기.assets/flex-grow.jpeg)

[flex-shrink]

![flex-shirink](CSS - flexbox 필기.assets/flex-shirink.jpeg)

[flex-basis]![flex-basis](CSS - flexbox 필기.assets/flex-basis.jpeg)