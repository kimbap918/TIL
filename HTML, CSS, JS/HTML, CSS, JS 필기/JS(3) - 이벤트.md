## JavaScript - Event

* 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
* 이벤트 발생
  * 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있음
  * 특정 메서드를 호출(Element.click())하여 프로그래밍적으로도 만들어 낼 수 있음

<br>

#### 이벤트의 역할

이벤트의 핵심 : "~하면 ~한다."

* "대상에 특정 **이벤트가 발생**하면,  **할 일**(함수)을 등록한다."

예시) "클릭하면, 경고창을 띄운다."

<br>

* EventTarget.addEventListener(type, listener[, options])
  * type : 반응 할 이벤트 유형(대소문자 구분)
  * listener : 지정된 타입의 **이벤트가 발생했을 때** 알림을 받는 객체
    * EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 함 **(할 일)**

<br>

#### 예시 - 버튼 이벤트

[카운트 증가]

``` javascript
// 버튼 클릭시 카운트 증가 
<body>
  <button id="btn">버튼</button>
  <p id="counter">0</p>
  <script>
    // 초기값
    let countNumber = 0

    // id가 btn인 요소를 선택
    document.querySelector('#btn')
    console.log(btn)
    // btn이 클릭 되었을 때 함수가 실행됨
    btn.addEventListenter('click', function() {
      console.log('버튼 클릭!')
      // countNumber를 증가시키고
      countNumber += 1
      // id가 counter인 내용을 증가시킨다.
      const counter = document.querySelector('#counter')
      counter.innerText = countNumber
    })
  </script>
</body>
```

<br>

[input 가져오기]

``` javascript
<body>
  <input type="text" id="text-input">
  <script>
    // 1. input 선택
    const textInput = document.querySelector('#text-input')
    // 2. 
    textInput.addEventListener('input', function(e) {
      // input의 value를 받아오고 싶음
      // input은 이벤트의 대상
      console.log(e)
      console.log(e.target.value)

    }) 
  </script>
</body>
```

<br>

[이벤트 막기]

``` javascript
<body>
  <h1>정말 중요한 내용</h1>
  <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Error harum officia facilis nulla aspernatur ratione atque explicabo.</p>
  <script>
    const h1 = document.querySelect('h1')
    h1.addEventListener('copy', function(event) {
      // event의 기본 동작을 막고, 다른 행위를 할수 없게함
      event.preventDefault()
      console.log('복사를 할 수 없습니다.')
      
    h1.addEventListener('dragstart', function(event) {
      event.preventDefault()
      console.log('드래그가 금지되어 있습니다.')
    })
    })
  </script>
</body>
```

<br>

[토글하기]

``` javascript
  <style>
    .modal-overlay {
      background-color: rgba(0, 0, 0, 0.8);
      width: 100%;
      height: 100vh;
      /* 내부 내용 */
      color: white;
      justify-content: center;
      align-items: center;
      /* 기본은 안보이게 */
      display: none;
    }
    .active {
      display: flex;
    }
  </style>
</head>
<body>
  <button>모달 버튼</button>
  <div id="modal-content" class="modal-overlay">모달</div>

  <script>
    // 모달 버튼이 클릭되면
    const modalBtn = document.querySelector('#modal-btn')
    modalBtn.addEventListener('click', function() {
      // 클래스 active를 토글함
      documnet.querySelector('#modal-content').classList.toggle('active')
    })

    // 모달 취소버튼이 클릭되면
    const modalCancelBtn = document.querySelector('#modal-cancel-btn')
    modalCancelBtn.addEventListener('click', function() {
      document.querySelector('#modal-content').classList.toggle('active')
    })
  </script>
</body>
```

