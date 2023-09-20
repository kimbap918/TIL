## ECMA Script

## 코딩 스타일 가이드

* 코딩 스타일의 핵심은 합의된 원칙과 일관성
  * 절대적인 하나의 정답은 없으며, 상황에 맞게 원칙을 정하고 일관성 있게 사용하는 것이 중요하다.
* 코딩 스타일은 코드의 품질에 직결되는 중요한 요소
  * 코드의 가독성, 유지보수 또는 팀원과의 커뮤니케이션 등 개발 과정 전체에 영향을 끼친다.

<br>

## 변수와 식별자

* 식별자는 변수를 구분할 수 있는 변수명을 말한다.
* 식별자는 반드시 문자, 달려($) 또는 밑줄(_)로 시작
* 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작된다
* 예약어 사용 불가능 (for, if, function 등)

<br>

#### 선언, 할당, 초기화

* 선언(Declaration)
  * 변수를 생성하는 행위 또는 시점
* 할당(Assignment)
  * 선언된 변수에 값을 저장하는 행위 또는 시점
* 초기화(Initialization)
  * 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

``` javascript
let foo
console.log(foo)

foo = 11
console.log(foo)

let bar = 0
console.log(bar)
```

<br>

#### let, const

``` javascript
let number = 10 // 1. 선언 및 초기값 할당
number = 10 // 2. 재할당

console.log(number) // 3. 10

let number = 10 // 1. 선언 및 초기값 할당
let number = 50 // 2. 재선언 불가능
```

let(재할당 가능, 재선언 불가능, 블록 스코프)

<br>

``` javascript
const number = 10 // 1. 선언 및 초기값 할당
number = 10 // 2. 재할당 불가능

const number = 10 // 1. 선언 및 초기값 할당
const number = 50 // 2. 재선언 불가능
```

const(재할당 불가능, 재선언 불가능, 블록 스코프)

<br>

* 블록 스코프(block scope)

  * if, for,  함수등의 중괄호 내부를 가리킴

  * 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

    ``` javascript
    let x = 1
    
    if (x === 1) {
      let x = 2
      console.log(x) // 2
    }
    
    console.log(x) // 1
    ```

<br>

#### var

* var로 선언한 변수는 재선언 및 재할당 모두 가능
* ES6 이전에 변수를 선언할 때 사용되던 키워드
* 호이스팅 되는 특성으로 인해 예기치 못한 문제 발생 가능
  * 호이스팅(hoisting)
    * 변수를 선언 이전에 참조할 수 있는 현상
    * 변수 선언 이전의 위치에서 접근 시 undefined를 반환
    * 자바스크립트는 모든 선언을 호이스팅한다.
    * var, let, const 모두 호이스팅이 발생하지만, var는 선언과 초기화가 동시에 발생하여 일시적으로 사각지대가 존재하지 않는다.
* 함수 스코프
  * 함수의 중괄호 내부를 가리킴
  * 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

``` javascript
function foo() {
  var x = 5
  console.log(x)
}
// ReferenceError: x is not defined
console.log(x)
```

<br>

## 데이터 타입

* 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐
* 크게 원시 타입(Primitive type)과 참조 타입(Reference type)으로 분류됨

* Primitive type

  * 객체가 아닌 기본 타입
  * 변수에 해당 타입의 값이 담긴다
  * 다른 변수에 복사할 때 실제 값이 복사됨

* Reference type

  * 객체 타입의 자료형
  * 변수에 해당 객체의 참조 값이 담김
  * 다른 변수에 복사할 때 참조 값이 복사됨

* 숫자 타입

  * 정수, 실수 구분 없는 하나의 숫자 타입
  * 부동소수점 형식을 타름
  * Nan(Not-A-Number)
    * 계산 불가능한 경우 반환되는 값

