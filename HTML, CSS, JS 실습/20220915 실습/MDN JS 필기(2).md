## JavaScript

#### 문법

#### 변수 선언

JavaScript는 **대소문자를 구별**하며 **유니코드** 문자셋을 이용한다. 예를 들면, Früh(독일어로 "이른")을 변수명으로 사용할 수도 있다.

``` javascript
var 갑을 = "병정";
var Früh = "foobar";
```

JavaScript는 대소문자를 구분하기때문에 Früh과 früh는 다르며, 명령문이 한 줄을 다 차지할때는 세미콜론이 필요하지 않다. (두 줄 이상일경우 반드시 세미콜론으로 구분)

<br>

#### 주석

``` javascript
// 한 줄 주석

/* 이건 더 긴,
 * 여러 줄 주석입니다.
 */

/* 그러나, /* 중첩된 주석은 쓸 수 없습니다 */ SyntaxError */
```

<br>

#### 선언

JavaScript의 선언에는 3가지 방법이 있다.

- [`var`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/var)

  변수를 선언. 추가로 동시에 값을 초기화.

- [`let`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let)

  블록 스코프 지역 변수를 선언. 추가로 동시에 값을 초기화.

- [`const`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const)

  블록 스코프 읽기 전용 상수를 선언.

<br>

#### 변수 할당

지정된 초기 값 없이 `var` 혹은 `let` 문을 사용해서 선언된 변수는 [`undefined`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/undefined) 값을 갖는다.

선언되지 않은 변수에 접근을 시도하는 경우 [`ReferenceError`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError) 예외가 발생한다.

```javascript
var a;
console.log('a 값은 ' + a); // a 값은 undefined

console.log('b 값은 ' + b); // b 값은 undefined
var b;
// 이것은 아래의 '변수 호이스팅'을 읽기 전에는 혼란스러울 수 있음

console.log('c 값은 ' + c); // Uncaught ReferenceError: c is not defined

let x;
console.log('x 값은 ' + x); // x 값은 undefined

console.log('y 값은 ' + y); // Uncaught ReferenceError: y is not defined
let y;
```

<br>

`undefined`를 사용하여 변수 값이 있는지 확인할 수 있다. 아래 코드에서, `input` 변수는 값이 할당되지 않았고 [`if`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/if...else)문은 `true`로 평가한다.

```javascript
var input;
if(input === undefined) {
  doThis();
} else {
  doThat();
}
```

<br>

`undefined` 값은 boolean에서 사용될 때 `false`로 동작한다. 예를 들어, 아래 코드는 `myArray` 요소가 `undefined`이므로 `myFunction` 함수를 실행한다.

```javascript
var myArray = [];
if (!myArray[0]) myFunction();
```

<br>

`undefined` 값은 numeric에서 사용될 때 `NaN`으로 변환된다.

```javascript
var a;
a + 2; // NaN으로 평가
```

<br>

[`null`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/null) 값을 평가할 때, numeric에서는 `0`으로, boolean에서는 `false`로 동작한다. 예를 들면,

```javascript
var n = null;
console.log(n * 32); // 콘솔에 0 으로 로그가 남음
```

<br>

#### 변수 스코프(범위)

아래의 코드는 `5`라는 로그가 남는데. `x`의 스코프가 전역(global)이기 때문이다. `x`의 스코프는 `if`문 블록에 제한되지 않는다.

```javascript
if (true) {
  var x = 5;
}
console.log(x); // 5
```

<br>

이 동작은 `let` 선언을 사용하면 바뀐다 (ECMAScript 2015에 도입됨).

```javascript
if (true) {
  let y = 5;
}
console.log(y); // ReferenceError: y is not defined
```

<br>

#### 변수 호이스팅

JavaScript 변수의 특이한 점은 예외를 받지 않고도, 나중에 선언된 변수를 참조할 수 있다는 점이다.

이 개념은 **호이스팅**(hoisting)으로 알려져 있으며, JavaScript 변수가 어떤 의미에서 함수나 문의 최상단으로 "올려지는" 것을 말한다. 하지만, 끌어올려진 변수는 `undefined` 값을 반환한다. 그래서 이 변수를 사용 혹은 참조한 후에 선언 및 초기화하더라도, 여전히 `undefined`를 반환한다.

```javascript
/**
 * Example 1
 */
var x;
console.log(x === undefined); // true
x = 3;

/**
 * Example 2
 */
var myvar = 'my value';

(function() {
  var myvar;
  console.log(myvar); // undefined
  myvar = 'local value';
})();
```

