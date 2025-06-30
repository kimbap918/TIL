**LangGraph의 목적**
    - LangGraph는 대화 흐름을 노드 기반으로 구성하는 LLM 기반 워크플로우 도구입니다.
    - 사용자의 입력을 분기 처리하고, 조건별로 다음 노드로 흐름을 제어할 수 있기 때문에,
    - 예: “동화를 추천해줘” → 유저 정보 기반 추천 → 동화 DB 검색 → 추천 결과 반환 가능


<br>

## Step 1: LangGraph 구조 준비 – 폴더 생성
* Django 백엔드 안에서 LangGraph 관련 코드를 구성하기 위한 폴더를 먼저 만듭니다.

```swift
back/api/services/langgraph/
├── __init__.py
├── nodes.py         ← LangGraph 노드 정의 (생성, 저장 등)
└── story_flow.py    ← LangGraph 플로우 정의

```


<br>

## Step 2: LangGraph 노드 정의
1. `nodes.py`에 다음 노드 생성:
	- generate_paragraph: 재미나이(Gemini)를 이용해 패러그래프 생성        
    - `save_paragraph`: 생성 결과를 `StoryParagraph`, `ParagraphVersion`에 저장    
    - `generate_qa` (선택): 해당 패러그래프에 대한 Q&A 생성
        
2. `story_flow.py`에서 위 노드를 연결하는 LangGraph 플로우 정의
3. 경로: `back/api/services/langgraph/story_flow.py`


