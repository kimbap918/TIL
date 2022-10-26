## AJAX

#### Asynchronous JavaScript(비동기 자바스크립트)

``` javascript
const request = new XMLHttpRequest()
const URL = 'https://jsonplaceholder.typicode.com/todos/1/'

request.open('GET', URL)
request.send()

const todo = request.response
console.log('data: ${todo}') 


console.log('hi')

setTimeout(function () {
  console.log('작업중')
})

console.log('bye')
```

비동기의 특징

* 병렬적 작업 수행
* 요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어진다.
* 결과적으로 변수 todo에는 응답 데이터가 할당되지 않고 빈 문자열이 출력됨
* 그렇다면 JS는 왜 기다려주지 않는 방식으로 동작하는가?

<br>

#### Event Loop 기반 동시성 모델

**Call Stack**

* 요청이 들어올 때마다  해당 요청을 순차적으로 처리하는 Stack(LIFO) 형태의 자료구조

**Web API(Browser API)**

* JS 엔진이 아닌 브라우저 영역에서 제공하는 API
* 예) setTimeout(), DOM event, AJAX

**Task Queue(Event Queue, Message Queue)**

* 비동기 처리된 callback 함수가 대기하는 Queue(FIFO) 형태의 자료 구조
* main thread가 끝난 후 실행되어 후속 JavaScript 코드가 차단되는 것을 방지함

**Event Loop**

* Call Stack이 비어있는지 확인
* 비어 있는 경우 Task Queue에서 실행 대기 중인 callback 함수가 있는지 확인
* Task Queue에 대기중인 callback 함수가 있다면 가장 앞에 있는 callback 함수를 Call Stack으로 push

<br>

#### AJAX?

* Asynchoronous JavaScript And XML(최근에는 JSON을 더 많이 사용한다)
* 비동기 통신을 이용하면 화면 전체를 새로고침 하지 않아도 서버로 요청을 보내고, 데이터를 받아 화면의 일부분만 업데이트 하는것이 가능하다
* 이러한 비동기 통신 웹 개발 기술을 AJAX라고 한다.
* 비동기 웹 통신을 위한 라이브러리 중 하나가 **Axios**

<br>

## 좋아요 기능 비동기로 처리하기

#### articles > detail.html

* i 태그에 id와 data-article-id를 부여해준다.

``` html
  {% if request.user.is_authenticated %}
    {% if request.user in article.like_users.all %}
      <a class="btn btn-secondary" href="{% url 'articles:like' article.pk %}">
        <i id="like-btn"  data-article-id="{{ article.pk }}" class="bi bi-balloon-heart-fill"></i> 좋아요 취소</a>
    {% else %}
      <a class="btn btn-danger" href="{% url 'articles:like' article.pk %}">
        <i id="like-btn" data-article-id="{{ article.pk }}" class="bi bi-balloon-heart"></i> 좋아요</a>
    {% endif %}
  {% endif %}
```

<br>

#### detail.html의 script부

``` html
<script>
  // (1) 좋아요 버튼
  const likeBtn = document.querySelector('#like-btn')
  // (2) 좋아요 버튼을 클릭하면, 함수 실행
  likeBtn.addEventListener('click', function(){
    // 서버로 비동기 요청을 하고싶음
    axios({
      method: 'get',
      url: `/articles/${event.target.dateset.articleId}/like/`
    })
    .then(response => {
      console.log(response)
      console.log(response.data)
      //event.target.classList.toggle('bi-heart')
      //event.target.classList.toggle('bi-heart-fill')
      if (response.data.isLiked === true ) {
        event.target.classList.add('bi-balloon-heart')
        event.target.classList.remove('bi-balloon-heart-fill')
      }
      const likeCount = document.querySelector('#like-count')
      likeCount.innerText = response.data.likeCount
    })
  })
</script>
```

<br>

#### views.py 

``` python
from django.http import JsonResponse
@login_required
def like(request, pk):
  article = get_object_or_404(Article, pk=pk)
  # 만약에 로그인한 유저가 이 글을 좋아요를 눌렀다면,
  # like_users.all() 안에 그 안에 유저가 있으면 (apple 에 a가 포함되어있나? 정도 느낌)
  if request.user in article.like_users.all(): 
    # 좋아요 삭제
    article.like_users.remove(request.user)
    is_liked = False
  else:
    # 좋아요 추가
    article.like_users.add(request.user)
    is_liked = True
  # 상세 페이지로 redirect
  return JsonResponse({'idLiked': is_liked})
```

<br>

## 댓글 작성 비동기 처리

1. 어떤 이벤트일때 요청을 보낼지
   * form을 작성하면..
   * /article/`<pk>`/comments/
2. 서버에서 어떤 응답을 JSON으로 보내서
   * 댓글 정보를 보내서
3. DOM 조작을 어떻게 할지
   * 댓글 목록에 추가해줌

#### articles > detail.html

* 기존의 댓글 form에 id값과 data-article-id를 부여한다.

``` html
...
	<h4 class="my-3">댓글</h4>
  {% if request.user.is_authenticated %}
  <form id="comment-form" data-article-id="{{ article.pk }}" action="{% url 'articles:comment_create' article.pk %}" method="POST">
    {% csrf_token %}
    {% bootstrap_form comment_form layout='inline' %}
    {% bootstrap_button button_type="submit" content="OK" %}
    {% comment %}  {% endcomment %}
  </form>
...
```

<br>

#### detail.html 의 script부

* 기존의 댓글이 생성되는 부분에 div를 추가해서 id를 부여해준다

``` html
  <div id="comments">
    {% for comment in comments %}
      <p>{{ comment.user.username }} | {{ comment.content }}</p>
      <form action="{% url 'articles:comment_delete' article.pk comment.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      </form>
      <hr>
      {% empty %}
      <p>댓글이 없어요 ㅠ_ㅠ</p>
    {% endfor %}
  </div>
```

<br>

#### views.py

* context로 내용과 유저명을 담아서 JsonResponse로 context를 반환

``` python
from django.http import JsonResponse

@login_required
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment_form.save() # 모델 인스턴스의 save()
        context = {
            'content': comment.content,
            'userName': comment.user.username
        }
    return JsonResponse(context)
```