호이스팅 때문에, 함수 내의 모든 `var` 문은 가능한 함수 상단 근처에 두는 것이 좋다.

CMAScript 2015의 `let`과 `const`는 변수를 블록의 상단으로 **끌어올리지만 초기화하지 않는다.** 변수가 선언되기 전에 블록 안에서 변수를 참조하게 되면 [`ReferenceError`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)를 발생시키게 되는데, 변수는 블록 시작부터 선언이 처리될 때까지 "temporal dead zone"에 위치하게 되기 때문이다.

```javascript
console.log(x); // ReferenceError
let x = 3;
```

<br>

#### 함수 호이스팅

함수에서는 [함수 선언](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/function)으로는 호이스팅되지만 [함수 표현식](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/function)으로는 호이스팅 되지 않는다.

```javascript
/* 함수 선언 */

foo(); // "bar"

function foo() {
  console.log('bar');
}

/* 함수 표현식 */

baz(); // TypeError: baz is not a function

var baz = function() {
  console.log('bar2');
};
```

<br>

#### 상수

[`const`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const) 키워드로 **읽기 전용** 상수를 만들 수 있다.

상수 식별자의 구문은 변수 식별자와 같다. 문자, 밑줄이나 달러 기호 (`$`) 로 시작해야 하고 문자, 숫자나 밑줄을 포함할 수 있다.

```javascript
const PI = 3.14;
```

상수는 스크립트가 실행 중인 동안 대입을 통해 값을 바꾸거나 재선언될 수 없으며 값으로 초기화해야 한다.

<br>

### [데이터 형](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#데이터_형)

최신 ECMAScript 표준은 8가지 데이터 형을 정의한다.