### 🛠️ 준비 사항
- `.env`의 `GOOGLE_API_KEY` → Gemini API에 사용
- Django 모델은 `managed = False`이므로 직접 쿼리 또는 ORM으로 저장 가능
- Gemini API 호출은 Python용 라이브러리 [`google.generativeai`](https://pypi.org/project/google-generativeai/) 사용 가능

<br>

### 목표 노드 구성
| 노드 이름                          | 기능 설명                                    |
| ------------------------------ | ---------------------------------------- |
| 1️⃣ `generate_paragraph`       | Gemini로 패러그래프 생성                         |
| 2️⃣ `save_paragraph`           | `StoryParagraph`, `ParagraphVersion`에 저장 |
| 3️⃣ `save_qa`                  | 사용자 질문과 챗봇 답변을 `ParagraphQA`에 저장         |
| 4️⃣ `update_paragraph_version` | 사용자의 요청으로 내용을 수정, 1, 2번에 저장              |

#### 1. generate_paragraph
* 사용자의 입력에 따른 동화 생성 


```python
# LangGraph 노드 정의
# 작성자 : 최준혁
# 작성일 : 2025-06-03

import google.generativeai as genai
import os

# Gemini 초기화 및 모델 정의
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

# 기능 : 사용자 입력을 받아 동화 패러그래프를 생성하는 노드
def generate_paragraph(state: dict) -> dict:
    user_input = state.get("input")
    user_age = state.get("age")

    # Gemini에게 프롬프트 전송
    prompt = (
        "아래 사용자의 요청을 바탕으로 사용자의 연령에 따라 친근한 말투를 사용하며 동화의 문장을 만들어줘.\n"
        "- 대화 상호작용을 통해 동화의 문단을 만들고, 사용자의 요청에 따라 동화의 내용을 수정해줘.\n"
        "- 사용자의 연령에 따라 문장의 길이와 복잡도를 조절해줘.\n"
        f"- 사용자의 연령은 {user_age}세.\n"
        "- 문장은 짧고 이해하기 쉽게 써줘.\n"
        "- 총 3~5문장 정도가 적당해.\n"
        "- 너무 무겁거나 복잡한 표현은 피하고, 동심을 담아줘.\n\n"
        f"사용자 요청: {user_input}"
    )

    response = model.generate_content(prompt)
    generated_paragraph = response.text.strip()

    return {
        "input": user_input,
        "age": user_age,
        "paragraph_text": generated_paragraph
    }
```

<br>

#### 2. save_paragraph
*  생성된 패러그래프를 `StoryParagraph` 테이블에 저장
* 동일한 내용을 `ParagraphVersion` 테이블에도 버전 1로 저장


StoryParagraph

| 필드명                        | 설명                        |
| -------------------------- | ------------------------- |
| `story`                    | 연결된 Story 객체 (ForeignKey) |
| `paragraph_no`             | 스토리 내 순서                  |
| `content_text`             | 본문 내용                     |
| `created_at`, `updated_at` | 생성/수정 시간                  |

ParagraphVersion

| 필드명                                          | 설명            |
| -------------------------------------------- | ------------- |
| `paragraph`                                  | 연결된 문단        |
| `version_no`                                 | 버전 (1부터 시작)   |
| `content_text`, `generated_by`, `created_at` | 내용, 출처, 생성 시각 |

```python
# 작성자 : 최준혁
# 기능 : 생성된 패러그래프를 StoryParagraph 테이블에 저장
#       동일한 내용을 ParagraphVersion 테이블에 v1로 저장
# 마지막 수정일 : 2025-06-03
from api.models import Storyparagraph, Paragraphversion
from django.utils import timezone

def save_paragraph(state: dict) -> dict:
    story_id = state.get("story_id")
    paragraph_text = state.get("paragraph_text")

    # 단락 번호 계산 : 현재 story_id에서 가장 높은 번호 + 1
    last_para = Storyparagraph.objects.filter(story_id=story_id).order_by("-paragraph_no").first()
    next_no = (last_para.paragraph_no + 1) if last_para else 1

    # StoryParagraph 테이블에 저장
    paragraph = Storyparagraph.objects.create(
        story_id=story_id,
        paragraph_no=next_no,
        content_text=paragraph_text,
        created_at=timezone.now(),
        updated_at=timezone.now()
    )

    # ParagraphVersion 저장 (v1)
    Paragraphversion.objects.create(
        paragraph_id=paragraph.paragraph_id,
        version_no=1,
        content_text=paragraph_text,
        generated_by=str(state.get("user_id")),
        created_at=timezone.now()
    )

    return {
        **state,
        "paragraph_id": paragraph.paragraph_id,
        "paragraph_no": next_no
    }
```


<br>

#### 3. save_qa
* 사용자 입력(질문)과 생성된 응답(패러그래프)을 `ParagraphQA` 테이블에 저장

|항목|설명|
|---|---|
|`question_text`|사용자가 입력한 메시지|
|`answer_text`|챗봇이 생성한 패러그래프|
|`paragraph_id`, `story_id`|해당 문단/동화와 연결|
|`created_at`|생성 시각|

``` python
from api.models import Paragraphqa

# 작성자 : 최준혁
# 기능 : 사용자 입력과 패러그래프를 ParagraphQA에 저장
# 마지막 수정일 : 2025-06-03
def save_qa(state: dict) -> dict:
    Paragraphqa.objects.create(
        paragraph_id=state.get("paragraph_id"),
        story_id=state.get("story_id"),
        question_text=state.get("input"),
        answer_text=state.get("paragraph_text"),
        created_at=timezone.now()
    )

    return state

```




#### 4. update_paragraph_version
* 기존 문단(`paragraph_id`)에 대해 사용자의 요청으로 내용을 수정
* `ParagraphVersion` 테이블에 새 버전(`version_no + 1`)을 추가
* `StoryParagraph` 테이블의 본문도 최신 내용으로 업데이트


#### 플로우 분기
|목적|함수|설명|
|---|---|---|
|새로운 문단 생성|`generate → save_paragraph → save_qa`|지금 만든 기본 흐름|
|기존 문단 수정|`generate → update_paragraph_version → save_qa`|수정 흐름|

```python
# 작성자 : 최준혁
# 기능 : 기존 paragraph_id의 문단 내용을 수정하여 ParagraphVersion에 새 버전을 추가하고,
#        StoryParagraph의 본문도 최신 내용으로 업데이트
# 마지막 수정일 : 2025-06-03

from api.models import StoryParagraph, ParagraphVersion
from django.utils import timezone

def update_paragraph_version(state: dict) -> dict:
    paragraph_id = state.get("paragraph_id")
    new_text = state.get("paragraph_text")
    user_id = state.get("user_id")

    # 현재 버전 번호 조회
    last_version = ParagraphVersion.objects.filter(paragraph_id=paragraph_id).order_by('-version_no').first()
    next_version = (last_version.version_no + 1) if last_version else 2

    # ParagraphVersion 테이블에 새 버전 추가
    ParagraphVersion.objects.create(
        paragraph_id=paragraph_id,
        version_no=next_version,
        content_text=new_text,
        generated_by=str(user_id),
        created_at=timezone.now()
    )

    # StoryParagraph 테이블 본문 업데이트
    StoryParagraph.objects.filter(paragraph_id=paragraph_id).update(
        content_text=new_text,
        updated_at=timezone.now()
    )

    return {
        **state,
        "version_no": next_version
    }
```


<br>

## Step 3: LangGraph 플로우 정의
* `story_flow.py`에서 LangGraph 구성
* 경로: `back/api/services/langgraph/story_flow.py`
#### 처리흐름 요약
``` text
(1) GenerateParagraph → (2) SaveParagraph → (3) SaveQA     [create 모드]
(1) GenerateParagraph → (2) UpdateParagraphVersion → (3) SaveQA     [edit 모드]
```

```python
# LangGraph 플로우 정의
# 작성자 : 최준혁
# 작성일 : 2025-06-03

from langgraph.graph import StateGraph
from typing import TypedDict, Literal
from api.services.langgraph.nodes import (
    generate_paragraph,             # Gemini로 문단 생성
    save_paragraph,                 # 신규 문단 저장
    save_qa,                        # 사용자 입력과 응답을 QA 테이블에 저장
    update_paragraph_version        # 기존 문단 수정 및 버전 추가
)


# 작성자 : 최준혁
# 기능 : 상태를 정의하는 클래스
#       LangGraph 실행 중 상태(state)에 저장/전달되는 키와 타입을 명시
# 마지막 수정일 : 2025-06-03
class StoryState(TypedDict, total=False):
    input: str                      # 사용자 입력 문장
    user_id: int                    # 사용자 ID
    story_id: int                   # 대상 동화 ID
    age: int                        # 사용자 연령
    paragraph_id: int               # 단락 ID (수정 시 필요)
    paragraph_no: int               # 단락 번호
    paragraph_text: str             # 생성된 패러그래프 텍스트
    version_no: int                 # 버전 번호 (수정 시 증가)
    mode: Literal["create", "edit"] # 생성 모드 or 수정 모드


# 작성자 : 최준혁
# 기능 : 흐름 분기 함수
#       mode 값에 따라 "SaveParagraph" 또는 "UpdateParagraphVersion" 노드로 분기
# 마지막 수정일 : 2025-06-03
def mode_router(state: StoryState) -> str:
    if state.get("mode") == "edit":
        return "UpdateParagraphVersion"
    else:
        return "SaveParagraph"


# 작성자 : 최준혁
# 기능 : LangGraph 플로우 정의 함수
#       각 노드를 순서대로 등록하고, 조건에 따라 분기되도록 그래프 구성
# 마지막 수정일 : 2025-06-03
def story_flow():
    graph = StateGraph(StoryState)
    
    # 노드 등록
    graph.add_node("GenerateParagraph", generate_paragraph)
    graph.add_node("SaveParagraph", save_paragraph)
    graph.add_node("UpdateParagraphVersion", update_paragraph_version)
    graph.add_node("SaveQA", save_qa)

    # 시작점 설정
    graph.set_entry_point("GenerateParagraph")

    # 분기: create vs edit
    graph.add_conditional_edges("GenerateParagraph", mode_router)

    # 각각의 흐름 다음에 저장
    graph.add_edge("SaveParagraph", "SaveQA")
    graph.add_edge("UpdateParagraphVersion", "SaveQA")

    # 종료 노드 설정
    graph.set_finish_point("SaveQA")

    # 컴파일된 그래프 반환
    flow = graph.compile()
    return flow
```

<br>

## Step 4: LangGraph실행
* 사용자가 프론트에서 보낸 요청(`input`, `user_id`, `story_id`, `age`, `mode`, `paragraph_id`)을 받아  `LangGraph` 플로우(`story_flow`)를 실행하고 결과를 응답하는 API를 `views.py`에 정의
* 경로: `back/api/views.py`


#### 1. views.py
```python
# 작성자 : 최준혁
# 기능 : news 페이지에서 호출하는 LangGraph 기반 동화 생성 API
# 마지막 수정일 : 2025-06-03

from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.services.langgraph.story_flow import story_flow
from api.models import User

# LangGraph 실행 객체 초기화
flow = story_flow()

@api_view(["POST"])
def chatbot_news_story(request):
    user_id = request.data.get("user_id")
    story_id = request.data.get("story_id")
    paragraph_id = request.data.get("paragraph_id")  # edit 모드일 경우
    mode = request.data.get("mode", "create")
    user_input = request.data.get("input")

    # 사용자 정보에서 나이 조회
    user = User.objects.get(user_id=user_id)

    # LangGraph 상태 구성
    initial_state = {
        "input": user_input,
        "user_id": user_id,
        "story_id": story_id,
        "age": user.age,
        "mode": mode
    }

    if mode == "edit" and paragraph_id:
        initial_state["paragraph_id"] = paragraph_id

    # LangGraph 실행
    result = flow.invoke(initial_state)

    return Response({
        "paragraph": result["paragraph_text"],
        "paragraph_no": result.get("paragraph_no"),
        "version_no": result.get("version_no"),
        "paragraph_id": result.get("paragraph_id")
    })
```


<br>

#### 2. URL연결
* 경로: `back/api/urls.py`에 추가
``` python
from .views import chatbot_news_story

urlpatterns = [
    path('v1/chat/story/', chatbot_story, name='api_chatbot_story'),

]
```


<br>

## Step 5: Next.js 페이지 연동
* 사용자가 `news` 페이지에서 텍스트를 입력하면  
* `POST /v1/chat/story/` API를 호출해서  
* 챗봇이 문단을 생성하고 이를 화면에 출력
* **테스트를 위해 기존의 news페이지를 사용하겠습니다.**
* 경로: `front/app/news/page.tsx`


``` tsx
'use client';

import { useState, useRef, useEffect } from 'react';
import axios from 'axios';


// LangGraph 기반 동화 생성 API 호출 함수
const getAIResponse = async (msg: string): Promise<string> => {
  try {
    const res = await axios.post('http://localhost:8000/v1/chat/story/', {
      input: msg,
      user_id: 1,
      story_id: 3,
      mode: 'create'
    });
    return res.data?.paragraph || '동화를 생성할 수 없습니다.';
  } catch (error) {
    console.error('LangGraph 요청 실패:', error);
    return '서버에 연결할 수 없습니다.';
  }
};

export default function GeminiStoryChatbot() {
  const [messages, setMessages] = useState([
    { sender: 'ai', text: "안녕하세요! 🧒 재미나이와 함께 동화를 만들어봐요. 주제나 상황을 입력해보세요!" }
  ]);
  const [input, setInput] = useState('');
  const chatContainerRef = useRef<HTMLDivElement>(null);

  // 메시지 추가될 때마다 자동 스크롤
  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
    }
  }, [messages]);

  // 메시지 전송 핸들러
  const handleSend = async () => {
    const trimmed = input.trim();
    if (!trimmed) return;

    setMessages(prev => [...prev, { sender: 'user', text: trimmed }]);
    setInput('');

    const aiResponse = await getAIResponse(trimmed);
    setMessages(prev => [...prev, { sender: 'ai', text: aiResponse }]);
  };

  const handleClear = () => {
    setMessages([
      { sender: 'ai', text: "안녕하세요! 🧒 재미나이와 함께 동화를 만들어봐요. 주제나 상황을 입력해보세요!" }
    ]);
  };

  return (
    <main className="bg-gray-50 min-h-screen px-4 py-6">
      <div className="container mx-auto max-w-4xl">

        {/* 헤더 */}
        <div className="mb-6">
          <h1 className="text-2xl md:text-3xl font-bold text-gray-800">🧒 재미나이 동화 생성 챗봇</h1>
          <p className="text-gray-600 text-sm mt-1">예: “작은 여우가 눈 오는 날 길을 잃었어”</p>
        </div>

        {/* 채팅 창 */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200 mb-4">
          <div className="flex items-center px-4 py-3 border-b border-gray-200 bg-gray-50 rounded-t-lg">
            <div className="flex items-center space-x-2">
              <div className="w-3 h-3 bg-green-500 rounded-full" />
              <span className="text-sm font-medium text-gray-700">재미나이</span>
            </div>
          </div>

          <div
            ref={chatContainerRef}
            className="overflow-y-auto h-[calc(100vh-300px)] min-h-[400px] p-4 space-y-4"
          >
            {messages.map((msg, idx) => (
              <div key={idx} className={`flex space-x-3 animate-fadeIn ${msg.sender === 'user' ? 'justify-end' : ''}`}>
                {msg.sender === 'ai' && (
                  <div className="flex-shrink-0 w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center">
                    <span className="text-white text-sm font-medium">AI</span>
                  </div>
                )}
                <div className="flex-1 max-w-md">
                  <div className={`${msg.sender === 'user' ? 'bg-gray-800 text-white' : 'bg-blue-50 text-gray-800'} rounded-lg px-4 py-3`}>
                    <p>{msg.text}</p>
                  </div>
                  <span className="text-xs text-gray-500 mt-1 block text-right">
                    {new Date().toLocaleTimeString('ko-KR', { hour: '2-digit', minute: '2-digit' })}
                  </span>
                </div>
                {msg.sender === 'user' && (
                  <div className="flex-shrink-0 w-8 h-8 bg-gray-600 rounded-full flex items-center justify-center">
                    <span className="text-white text-sm font-medium">U</span>
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* 입력 영역 */}
        <div className="bg-white rounded-lg shadow-sm border border-gray-200">
          <div className="p-4">
            <label className="block text-sm font-medium text-gray-700 mb-2">어떤 이야기를 들려줄까요?</label>
            <div className="flex space-x-2">
              <textarea
                rows={3}
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    handleSend();
                  }
                }}
                className="flex-1 resize-none border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                placeholder="예: 용감한 토끼가 친구를 찾고 있어요"
              />
              <button
                onClick={handleSend}
                className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
              >
                전송
              </button>
            </div>
          </div>
          <div className="px-4 pb-4">
            <button
              onClick={handleClear}
              className="w-full py-3 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition"
            >
              대화 초기화
            </button>
          </div>
        </div>
      </div>
    </main>
  );
}

```


<br>

