## 중단점(Breakpoints)

Breakpoints는 Bootstrap의 **반응형 레이아웃이 뷰포트 크기 또는 기기에서 어떻게 작동 할지 결정하는 사용자가 정의 가능한 넓이**다.

부트스트랩에는 반응형 제작을 위해 **grid tiers**라고 하는 6개의 중단점이 포함되어 있다. 

| Breakpoint        | Class infix | Dimensions          |
| ----------------- | ----------- | ------------------- |
| X-Small           | none        | < 576px             |
| Small             | sm          | >= 576px (스마트폰) |
| Medium            | md          | >= 768px (태블릿)   |
| Large             | lg          | >= 992px (PC)       |
| Extra large       | xl          | >= 1200px           |
| Extra extra large | xxl         | >= 1400px           |

Breakpoints는 Sass를 통해 사용자 정의 할 수 있다.

```scss
$grid-breakpoints: (
  xs: 0,
  sm: 576px,
  md: 768px,
  lg: 992px,
  xl: 1200px,
  xxl: 1400px
);
```

<br>

## 미디어 쿼리

부트스트랩은 모바일 우선으로 제작되었으므로 몇 가지 미디어 쿼리를 이용해 레이아웃에 적합한 breakpoints를 만든다. 이러한 breakpoints는 대부분 최소 뷰포트 넓이를 기반으로 하며, 뷰포트를 변경함에 따라서 요소를 확장할 수 있다.

<br>

#### Min-width

기존의 미디어 쿼리는 이렇게 하나하나 정해서 써줘야했다.

``` scss
// Small devices (landscape phones, 576px and up)
@media (min-width: 576px) { ... }
 
// Medium devices (tablets, 768px and up)
@media (min-width: 768px) { ... }
 
// Large devices (desktops, 992px and up)
@media (min-width: 992px) { ... }
 
// X-Large devices (large desktops, 1200px and up)
@media (min-width: 1200px) { ... }
 
// XX-Large devices (larger desktops, 1400px and up)
@media (min-width: 1400px) { ... }
```

<br>

부트스트랩에서는 이것들을 모듈화해서 지원해준다.

``` scss
/* No media query necessary for xs breakpoint as it's effectively `@media (min-width: 0) { ... } */`
@include media-breakpoint-up(sm) { ... }
@include media-breakpoint-up(md) { ... }
@include media-breakpoint-up(lg) { ... }
@include media-breakpoint-up(xl) { ... }
@include media-breakpoint-up(xxl) { ... }
 
 
/* Example: Hide starting at `min-width: 0`, and then show at the `sm` breakpoint */
.custom-class {
  display: none;
}
@include media-breakpoint-up(sm) {
  .custom-class {
    display: block;
  }
}
```

<br>

#### Max-width

``` scss
/* 부트스트랩 */
@include media-breakpoint-down(sm) { ... }
@include media-breakpoint-down(md) { ... }
@include media-breakpoint-down(lg) { ... }
@include media-breakpoint-down(xl) { ... }
@include media-breakpoint-down(xxl) { ... }
 
@include media-breakpoint-down(md) {
  .custom-class {
    display: block;
  }
}
 
/*----------------------------------------*/
 
/* css */
// X-Small devices (portrait phones, less than 576px)
@media (max-width: 575.98px) { ... }
 
// Small devices (landscape phones, less than 768px)
@media (max-width: 767.98px) { ... }
 
// Medium devices (tablets, less than 992px)
@media (max-width: 991.98px) { ... }
 
// Large devices (desktops, less than 1200px)
@media (max-width: 1199.98px) { ... }
 
// X-Large devices (large desktops, less than 1400px)
@media (max-width: 1399.98px) { ... }
```

<br>

#### 중단점 사이(Between)

``` scss
/* 부트스트랩 */
@include media-breakpoint-between(md, xl) { ... }
 
/*----------------------------------------*/
 
/* css */
@media (min-width: 768px) and (max-width: 1199.98px) { ... }
```

