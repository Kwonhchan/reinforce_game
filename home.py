import streamlit as st
"hello"
st.write("안녕하세요")
st.title("타이틀")
st.header("헤더")
st.subheader("서브헤더")
st.code("print('hello world')") # 코드박스, default = python
with st.echo():
    st.write("이렇게 씁니다.") #명령어를 코드박스로 놓고 동시에 실행
# streamlit run home.py

if st.button("a"):
    st.write("안녕하세요")
else:
    st.write("응 싫어~")

st.button("b")