## Reboot

단일 파일에 있는 요소별 CSS의 변경모음

<br>

#### 접근

- 확장 가능한 컴포넌트 간격에 `em` 대신`rem`을 사용하도록 기본값을 업데이트함.
- 수직 margin은 구조적으로 불안정하며, 예상치 못한 결과를 가져올 수 있기 때문에 `margin-top`을 제외한다. 더 중요한 것은 단방향 `margin`이 더 단순한 멘탈 모델이기 때문이다.
- 더 쉬운 기기 간 크기 확장을 위해서 블럭 요소의 `margin`에 `rem`을 사용한다.
- 가능하면 `inherit`를 사용하여 `font` 관련 속성의 선언을 최소한으로 유지한다.

<br>

## 페이지 기본값

`<html>` 과 `<body>` 요소는 더 넒은 페이지를 제공하기 위해 갱신된다. 구체적으로는 다음과 같다.

box-sizing은 *::before및 *::after를 포함한 모든 요소에서 **border-box**로 전역적으로 설정된다. 이렇게 하면 요소의 선언된 너비가 패딩이나 테두리로 인해 초과되지 않는다.

- `<html>`에는 기본 `font-size`가 선언되지 않지만 `16px`로 가정되며 (브라우저 기본값). `font-size: 1rem` 은 `<body>`에 적용된다. 이 브라우저 기본값은 `$font-size-root` 변수를 수정하여 재정의할 수 있습니다.

- `<body>`는 전역 `font-family`, `font-weight`, `line-height`,`color`도 설정한다. 이것은 나중에 글꼴 불일치를 방지하기 위해 일부 폼 요소에 의해 상속된다.
- 안전을 위해서 `<body>`에는 선언된 `background-color`가 있으며 기본값은`#fff`다.

<br>

## 기본 글꼴 스택

Bootstrap은 모든 장치 및 OS에서 최적의 텍스트 렌더링을 위해 “기본 글꼴 스택” 또는 “시스템 글꼴 스택"을 사용한다. 

```scss
$font-family-sans-serif:
  // Cross-platform generic font family (default user interface font)
  system-ui,
  // Safari for macOS and iOS (San Francisco)
  -apple-system,
  // Windows
  "Segoe UI",
  // Android
  Roboto,
  // Basic web fallback
  "Helvetica Neue", Arial,
  // Linux
  "Noto Sans",
  "Liberation Sans",
  // Sans serif fallback
  sans-serif,
  // Emoji fonts
  "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji" !default;
```

<br>

## CSS 변수

부트스트랩에서는 Sass 변수를 가져와 CSS 변수로 변환하는데, 이렇게 하면 CSS 변수를 사용하지 않더라도 여전히 Sass의 모든 기능을 사용할 수 있다.

일반적인 `<body>` 스타일에 대해 다음 `:root` CSS 변수.

```scss
  @if $font-size-root != null 
    --#{$variable-prefix}root-font-size: #{$font-size-root};
  }
  --#{$variable-prefix}body-font-family: #{$font-family-base};
  --#{$variable-prefix}body-font-size: #{$font-size-base};
  --#{$variable-prefix}body-font-weight: #{$font-weight-base};
  --#{$variable-prefix}body-line-height: #{$line-height-base};
  --#{$variable-prefix}body-color: #{$body-color};
  @if $body-text-align != null {
    --#{$variable-prefix}body-text-align: #{$body-text-align};
  }
  --#{$variable-prefix}body-bg: #{$body-bg};
  
```

이런 변수는 실제로 다음과 같이 Reboot에 적용된다.

```scss
body {
  margin: 0; // 1
  font-family: var(--#{$variable-prefix}body-font-family);
  @include font-size(var(--#{$variable-prefix}body-font-size));
  font-weight: var(--#{$variable-prefix}body-font-weight);
  line-height: var(--#{$variable-prefix}body-line-height);
  color: var(--#{$variable-prefix}body-color);
  text-align: var(--#{$variable-prefix}body-text-align);
  background-color: var(--#{$variable-prefix}body-bg); // 2
  -webkit-text-size-adjust: 100%; // 3
  -webkit-tap-highlight-color: rgba($black, 0); // 4
}
```

원하는 대로 실시간 사용자 정의할 수 있다.

```html
<body style="--bs-body-color: #333;">
  <!-- ... -->
</body>
```

<br>

## 제목과 단락

모든 제목 요소 (예: `<h1>` 및 `<p>`)는 `margin-top`이 제거되도록 재설정된다. 제목에는 `margin-bottom: .5rem`이추가되고, 단락은 `margin-bottom : 1rem`이 추가되어 간격을 쉽게 조정할 수 있다.

| Heading     | Example               |
| ----------- | --------------------- |
| `<h1></h1>` | h1. Bootstrap heading |
| `<h2></h2>` | h2. Bootstrap heading |
| `<h3></h3>` | h3. Bootstrap heading |
| `<h4></h4>` | h4. Bootstrap heading |
| `<h5></h5>` | h5. Bootstrap heading |
| `<h6></h6>` | h6. Bootstrap heading |

<br>

## 목록

모든 목록 (`<ul>`,`<ol>`, `<dl>`)에는 `margin-top`이 제거되고 `margin-bottom: 1rem`이 제거된다. 중첩된 목록에는 `margin-bottom`이 없으며, `<ul>` 및 `<ol>` 요소에서 `padding-left`를 재설정한다.

