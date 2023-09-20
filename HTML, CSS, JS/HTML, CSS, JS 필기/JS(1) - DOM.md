## JavaScript

JavaScript의 필요성

* 브라우저 화면을 '동적'으로 만들기 위함
* 브라우저를 조작할 수 있는 유일한 언어

<br>

## DOM(Document Object Model)

**브라우저에서 할 수 있는 일**

* DOM 조작
  * 문서  HTML조작
* BOM 조작
  * navigator, screen, location, frames, history, XHR
* JavaScript Core(ECMA Script)
  * Data Structure(Object, Array), Conditional Expression, Iteration

<br>

#### DOM?

* HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
* 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
* 문서가 구조화되어 있으며 각 요소는 객체로 취급
* 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
* 주요 객체
  * window : DOM을 표현하는 창, 가장 최상위 객체(작성시 생략 가능)
  * document : 페이지 컨텐츠의 Entry Point 역할을 하며, `<body>` 등과 같은 수많은 다른 요소들을 포함
  * navigator, location, history, screen

<br>

#### DOM - 해석

* 파싱(Parsing)
  * 구문 분석, 해석
  * 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

<br>

## BOM(Browser Object Model)

* 자바스크립트가 브라우저와 소통하기 위한 모델
* 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
  * 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능
* window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창을 지칭

<br>

## JavaScript Core

* 프로그래밍 언어

<br>

**브라우저(BOM)과 그 내부의 문서(DOM)를 조작하기 위해 ECMAScript(JS)를 학습**

<br>

## DOM 조작

* Document 는 문서 한 장에 해당하고(HTML) 이것을 조작한다.
* DOM 조작 순서 
  * 선택(Select)
  * 변경(Manipulation)

#### 선택(Select)

``` html
<body>
  <h1 id="title">JS 기초</h1>
  <h2>DOM 조작</h2>
  <!-- 웹 페이지 콘솔 querySelector에서 id가 title인
  값을 가져오려면? document.querySelector('#title')
  -->

  <!-- 선택자를 활용해 선택할 때
  하나를 선택한다. => querySelector
  모든 결과를 선택한다. => querySelectorAll -->
  <p class="text">querySelector</p> 
  <p class="text">querySelectorALL</p>

  <script>
    console.log(document.querySelectorAll('#title'))
    // <h1 id="title">JS 기초</h1>
    console.log(document.querySelectorAll('.text'))
    // NodeList(2) [p.text, p.text]
    console.log(document.querySelector('.text'))
    // <p class="text">querySelector</p>

  </script>
</body>
```

<br>

#### 속성(Attribute)

``` html
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .red {
      color : red;
    }
    .blue {
      color : blue;
    }
  </style>
</head>
<body>
  <h1 class="red text-center my-5">안녕하세요</h1>
  <script>
    const a = document.createElement('a')
    a.innerText = '실라버스'
    const body = document.querySelector('body')
    body.appendchild(a)
    // a에 속성을 붙혀서 사용할 수 있음
    a.setAttribute('href', 'https://syllaverse.com')
    // a에 있는 속성을 가져올 수 있음  
    console.log(a.getAttribute('href'))

    // h1 태그 조작(클래스)
    const h1 = documnet.querySelector('h1')
    // h1.getAttribute('class')
    // // 'red'
    // h1.setAttribute('class', 'blue')
    // // 'blue'로 변경됨
    console.log(h1.classList)
  </script>
</body>
```

<br>

#### 이벤트(Event)

``` html
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .blue {
      color : blue;
    }
  </style>
</head>
<body>
  <button id="btn1">클릭</button>
  <script>
    // btn1
    const btn1 = document.querySelector('#btn1')
    // btn1이 클릭되면 함수 실행
    btn1.addEventListener('click', function(){
      // h1 태그를 잡아서
      const h1 = document.querySelector('h1')
      // 클래스 blue를 토글
      h1.classList.toggle('blue')
    })
    
    // input
    const input = document.querySelector('input')
    input.addEventListener('input', function() {
      console.log(e.target.value)
    })
  </script>
</body>
```

<br>

