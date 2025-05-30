import streamlit as st

# 타이틀
st.title("LangChain 챗봇")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for content in st.session_state.chat_history:
    with st.chat_message(content["role"]):
        st.markdown(content["content"])

# 입력창
if prompt := st.chat_input("메시지를 입력하세요."):
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.chat_history.append({"role":"user", "massage": prompt})

    with st.chat_message("ai"):
        response = f'{prompt} 내용이 입력되었습니다.'
        st.markdown(response)
        st.session_state.chat_history.append({"role":"ai", "message": response})
