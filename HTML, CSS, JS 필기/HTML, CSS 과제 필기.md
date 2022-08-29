## HTML

**H**yper **T**ext **M**arkup **L**anguage

* 웹을 이루는 가장 기초적인 구성 요소
* 웹 콘텐츠의 **의미**와 **구조**를 정의할때 사용

<br>

**Hypertext**(하이퍼텍스트)란?

* 웹 페이지를 다른 페이지로 연결하는 링크

<br>

#### HTML의 요소

HTML은 웹 브라우저에 표시되는 글과 이미지등의 콘텐츠를 표시하기 위해 **Markup**을 사용한다. HTML 마크업은 다양한 요소를 사용하는데 요소의 종류에는

`<head>`, `<title>`, `<body>`, `<header>`, `<footer>`, `<article>`, `<section>`, `<p>`, `<div>`, `<span>`, `<img>`, `<aside>`, `<audio>`, `<canvas>`, `<datalist>`, `<details>`, `<enbed>`, `<nav>`, `<output>`, `<progress>`, `<video>`, `<ul>`, `<ol>`, `<li>` 등 많은 종류가 있다.

``` html
<!-- a태그(anchor) 링크를 표현> -->
<a href="https://google.com">구글</a> 

<!-- b태그(bold) -->
<b>굵은 글씨</b>
<!-- 강조 -->
<strong>강한 글씨?</strong>

<!-- i태그(italic) -->
<i>italic</i>
<!-- 기울임 강조 -->
<em>강한 글씨?</em>

<!-- heading -->
<h1></h1>
<h2></h2>
<h6></h6>

<!-- 줄바꿈 -->
<br>

<!-- 띄워쓰기 -->
&nbsp;

<!-- img -->
<!-- alt는 대체 텍스트 -->
<img src="https://item.kakaocdn.net/do/2e134bd9f0af46e1e661fcf6240cfebfa88f7b2cbb72be0bdfff91ad65b168ab" alt="농담곰">

<!-- 문단 -->
<p>
  문단
</p>

<!-- 수평선 -->
<hr>

<!-- ol(ordered list), ul(unordered list) -->
<ol>
	<li>순서가 있음</li>
</ol>

<ul>
  <li>순서가 없음</li>
</ul>

<!-- 인용문 -->
<blockquote></blockquote>
```

<br>

#### 그 외의 각종 요소들

https://developer.mozilla.org/ko/docs/Web/HTML/Element

<br>

#### HTML의 특성

* HTML의 요소들은 특성을 가지고 있다.
* 특성은 사용자가 원하는 기준에 맞도록 요소를 설정하거나 다양한 방식으로 요소의 동작을 조절하기 위한 값이다.

<br>

#### HTML의 특성 목록 참고

https://developer.mozilla.org/ko/docs/Web/HTML/Attributes

<br>

## CSS

**C**ascading **S**tyle **S**heet

* HTML이나 XML로 작석된 문서의 표시 방법을 기술하기 위한 스타일 시트 언어
* 요소가 화면, 종이, 음성이나 다른 매체 상에 어떻게 렌더링 되어야 하는지 지정

* 웹 페이지의 **모양**, **표현**에 사용

<br>

#### CSS 구문

``` css
h1(선택자) {
  color : blue;(선언)
  font-size(속성): 15px;(값)
}
```

<br>

#### CSS의 ruleset

- **선택자**(selector) : rule set의 맨 앞에 있는 HTML 요소 이름. 꾸밀 요소를 선택한다.
- **선언** : color : red와 같은 단일 규칙, 꾸미기 원하는 요소의 속성을 명시한다.
- **속성**(property) : 주어진 HTML 요소를 꾸밀 수 있는 방법. 예시에서 blue는 h1요소의 속성이다. CSS에서, rule 내에서 영향을 줄 속성을 선택한다.
- **속성 값** : 속성의 오른쪽에, 콜론 뒤에 주어진 속성을 위한 많은 가능한 결과중 하나를 선택하기 위해 속성 값을 갖는다. (color 안에는 여러가지 색이 있다.)

<br>

#### rule set의 작성 규칙

* 각각의 rule set(셀렉터로 구분)은 반드시 (`{}`)로 감싸져야 한다.

* 각각의 선언 안에, 각 속성을 해당 값과 구분하기 위해 콜론(:)을 사용해야만 한다.

* 각각의 rule set안에, 각 선언을 그 다음 선언으로부터 구분하기 위해 세미콜론(;)을 사용해야만 한다.

  ``` CSS
  p {
    color: red;
    width: 500px;
    border: 1px solid black;
  }
  
  /* 콤마로 구분하여 여러가지 요소 선택 가능 */
  p,li,h1 {
    color: red;
  }
  ```

<br>

#### 선택자의 종류

| 선택자 이름                                       | 선택하는 것                                                  | 예시                                                         |
| :------------------------------------------------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 요소 선택자 (때때로 태그 또는 타입 선택자라 불림) | 특정 타입의 모든 HTML 요소.                                  | `p` `<p> 를 선택`                                            |
| 아이디 선택자                                     | 특정 아이디를 가진 페이지의 요소 (주어진 HTML 페이지에서, 아이디당 딱 하나의 요소만 허용됩니다). | `#my-id` `<p id="my-id">`또는 `<a id="my-id">` 를 선택       |
| 클래스 선택자                                     | 특정 클래스를 가진 페이지의 요소 (한 페이지에 클래스가 여러번 나타날 수 있습니다). | `.my-class` `<p class="my-class">` 와 `<a class="my-class">` 를 선택 |
| 속성 선택자                                       | 특정 속성을 갖는 페이지의 요소.                              | `img[src]` `<img src="myimage.png">` 를 선택하지만 `<img> `는 선택 안함 |
| 수도(Pseudo) 클래스 선택자                        | 특정 요소이지만 특정 상태에 있을 때만, 예를 들면, hover over 상태일 때. | `a:hover` `<a>` 를 선택하지만, 마우스 포인터가 링크위에 있을 때만 선택함 |

<br>

#### 더 많은 선택자 알아보기

https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors

<br>

## 웹 접근성 경험하고 느낀점 작성하기

굉장히 불편했다. 휴대폰에도 고대비 보기가 있었는데 이게 저시력 시각장애를 위한 화면인지는 잘 모르고있었다. 그래도 여기까진 괜찮았는데 손 운동장애로 넘어가니 계산기를 두드리는게 짜증날정도로 마우스 휠이 이리저리 움직였다. 오늘 배운 것중에 대체 텍스트가 있었는데 이게 왜 필요한지, 왜 마음대로 적으면 안되는지 알게됐다. 인터넷은 다양한 사람들이 사용하고 있고, 그만큼 신체조건이 다양한 사람들이 있다. 웹 개발을 한다는건 이러한 특성을 가진 사람 모두를 고려해서 개발해야한다는걸 느꼈다.