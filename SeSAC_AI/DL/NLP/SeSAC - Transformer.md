positional encoding
https://erdem.pl/2021/05/understanding-positional-encoding-in-transformers

positional encoding : 단어의 상대적인 위치나 순서를 인식하기 위해 사용되는데, 


트렌스포머에 사용되는 3가지 어텐션이 있는데
셀프 어텐션은 Query, Key, Value가 동일한 경우


단어 i에 대한 Q벡터가 있고, 단어 i에 대한 Q벡터가 모든 K벡터 i am a student에 대해 어텐션 스코어를 구합니다. 단어 I가 단어 I, am, a, student와 얼마나 연관되어 있는지 