- 7가지 원시 데이터 형
  1. [Boolean](https://developer.mozilla.org/ko/docs/Glossary/Boolean). `true`와 `false`
  2. [null](https://developer.mozilla.org/ko/docs/Glossary/Null). null 값을 나타내는 특별한 키워드. 
  3. [undefined](https://developer.mozilla.org/ko/docs/Glossary/undefined). 값이 정의되어 있지 않은 최상위 속성.
  4. [Number (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/Number). 정수 또는 실수형 숫자. 예: `42` 혹은 `3.14159`.
  5. [BigInt (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/BigInt). 임의 정밀도의 정수. 예: `9007199254740992n`.
  6. [String](https://developer.mozilla.org/ko/docs/Glossary/String). 문자열. 예:"안녕"
  7. [Symbol](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Symbol). (ECMAScript 2015에 도입) 인스턴스가 고유하고 불변인 데이터 형.
- 그리고 [Object](https://developer.mozilla.org/ko/docs/Glossary/Object)

<br>

#### 형변환

JavaScript는 변수를 선언할 때 데이터 형을 지정할 필요가 없다. 또한 데이터 형이 스크립트 실행 도중 필요에 의해 자동으로 변환된다.

다음과 같이 변수를 정의할 수 있다.

```javascript
var answer = 42;
```

<br>

동일한 변수에 문자열 값을 할당할 수도 있다. 

```javascript
answer = 'Thanks for all the fish...';
```

<br>

#### 문자열 + 숫자

숫자와 문자열 값 사이에 `+` 연산자를 포함한 식에서, JavaScript는 숫자 값을 문자열로 변환한다. 

```javascript
x = 'The answer is ' + 42 // "The answer is 42"
y = 42 + ' is the answer' // "42 is the answer"
```

<br>

`+` 외의 다른 연산자를 포함한 식의 경우, JavaScript는 숫자 값을 문자열로 변환하지 않는다.

```javascript
'37' - 7 // 30
'37' + 7 // "377"
```

<br>

#### 문자열을 숫자로 변환

숫자를 나타내는 값이 문자열로 메모리에 있는 경우, 변환을 위한 메서드가 있다.

- [`parseInt()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
- [`parseFloat()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/parseFloat)

`parseInt`는 오직 정수만 반환하므로, 소수에서는 사용성이 떨어진다.

문자열을 숫자로 변환하는 대안은 `+` (단항 더하기) 연산자다.

```javascript
'1.1' + '1.1' // '1.11.1'
(+'1.1') + (+'1.1') // 2.2
// 참고: 괄호는 명확성을 위해 추가. 필수 x
```

<br>

#### 배열

length가 3인 coffees 배열

```javascript
let coffees = ['French Roast', 'Colombian', 'Kona'];
```

<br>

#### 배열의 추가 쉼표

배열 리터럴에서 모든 요소를 지정할 필요는 없다. 만약 잇달아 두 개의 쉼표를 두면, 배열은 지정되지 않은 요소를 `undefined`로 채운다.

```javascript
let fish = ['Lion', , 'Angel'];
```

이 배열은 값이 있는 두 요소와 빈 요소 하나를 가진다.

- `fish[0]`은 "Lion"
- `fish[1]`은 `undefined`
- `fish[2]`는 "Angel"

<br>

아래 예제에서, 배열의 `length`는 4이며, `myList[1]`과 `myList[3]`은 값이 빠졌다. **마지막 쉼표는 무시된다.**

```javascript
var myList = ['home', , 'school', , ];
```

<br>

#### 객체 리터럴

객체 리터럴은 중괄호(`{}`)로 묶인 0개 이상인 객체의 속성명과 관련 값 쌍 목록이다.

> **주의:** 문(statement)의 시작에 객체 리터럴을 사용해서는 안된다. 이는 `{`가 블록의 시작으로 해석되기 때문에 오류를 유발하거나 의도한 대로 동작하지 않는다.

아래의 `car` 객체의 첫째 요소는 `myCar` 속성을 정의하고 문자열 `"Saturn"`을 할당한다. 반면 둘째 요소인 `getCar` 속성은 함수 `(carTypes("Honda"))`을 호출한 결과가 즉시 할당된다. 셋째 요소 `special` 속성은 기존 변수 (`sales`)를 사용한다.

```javascript
var sales = 'Toyota';

function carTypes(name) {
  if (name === 'Honda') {
    return name;
  } else {
    return "Sorry, we don't sell " + name + ".";
  }
}

var car = { myCar: 'Saturn', getCar: carTypes('Honda'), special: sales };

console.log(car.myCar);   // Saturn
console.log(car.getCar);  // Honda
console.log(car.special); // Toyota
```

<br>

속성명으로 숫자나 문자열 리터럴을 사용하거나 또다른 객체 리터럴 내부에 객체를 중첩할 수도 있다.

```javascript
var car = { manyCars: {a: 'Saab', b: 'Jeep'}, 7: 'Mazda' };

console.log(car.manyCars.b); // Jeep
console.log(car[7]); // Mazda
```

<br>

객체 속성명은 빈 문자열 포함 어떤 문자열도 될 수 있다. 속성명이 유효한 JavaScript [식별자](https://developer.mozilla.org/ko/docs/Glossary/Identifier)나 숫자가 아닌 경우, 따옴표로 묶여야 한다.

또한 유효한 식별자가 아닌 속성명은 점(`.`) 속성으로 접근할 수 없다. 대신 배열 같은 표기법("`[]`")으로 접근하고 값을 설정할 수 있다.

```javascript
var unusualPropertyNames = {
  '': 'An empty string',
  '!': 'Bang!'
}
console.log(unusualPropertyNames.'');   // SyntaxError: Unexpected string
console.log(unusualPropertyNames['']);  // An empty string
console.log(unusualPropertyNames.!);    // SyntaxError: Unexpected token !
console.log(unusualPropertyNames['!']); // Bang!
```

<br>

#### 향상된 객체 리터럴

ES2015에서, 객체 리터럴은 구성에서 프로토타입 설정, `foo: foo` 할당을 위한 단축 표기, 메서드 정의, `super` 클래스 호출 및 식으로 동적인 속성명 계산을 지원하기 위해 확장됐다.

그에 따라 객체 리터럴 및 클래스 선언이 함께 더 가까워지고, 객체 기반 설계는 같은 일부 편의기능으로 득을 볼 수 있다.

```javascript
var obj = {
    // __proto__
    __proto__: theProtoObj,
    // ‘handler: handler’의 단축 표기
    handler,
    // Methods
    toString() {
     // Super calls
     return 'd ' + super.toString();
    },
    // Computed (dynamic) property names
    [ 'prop_' + (() => 42)() ]: 42
};
```

<br>

#### 정규식 리터럴

정규식 리터럴은 ([정규식 상세](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Regular_Expressions)) 슬래시 사이에 감싸인 패턴이다. 

```javascript
var re = /ab+c/;
```

<br>

#### 문자열 리터럴

문자열 리터럴은 큰 따옴표(`"`) 혹은 작은 따옴표(`'`)로 묶인 0개 이상의 문자다. 문자열은 같은 형 따옴표 (즉 큰 따옴표 쌍이나 작은 따옴표 쌍) 로 구분되어야 한다.

```javascript
'foo'
"bar"
'1234'
'one line \n another line'
"John's cat"
```

꼭 `String` 객체를 사용할 필요가 없는 경우 문자열 리터럴을 사용해야 한다. 

문자열 리터럴 값은 [`String`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String) 객체의 모든 메서드를 호출할 수 있다. JavaScript는 자동으로 문자열 리터럴을 임시 문자열 객체로 변환, 메서드를 호출하고 나서 임시 문자열 객체를 폐기한다. 또한 문자열 리터럴에서도 `String.length` 속성을 사용할 수 있다.

```javascript
// 공백을 포함한 문자열 내 심볼 갯수가 출력됩니다.
console.log("John's cat".length)// 여기서는, 10.
```

<br>

[템플릿 리터럴](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Template_literals)도 사용할 수 있다. 템플릿 리터럴은 큰 따옴표나 작은 따옴표 대신 백틱 (```) 으로 문자를 감싼다.

```javascript
// 기본적인 문자열 리터럴 생성
`In JavaScript '\n' is a line-feed.`

// 여러 줄 문자열
`In JavaScript, template strings can run
 over multiple lines, but double and single
 quoted strings cannot.`

// 문자열 삽입
var name = 'Bob', time = 'today';
`Hello ${name}, how are you ${time}?`
```

<br>

[Tagged templates](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Template_literals#tagged_templates)은 구문 분석을 위한 "태그" 함수에 대한 호출과 함께 템플릿 리터럴을 지정하기 위한 간결한 구문이다. 템플릿 태그 함수의 이름은 아래 예제에서 `myTag` 가 템플릿 태그 함수 이름인 것과 같이 템플릿 리터럴 앞에 온다.

```javascript
let myTag = (str, name, age) => `${str[0]}${name}${str[1]}${age}${str[2]}`;
let [name, age] = ['Mika', 28];
myTag`Participant "${ name }" is ${ age } years old.`;
// Participant "Mika" is 28 years old.
```

<br>

#### 문자열에서 특수 문자 사용

보통 문자에 더해서, 문자열에 아래 예제와 같이 특수 문자도 포함할 수 있다.

```javascript
'one line \n another line'
```

<br>

다음 표는 JavaScript 문자열에 사용할 수 있는 특수 문자 목록이다.

| 문자          | 뜻                                                           |
| :------------ | :----------------------------------------------------------- |
| `\0`          | Null Byte                                                    |
| `\b`          | Backspace                                                    |
| `\f`          | Form feed                                                    |
| `\n`          | New line                                                     |
| `\r`          | Carriage return                                              |
| `\t`          | Tab                                                          |
| `\v`          | Vertical tab                                                 |
| `\'`          | Apostrophe 혹은 작은 따옴표                                  |
| `\"`          | 큰 따옴표                                                    |
| `\\`          | 백슬래시                                                     |
| `\*XXX*`      | Latin-1 인코딩 문자는 `0` - `377` 사이 8진수 3자리 *XXX*까지 지정될 수 있습니다. 예를 들어, `\251`은 copyright 심볼을 표현하는 8진수 시퀀스입니다. |
| `\x*XX*`      | Latin-1 인코딩 문자는 `00` - `FF` 사이의 16진수 2자리 *XX*로 지정될 수 있습니다. 예를 들어, `\xA9`는 copyright 심볼을 표현하는 16진수 시퀀스입니다. |
| `\u*XXXX*`    | 유니코드 문자는 16진수 4자리 *XXXX*로 지정될 수 있습니다. 예를 들어, `\u00A9`는 copyright 심볼을 표현하는 유니코드 시퀀스입니다. [Unicode escape sequences](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Lexical_grammar#string_literals)를 참고하세요. |
| `\u*{XXXXX}*` | 유니코드 코드 포인트 이스케이프. 예를 들어, `\u{2F804}`는 간단한 유니코드 이스케이프 `\uD87E\uDC04`와 같습니다. |

<br>

#### 문자 이스케이프

JavaScript에는 "heredoc" 구문은 없지만, 줄바꿈 이스케이프와 각 줄 끝 이스케이프된 줄바꿈을 추가하여 흉내낼 수 있다.

```javascript
var poem =
'Roses are red,\n\
Violets are blue.\n\
Sugar is sweet,\n\
and so is foo.'
```

<br>

ECMAScript 2015에서는 [**템플릿 리터럴**](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Template_literals)이라는 새로운 리터럴이 소개되었고, 다중 문자열을 포함한 많은 새로운 기능을 가지고 있다.

```javascript
var poem =
`Roses are red,
Violets are blue.
Sugar is sweet,
and so is foo.`
```

