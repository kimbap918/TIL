
### 1. LangGraph의 상태(state) 전파 구조에 대한 본질적 이해 부족 → 구조 전환

- **왜 기억에 남는가?**
    - LangGraph는 ‘함수 호출 순서’가 아니라 ‘상태와 조건’으로 흐름이 결정되는 구조.
    - `story_plan`, `story`, `paragraph_no` 등의 상태를 누락하면 예상과 달리 흐름이 통제되지 않음.
        
- 문제 상황:
    - `RetrieveContext`가 summary 없이 실행 → 빈 context 반환.
    - `story`를 매번 DB에서 불러와 성능 저하.
- 결정적 교훈:  
	-> "LangGraph는 state가 설계의 핵심이다. 모든 노드는 이 state를 통해 이어져야 하고, 누락된 값은 흐름 자체를 무너뜨린다."
    
- 해결책: `passthrough_start`에서 모든 핵심 정보 캐싱 routers.
    

---

### 2. 문체 일관성 유지 실패 → LLM과 협업할 때 ‘톤 조절’의 어려움

- **왜 기억에 남는가?**
    - 이야기 중간에 갑자기 “~했다”, “~하였다”로 문체가 바뀌며 감정이 깨짐.
    - 이건 코드의 문제가 아니라 LLM과의 협업 방식(프롬프트 설계)에서 발생한 구조적 문제.
        
-  문제 상황:
    - 초반: “친절한 ~해요” 말투
    - 중반: “간다”, “했다”로 돌변 → 사용자 경험 망침
        
- 결정적 교훈:  
    -> "LLM은 일관된 말투를 기본적으로 유지하지 않는다. 철저한 톤/스타일 가이드는 개발자의 책임이다."
    
- **해결책**: 모든 문장 끝은 ~어요/해요로 강제하는 톤 고정 규칙 도입core_nodes.
    

---

### 3. 기승전결 요약과 실제 이야기 전개 간 괴리 → 요약은 ‘계획이자 약속’이라는 인식
- 왜 기억에 남는가?
    - `summary_4step`으로 흐름을 짜고도, 모델이 전혀 다른 방향으로 진행함.
    - 사용자 입력이 들어오면 흐름이 갑자기 틀어짐.
- 문제 상황:
    - 예: “토끼와 거북이 경주”를 요청했지만 중간에 토끼가 우주선 타고 사라짐.
- 결정적 교훈:  
    -> "요약은 단순 참고가 아니라 이야기의 레일이다. 이탈하지 않도록 감시하고 필요 시 유연하게 재작성해야 한다."
- 해결책: `detect_and_update_story`에서 의미 있는 입력이 있을 경우 summary 자체를 업데이트summary_utils.
    

---

### 4. 캐릭터가 중복 등장하거나 프로필이 덮어지는 문제 → 정체성 보존의 중요성

- 왜 기억에 남는가?
    - 캐릭터 이름은 같고 프로필만 바뀜. 결국 “봉치”가 두 종류의 동물이 됨.
    - 이는 단순 중복 문제가 아니라, **사용자가 몰입했던 캐릭터의 정체성이 무너지는 문제**.
- 트리거가 된 상황:
    - LLM이 자동으로 캐릭터를 뽑아낼 때 이전 설정을 기억하지 못함.
- 결정적 교훈:  
    -> "아이들의 이야기에선 캐릭터의 '일관성'이 모든 것을 좌우한다. 캐릭터는 덮어쓰기보다 보호되어야 한다."
    
- 해결책: `is_similar_name`, `is_duplicate_character`로 중복 방지 및 정체성 보존character_utils.
    

---

### 5. 마지막 문단(결말)의 설계 → 서사의 완결감은 개발자의 책임

- **왜 기억에 남는가?**
    
    - 문단이 계속 이어지거나, 마지막 문단이 너무 짧고 맥이 끊기는 느낌을 줌.
        
    - 사용자는 “끝났는지 모르겠어요”, “이건 결말 같지 않아요” 같은 피드백을 줌.
        
- **트리거가 된 상황**:
    
    - 10문단이 넘어도 story가 계속됨.
        
    - 마지막 문단이 문체도 어색하고, 여운 없이 끝남.
        
- **결정적 교훈**:  
    👉 "결말은 기능이 아니라 감정이다. 끝났다는 걸 기술적으로 ‘조건문’으로 판단할 수 없다. 여운 있게 마무리해야 한다."
    
- **해결책**:
    
    - `generate_paragraph`에 paragraph_no == 10이면 `[질문]`, `[행동]` 생략
        
    - `finalize_story_output`으로 따뜻한 제목 + 요약 + 10단락 정리finalize_utilscore_nodes
        

---

## ✨ 총정리: 너의 개발적 성장에 가장 기여한 교훈들

|문제|너에게 남긴 교훈|
|---|---|
|상태 전파 누락|**LangGraph는 상태 중심이다. 모든 흐름은 state가 좌우한다.**|
|문체 변화|**LLM은 톤을 기억하지 않는다. 톤은 설계자가 지켜야 한다.**|
|요약-실제 불일치|**계획은 지켜야 하고, 필요하면 수정하되 흐름은 유지해야 한다.**|
|캐릭터 중복|**스토리의 인물은 데이터가 아닌 존재다. 덮지 말고 지켜줘야 한다.**|
|결말 불완전|**이야기의 끝은 코드가 아니라 감정이다.**|