- All lists have their top margin removed
- And their bottom margin normalized
- Nested lists have no bottom margin
  - This way they have a more even appearance
  - Particularly when followed by more list items
- The left padding has also been reset

1. Here’s an ordered list
2. With a few list items
3. It has the same overall look
4. As the previous unordered list

<br>

## 인라인 코드

인라인 코드 스니펫을 `<code>`로 묶는다. HTML 꺾쇠 괄호를 이스케이프해야 한다.

For example, `<section>` should be wrapped as inline.

```html
For example, <code>&lt;section&gt;</code> should be wrapped as inline.
```

<br>

## 코드 블록

여러 줄의 코드에는 `<pre>`를 사용한다. 코드에서 꺾쇠 괄호를 이스케이프해야 하며, `<pre>` 요소는 `margin-top`을 제거하고 `margin-bottom`에 `rem` 단위를 사용하도록 재설정된다.

```
<p>Sample text here...</p>
<p>And another line of sample text here...</p>
```

```html
<pre><code>&lt;p&gt;Sample text here...&lt;/p&gt;
&lt;p&gt;And another line of sample text here...&lt;/p&gt;
</code></pre>
```

<br>

## 변수

변수를 나타내려면 `<var>` 태그를 사용한다.

y = mx + b

복사

```html
<var>y</var> = <var>m</var><var>x</var> + <var>b</var>
```

<br>

## 사용자 입력

일반적으로 키보드를 통해 입력되는 입력을 나타내려면 `<kbd>`를 사용한다.

```html
To switch directories, type <kbd>cd</kbd> followed by the name of the directory.<br>
To edit settings, press <kbd><kbd>ctrl</kbd> + <kbd>,</kbd></kbd>
```

<br>

## 출력 예시

프로그램의 출력 예시를 나타내려면 `<samp>` 태그를 사용한다.

```html
<samp>This text is meant to be treated as sample output from a computer program.</samp>
```

<br>

## 표

표는 스타일 `<caption>`, 테두리 축소 및 전체적으로 일관된 `text-align`을 위해 약간 조정된다. 테두리, 패딩 등에 대한 추가 변경 사항은 [`.table` 클래스](https://getbootstrap.kr/docs/5.1/content/tables/) 참고.

| Table heading | Table heading | Table heading | Table heading |
| ------------- | ------------- | ------------- | ------------- |
| Table cell    | Table cell    | Table cell    | Table cell    |
| Table cell    | Table cell    | Table cell    | Table cell    |
| Table cell    | Table cell    | Table cell    | Table cell    |

<br>

### 버튼 포인터

Reboot에는 기본 커서를 `pointer`로 변경하는 `role="button"`의 개선 사항이 포함되어 있습니다. 이 속성을 요소에 추가하면 요소가 상호 작용함을 나타내는 데에 도움이 됩니다. 이 역할은 자체 `cursor` 변경 사항을 갖는 `<button>` 요소에는 필요하지 않습니다.

Non-button element button

복사

```html
<span role="button" tabindex="0">Non-button element button</span>
```

<br>

## 기타 요소

### 주소

`<address>` 요소가 업데이트되어 브라우저 기본 `font-style`이 `italic`에서 `normal`로 재설정된다. 

이제` line-height` 가 상속되고 `margin-bottom: 1rem`이 추가됐다. 

**Twitter, Inc.**
1355 Market St, Suite 900
San Francisco, CA 94103
P: (123) 456-7890**Full Name**
[first.last@example.com](mailto:first.last@example.com)

<br>

### 인용구

인용구의 기본 `margin`은 `1em 40px`이므로 다른 요소와 더 일관된 무언가를 위해 `0 0 1rem`으로 재설정한다.

> A well-known quote, contained in a blockquote element.

Someone famous in Source Title

<br>

### 인라인 요소

`<abbr>` 요소는 단락 텍스트 사이에서 눈에 띄도록 기본 스타일링을 받는다.

The HTML abbreviation element.

<br>

### 요약

요약의 기본 `cursor`는 `text`이므로 요소를 클릭하여 상호 작용할 수 있음을 전달하기 위해 이를 `pointer`로 재설정한다.

<details style="box-sizing: border-box;"><summary style="box-sizing: border-box; display: list-item; cursor: pointer;">Some details</summary><p style="box-sizing: border-box; margin-top: 0px; margin-bottom: 1rem;"></p></details>

<details open="" style="box-sizing: border-box; margin-bottom: 0px;"><summary style="box-sizing: border-box; display: list-item; cursor: pointer;">Even more details</summary><p style="box-sizing: border-box; margin-top: 0px; margin-bottom: 1rem;">Here are even more details about the details.</p></details>

<br>

## HTML5 `[hidden]` 속성

HTML5에는 [a new global attribute named `[hidden\]`이라고 불리는 새로운 전역 속성](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/hidden)이 추가되었으며, 기본적으로 `display: none`으로 스타일링된다.

```html
<input type="text" hidden>
```

##### jQuery와 호환되지 않음

`[hidden]`은 jQuery의 `$(...).hide()` 및 `$(...).show()` 메소드와 호환되지 않는다.