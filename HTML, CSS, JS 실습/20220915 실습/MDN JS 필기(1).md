## JavaScript

웹 페이지에서 복잡한 기능을 구현할 수 있도록 하는 스크립팅 언어 또는 프로그래밍 언어. 페이지가 정적인 정보만 보여주는게 아니라 주기적으로 갱신되거나, 사용자와 상호작용하거나, 애니메이션이 적용된 2D/3D 그래픽을 볼 수 있다면 JavaScript가 관여하고 있다고 볼 수 있다.

* JavaScript는 동적으로 콘텐츠를 바꾸고, 멀티미디어를 제어하고, 애니메이션을 추가하는 등 거의 모든 것을 만들 수 있는 스크립팅 언어다.

<br>

HTML로 아래와 같이 텍스트에 구조와 목적을 부여할 수 있다.

``` html
<p>Player 1: Chris</p>
```

<br>

CSS를 추가해서 보기 좋게 꾸밀 수 있다.

``` css
p {
  font-family: 'helvetica neue', helvetica, sans-serif;
  letter-spacing: 1px;
  text-transform: uppercase;
  text-align: center;
  border: 2px solid rgba(0, 0, 200, 0.6);
  background: rgba(0, 0, 200, 0.3);
  color: rgba(0, 0, 200, 0.6);
  box-shadow: 1px 1px 2px rgba(0, 0, 200, 0.4);
  border-radius: 10px;
  padding: 3px 10px;
  display: inline-block;
  cursor: pointer;
}
```

<br>

JavaScript를 넣어 동적인 기능을 추가한다.

``` javascript
const para = document.querySelector('p');

para.addEventListener('click', updateName);

function updateName() {
  const name = prompt('Enter a new name');
  para.textContent = `Player 1: ${name}`;
}
```

<br>

완성된 텍스트 확인해보기 

https://mdn.github.io/learning-area/javascript/introduction-to-js-1/what-is-js/javascript-label.html

<br>

JavaScript는 DOM (Document Object Model) API를 통해 HTML과 CSS를 동적으로 수정, 사용자 인터페이스를 업데이트하는 일에 가장 많이 쓰인다. 

참고로 웹 문서(페이지)의 코드는 보통 문서 상에 나타나는 순서 그대로 불러와 실행하는데. 수정하려는 HTML과 CSS 코드보다 JavaScript를 먼저 불러와 실행해버리면 오류가 발생할 수 있다.

<br>

#### 내부 JavaScript

[js.html]

``` html
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Apply JavaScript example</title>
  </head>
	 <script>

  // JavaScript goes here
    document.addEventListener('DOMContentLoaded', () => {
    function createParagraph() {
      const para = document.createElement('p');
      para.textContent = 'You clicked the button!';
      document.body.appendChild(para);
    }

    const buttons = document.querySelectorAll('button');

    for (const button of buttons) {
      button.addEventListener('click', createParagraph);
    }
  });
	</script>
  <body>
    <button>Click me</button>
  </body>
</html>
```

<br>

외부 JavaScript

[js.html]

``` html
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Apply JavaScript example</title>
  </head>
	<script src="script.js" defer></script>
  <body>
    <button>Click me</button>
  </body>
</html>
```

<br>

[script.js]

``` javascript
function createParagraph() {
  const para = document.createElement('p');
  para.textContent = 'You clicked the button!';
  document.body.appendChild(para);
}

const buttons = document.querySelectorAll('button');

for (const button of buttons) {
  button.addEventListener('click', createParagraph);
}
```

작동 화면 : https://mdn.github.io/learning-area/javascript/introduction-to-js-1/what-is-js/apply-javascript-internal.html

<br>

이외에도 HTML 내부에서 JS를 쓰는 방법도 있지만 HTML과 JS가 섞여 보기도 불편할 뿐더러 비효율적이다. 그래서 이 방법 대신 addEventListener를 사용하면 좋다.

#### addEventListener 사용하기

``` javascript
const buttons = document.querySelectorAll('button');

for (const button of buttons) {
  button.addEventListener('click', createParagraph);
}
```

querySelectorAll() 함수를 사용해서 현재 페이지의 모든 버튼을 선택하고, 반복과 addEventListener() 로 버튼 하나씩 클릭에 대한 처리를 한다.

<br>

<br>

그래서 아래의 외부 예제에서는 defer 를 사용해 문제 발생을 예방한다. `defer` 특성은 브라우저가 `<script>` 태그를 마주쳐도 그 이후의 HTML 콘텐츠를 계속 불러오도록 지정한다.

```
<script src="script.js" defer></script>
```

이렇게 하면 스크립트와 HTML을 동시에 불러오므로 오류가 발생하지 않는다. (내부 JS에서는 사용할수 없다)

<br>

#### async와 defer

스크립트 중단 문제를 해결할 수 있는 기능에는 두 가지가 있는데 `async`와 `defer` 가 있다.

`async` 특성을 지정하면 스크립트를 가져오는 동안 페이지 로딩을 중단하지 않는다. 하지만 스크립트 다운로드가 끝나면 바로 실행되는데, 실행 도중에는 페이지 렌더링이 중단된다.  `async`는 다른 스크립트에 의존하지 않는 독립 스크립트에 사용해야 한다.

`defer` 특성을 지정한 스크립트는 페이지 내에 배치한 순서대로 불러오게 된다. 또한 페이지 콘텐츠를 모두 불러오기 전까지는 실행하지 않으므로, 페이지 요소를 수정하거나 추가하는 등 DOM 작업을 기대하는 스크립트에 유용하다.

다음은 세 개의 스크립트 로딩 전략을 적용했을 때 페이지에 어떤 영향을 주는지 시각적으로 표현한 이미지다.

![img](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript/async-defer.jpg)

#### 