* 문자열(String) 타입

  * 텍스트 데이터를 나타내는 타입

  * 16비트 유니코드 문자의 집합

  * 작은따옴표 또는 큰따옴표 모두 가능

  * 템플릿 리터럴(Templete Literal)

    * ES6부터 지원

    * 따옴표 대신 backtrack(`)으로 표현

    * ${ expression } 형태로 표현식 삽입 가능

      ``` javascript
      const firstName = 'Brandan'
      const lastName = 'Eich'
      const fullName = `${firstName} ${lastName}`
      
      console.log(fullName) // Brandan Eich
      ```

* undefined

  * 변수의 값이 없음을 나타내는 데이터 타입

  * 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined가 할당됨

    ``` javascript
    let firstName
    console.log(firstName) // undefined
    ```

* null

  * 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입

  * typeof : 자료형 평가를 위해 사용하는 연산자 

  * null의 typeof 연산자의 결과는 ECMA 명세의 원시 타입 정의에 따르면 원시 타입에 속하지만 객체(object)로 표현됨

    ``` javascript
    let firstName = null
    console.log(firstName) // null
    
    typeof null // object
    ```

* Boolean 타입

  * 논리적 참 또는 거짓을 나타내는 타입

  * true 또는 false로 표현

  * 조건문 또는 반복문에서 유용하게 사용

    ``` javascript
    let isAdmin = true
    console.log(isAdmin) // true
    
    isAdmin = false
    console.log(isAdmin) // false
    ```

<br>

## 연산자

* 할당 연산자

  * 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자

  * 다양한 연산에 대한 단축 연산자 지원

  * ++ 및 -- 연산자

    * ++ : 피연산자의 값을 1 증가시키는 연산자

    * -- : 피연산자의 값을 1 감소시키는 연산자 

      ``` javascript
      let x = 0
      
      x += 10
      x -= 3
      x *= 10
      x /= 10
      x++
      x-- 
      ```

* 비교 연산자

  * 피연산자를 비교하고 결과값을 boolean으로 반환하는 연산자

  * 문자열은 유니코드의 값을 사용하며 표준 사전 순서를 기반으로 비교

    ``` javascript
    const numOne = 1
    const numTwo = 100
    console.log(numOne < numTwo) // True
    
    const charOne = 'a'
    const charTwo = 'z'
    console.log(charOne > charTwo) // false
    ```

* 동등 비교 연산자(==)

  * 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환

  * 비교할때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교

  * 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별

  * 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않는다

    ``` javascript
    const a = 1004
    const b = '1004'
    console.log(a == b) // true
    
    const c = 1
    const d = true
    console.log(c == d) // true
    ```

* 일치 비교 연산자(===)

  * 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환

  * 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음

    * 엄격한 비교 : 두 비교 대상의 타입과 값 모두 같은지 비교

      ``` javascript
      const a = 1004
      const b = '1004'
      console.log(a === b) // false
      ```

* 논리 연산자

  * 세 가지 논리 연산자로 구성

  * and 연산은 && 연산자 이용

  * or 연산은 || 연산자 이용

  * not 연산은 ! 연산자를 이용

    ``` javascript
    console.log(true && false) // false
    console.log(1 && 0) // 0
    console.log(true || false) // ture
    console.log(1 || 0) // 1
    console.log(!true) // false
    ```

* 삼항 연산자

  * 세 개의 피연산자를 사용해 조건에 따라 값을 반환하는 연산자

  * 가장 왼쪽의 조건식이 참이면 : 앞의 값을 사용하고 그렇지 않으면 뒤의 값 사용

    ``` javascript
    console.log(true ? 1 : 2) // 1
    ```

    

<br>

## 조건문

조건문의 종류와 특징

* if, else if, else

  * 조건은 소괄호() 안에 작성 

  * 실행할 코드는 중괄호{} 안에 작성

  * 블록 스코프 생성 

    ``` javascript
    const nation = 'korea'
    
    if (nation === 'korea') {
      console.log('안녕하세요') 
    } else if (nation === 'France') {
      console.log('Bonjour')
    } else {
      console.log('Hello!')
    }
    ```

* switch

  * 표현식의 결과값과 case문의 오른쪽 값을 비교

  * break 및 default문은 [선택적]으로 사용 가능

  * break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행

    ``` javascript
    const nation = 'korea'
    
    switch(nation) {
      case 'korea': {
        console.log('안녕하세요!')
      }
      case 'France': {
        console.log('Bonjour!')
      }
      default: {
        console.log('Hello!')
      }
    }
    // 이 경우에는 break문이 없으므로 모두 출력
    ```

<br>

## 반복문

반복문의 종류와 특징

* while

  * 조건문이 참(true)일 경우에만 반복 시행

  * 조건은 소괄호 안에 작성

  * 실행할 코드는 중괄호 안에 작성

  * 블록 스코프 생성

    ``` javascript
    while (condition) {
      // do something
    }
    ```

* for

  * 세미콜론(;)으로 구분되는 세 부분으로 구성

  * initialization : 최초 반복문 진입 시 1회만 실행

  * condition : 매 반복 시행 전 평가되는 부분 

  * expression : 매 반복 시행 이후 평가되는 부분

  * 블록 스코프 생성

    ``` javascript
    for (initialization; condition; expression) {
      // do something
    }
    
    for (let i = 0; i < 6; i++) {
      console.log(i) // 0, 1, 2, 3, 4, 5
    }
    ```

* for ... in

  * 객체(object)의 속성(key)들을 순회할 때 사용

  * 배열도 순회 가능하지만 권장되지 않음

  * 실행할 코드는 중괄호 안에 작성

  * 블록 스코프 생성

    ``` javascript
    for (variable in object) {
      // do something
    }
    
    const capitals = {
      korea: 'seoul',
      france: 'paris',
      USA: 'washington D.C.'
    }
    
    for (let capital in capitals) {
      console.log(capital) // korea, france, USA
    }
    ```

* for ...of

  * 반복가능한 객체를 순회하며 값을 꺼낼때 사용

  * 실행할 코드는 중괄호 안에 작성

  * 블록 스코프 생성

    ``` javascript
    for (variable of iterables) {
      /// do something
    }
    
    const fruits = ['딸기', '바나나', '메론']
    
    for (let fruit of fruits) {
      fruit = fruit + '!'
      console.log(fruit)
    }
    ```

<br>

## 함수

* 참조 타입 중 하나로, function 타입에 속함
* JS에서 함수를 정의하는 방법은 주로 2가지
  * 함수 선언식
  * 함수 표현식
* JS의 함수는 일급 객체에 해당
  * 일급 객체 : 다음의 조건들을 만족하는 객체를 의미함
    * 변수에 할당 가능
    * 함수의 매개변수로 전달 가능
    * 함수의 반환 값으로 사용 가능

<br>

#### 함수의 정의

* 함수의 이름과 함께 정의하는 방식

* 3가지 부분으로 구성

  * 함수의 이름 (name)

  * 매개변수 (args)

  * 함수 body (중괄호 내부)

    ``` javascript
    function add(num1, num2) {
      return num1 + num2
    }
    
    add(1, 2)
    ```

* 함수 표현식

  * 함수를 표현식 내에서 정의하는 방식

    * 표현식 : 어떤 하나의 값으로 결정되는 코드의 단위

  * 함수의 이름을 생략하고 익명 함수로 정의 가능

    * 익명 함수 : 이름이 없는 함수
    * 익명 함수는 함수 표현식에서만 가능

  * 3가지 부분으로 구성

    * 함수의 이름 (생략 가능)

    * 매개변수 (args)

    * body (중괄호 내부)

      ``` javascript
      const add = function (num1, num2) {
        return num1 + num2
      }
      
      add(num1, num2)
      ```

* 기본 인자 : 인자 작성 시 '=' 문자 뒤 기본 인자 선언 가능  

  ``` javascript
  const add = function (num1 = 1, num2 = 2) {
    return num1 + num2
  }
  ```

* **매개변수와 인자의 개수 불일치 허용**

  * 매개변수보다 인자의 개수가 많을 경우

    ``` javascript
    const noArgs = funstion () {
      return 0
    }
    
    noArgs(1, 2, 3) // 0
    
    const twoArgs = function (arg1, arg2) {
      return [arg1, arg2]
    }
    
    twoArgs(1, 2, 3) // [1, 2]
    ```

  * 매개변수보다 인자의 개수가 적을 경우

    ``` javascript
    const twoArgs = function (arg1, arg2) {
      return [arg1, arg2]
    }
    
    twoArgs() // [undefined, undefined]
    ```

* Rest Parameter

  * rest parameter(...)을 사용하면 함수가  정해지지 않은 수의 매개변수를 열로 받음

    ``` javascript
    const restOpr = function(arg1, arg2, ...restArgs) {
      return [arg1, arg2, restargs]
    }
    
    restargs(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
    ```

* Spread operator

  * spread operator(...)를 사용하면 배열 인자를 전개하여 전개 가능

    ``` javascript
    const spreadOpr = function(arg1, arg2, arg3) {
      return arg1 + arg2 + arg3
    }
    
    const numbers = [1, 2, 3]
    spreadOpr(...numbers) // 6
    ```

<br>

#### 선언식 vs 표현식

함수의 타입

* 선언식의 함수와 표현식의 함수 모두 타입은 function으로 동일

  ``` javascript
  // 함수 표현식
  const add = function (args) {}
  
  // 함수 선언식
  function sub(args) {}
  
  console.log(typeof add) // function
  console.log(typeof sub) // function
  ```

호이스팅

* 함수 표현식

  * 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생

  * 함수 표현식으로 정의된 함수는 변수로 평가되어 scope규칙을 따름

    ``` javascript
    sub(7, 2) // 에러
    
    const sub = function (num1, num2) {
      return num1 - num2
    }
    ```

<br>

#### 화살표 함수(Arrow Function)

* 함수를 비교적 간결하게 정의할 수 있는 문법

* function 키워드 생략 가능

* 함수의 매개변수가 단 하나뿐이라면, () 도 생략 가능

* 함수의 body가 표현식 하나라면 {} 과 return도 생략 가능

  ``` javascript
  const arrow1 = function (name) {
    return `hello, ${name}`
  }
  // function 키워드 삭제
  const arrow2 = (name) => {return `hello, ${name}`}
  // 매개변수가 1개일 경우에는 () 삭제가능
  const arrow3 = name => {return `hello, ${name}`}
  // 함수의 body가 표현식 하나라면 {} 과 return도 생략 가능
  const arrow4 = name => `hello, ${name}`
  ```

<br>

## 배열

* 키와 속성들을 담고 있는 참조 타입의 객체(objcet)

* 순서를 보장하는 특징이 있다

* 주로 대괄호를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능

* 배열의 길이는 array.length 형태로 접근 가능

  ``` javascript
  const numbers = [1, 2, 3, 4, 5]
  
  console.log(numbers[numbers.length - 1]) // 5

<br>

#### 배열 관련 주요 메서드

* array.unshift() : 가장 앞에 요소 추가

* array.shift() : 배열의 첫번째 요소 제거 

* array.includes(value) : 배열의 특정 값이 존재하는지 판별 후 참 또는 거짓 반환

* array.indexOf(value) : 배열에 특정 값이 존재하는지 확인 후 가장 첫번째로 찾은 요소의 인덱스 반환 값이 없을경우 -1 반환 

* array.join([separator]) : 배열의 모든 요소를 연결하여 반환, 구분자는 선택적으로 지정 생략시 쉼표가 기본값

* array.forEach(callback(element[, index[,array]]))

  * 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  * 콜백 함수는 3가지 매개변수로 구성

    * element: 배열의 요소
    * index : 배열 요소의 인덱스
    * array : 배열 자체

  * 반환값이 없는 메서드

    ``` javascript
    array.forEach((element, index, array) => {
      // do something
    })
    
    const fruits = ['딸기', '수박', '사과', '체리']
    
    fruits.forEach((fruit, index) => {
      console.log(fruit, index)
      // 딸기 0
      // 수박 1
      // 사과 2
      // 체리 3
    })
    ```

* array.map(callback(element[, index[, array]]))

  * 배열의 각 요소에 대해 콜백 함수를 한번씩 실행

  * 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환

  * 기존 배열 전체를 다른 형태로 바꿀때 유용

    ``` javascript
    array.map((element, index, array) => {
      // do something
    })
    
    const numbers = [1, 2, 3, 4, 5]
    
    const doubleNums = numbers.map((num) => {
      return num * 2
    })
    
    console.log(doubleNums) // [2, 4, 6, 8, 10]
    ```

* array.reduce(callback(acc, element, [index[, array]])[, initialValue])

  * 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  * 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환

  * reduce 메서드의 주요 매개변수

    * acc
      * 이전 callback 함수의 반환 값이 누적되는 변수
    * initialValue(optional)
    * 최초  callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값

    ``` JavaScript
    array.reduce((acc, element, index, array) => {
      // do something
    }, initialValue)
    
    const numbers = [1, 2, 3]
    const result = numbers.reduce((acc, num) => {
      return acc + num
    }, 0)
    
    console.log(result) // 6
    ```

* array.some(callback(element[, index[, array]]))

  * 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환 

* array.every(callback(element[, index[, array]]))

  * 배열의 모든 요소가 주어진 판별 함수를 통과하면 참을 반환 

<br>

## 객체 

객체의 정의와 특징 

* 객체는 속성(propety)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현

* key는 문자열 타입만 가능

* value는 모든 타입(함수 포함) 가능

* 객체 요소 접근은 점 또는 대괄호로 가능

  ``` javascript
  const me = {
    name : 'jack',
    phoneNumber : '012345678',
    'samsung products' : {
      buds : 'Galaxy Buds pro',
      galaxy : 'Galaxy s20'
    },
  }
  
  console.log(me.name)
  ```

* 메서드는 객체의 속성이 참조하는 함수

* 객체.메서드명() 으로 호출 가능

* 메서드 내부에서는 this 키워드가 객체 를 의미

  ``` javascript
  const me = {
    firstName: 'John',
    lastName: 'Doe',
    getFullName: function () {
      return this.firstName + this.lastName
    }
  }
  ```

  