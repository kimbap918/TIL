### 툴 사용시 주의사항
1. Cursor : 자동 프로젝트 생성 **절대 하지말것**(토큰비용 매우 많이 나감)
2. Claude code를 사용하는 경우도 주의
	* linux, mac
	* window : wsl 설치 사용 => 윈도우에 linux를 설치하는것을 wsl이라고 함


<br>

향후 개발자는?
1. 개발을 잘 하는 개발자는 필요없음
2. 전체 시스템 로직, 플로우, 프레임워크를 잘 아는 사람
3. 문제를 해결하는 스킬 있는 사람

<br>

### LangGraph 장기기억메모리(LTM)
* 대화한 내용을 영구 메모리에 저장

google "git mem0"
https://github.com/mem0ai/mem0

<공부할 유튜브>
https://www.youtube.com/watch?v=DTVqC8IysiY

<예제소스>
https://github.com/dabidstudio/longterm-memory-agent

아예 API를 모두 구현하는 방법
=> 채팅 = 각각 
=> API

### A2A(Agent To Agent)
* MCP는 Agent가 하나
* A2A는 Agent를 여러개 섞어서 적용
![](https://i.imgur.com/0FnGMa9.png)

| 항목          | A2A (Agent to Agent)                    | MCP (Model Context Protocol)              |
| ----------- | --------------------------------------- | ----------------------------------------- |
| **정의**      | 에이전트 간 직접 상호작용 및 통신 모델                  | 여러 모델이나 기능 간의 문맥 공유를 위한 프로토콜              |
| **구성 방식**   | 분산된 다수의 에이전트들이 각자 의사결정 및 상호작용           | 중심화된 컨텍스트 모델이 여러 모델/모듈과 연동                |
| **상호작용 방식** | 에이전트 간 메시지 교환, 협상, 행동 계획 공유 등           | 모든 입력/출력은 공유된 컨텍스트를 기준으로 작동               |
| **의존성**     | 각 에이전트는 독립적이지만 상호작용 설계 필요               | 모든 구성요소가 동일한 컨텍스트 사양을 따라야 함               |
| **유연성**     | 동적으로 새로운 에이전트 추가 가능                     | 컨텍스트 사양을 바꾸지 않으면 구조가 고정됨                  |
| **문맥 관리**   | 각 에이전트가 자체 상태/목표 관리                     | 전체 문맥이 일원적으로 통합되어 관리됨                     |
| **장점**      | 1. 높은 자율성 2. 병렬성/확장성 우수 3. 협력적 작업 가능    | 1. 일관된 문맥 유지 2. 모듈 간 통합성 높음 3. 디버깅 용이     |
| **단점**      | 1.  통신 복잡성 증가 2. 일관성 보장 어려움 3. 설계 난이도 ↑ | 1. 유연성 부족 가능 2. 초기 설계 비용 큼 3. 단일 실패 지점 위험 |

<br>

#### A2A의 구조
래퍼런스 : https://github.com/a2aproject/A2A
* A2A 구조는 **에이전트 중심 설계**로, 각 에이전트가 독립적인 역할을 수행
* **Skill**, **Card**, **Memory**, **Interface** 등의 구성 요소를 통해 기능을 모듈화하고 외부와 소통하는 구조
* skills : 어떤 능력을 가지고 있는지
* cards : 실제 수행하는 방법
	-> 서버가 가동됨, 만약 card 20개를 가동하면 20개의 서버가 가동

![](https://i.imgur.com/Y2W0XEb.png)
``` graphql
User
 ↓
Interface ↔ Agent
            ├── Skill
            ├── Card
            └── Memory

```

- **User → Interface**: 사용자의 요청은 인터페이스(UI 혹은 API)를 통해 A2A 시스템에 전달됨
- **Interface → Agent**: 에이전트는 사용자 요청을 받아 적절한 하위 모듈(Skill/Card)을 통해 처리
- **Agent 내부**
    - `Skill`: 특정 기능 단위 (예: 요약하기, 검색하기)
    - `Card`: 특정 상황에 대한 반응이나 행동 카드 (일종의 명령 템플릿)
    - `Memory`: 대화나 상호작용 맥락을 저장하고 관리하는 역할
- 에이전트 간 통신이 가능함 (A2A 구조의 핵심)

<br>


#### 1. UV
google -> "python uv"
https://github.com/astral-sh/uv

mac
``` bash
curl -LsSf https://astral.sh/uv/install.sh | sh

~/.local/bin/uv --version
-> uv 0.7.17 (41c218a89 2025-06-29)
```

Anaconda Prompt
```bash
pip install uv
```

<br>

#### 2. 가상환경 설정
``` bash
conda create -n p312_a2a python=3.12
conda activate p312_a2a
```


<br>

#### 3. SDK설치
A2A python SDK
``` bash
pip install a2a-sdk
pip install uv
```


<br>

#### 4. 샘플 프로젝트 파일 설치
https://github.com/a2aproject/a2a-samples

<br>

#### 5. A2A 가동할 Agent
0. demo client 실행
- ModuleNotFoundError : PYTHONPATH=$(pwd) python demo/ui/main.py
```bash
(p312_a2a) ➜  a2a-samples-main find . -type d -name hosts
./samples/python/hosts
(p312_a2a) ➜  a2a-samples-main export PYTHONPATH=$(pwd)/samples/python
(p312_a2a) ➜  a2a-samples-main python demo/ui/main.py
```
1. adk_expense_reimbursement 
2. langgraph(공부)
    https://api.frankfurter.app/  Agent 정보를 전달해주는 파라미터를 미리 설정
3. crewai(이미지 생성 프레임워크)



http://localhost:10000/.well-known/agent.json












