import streamlit as st
import random

# 초기 상태 설정
if "cnt" not in st.session_state:
    st.session_state.cnt = 0

if "max_record" not in st.session_state:
    st.session_state.max_record = 0  # 최고 기록 저장용 변수

# 강화 확률 결정 함수
def 강화_확률(단계):
    if 1 <= 단계 <= 10:
        return 100 - 단계 * 1  # 100% - 90%
    elif 11 <= 단계 <= 20:
        return 100 - (단계 - 10) * 2  # 80% - 70%
    elif 21 <= 단계 <= 30:
        return 70 - (단계 - 20) * 2  # 70% - 50%
    elif 31 <= 단계 <= 40:
        return 50 - (단계 - 30) * 3  # 50% - 20%
    elif 41 <= 단계 <= 50:
        return max(5, 20 - (단계 - 40) * 1.5)  # 20% - 5%
    else:
        return 5  # 50단계 이후는 5%

# 현재 단계와 성공 확률 표시
단계 = st.session_state.cnt + 1
확률 = 강화_확률(단계)

st.write(f"현재 단계: {st.session_state.cnt}")
st.write(f"다음 단계: {단계}")
st.write(f"다음 단계 성공 확률: {확률:.2f}%")

# 버튼 클릭 시 실행
if st.button("plus"):
    확률 = 강화_확률(단계)
    성공 = random.random() * 100 <= 확률  # 확률에 따라 성공 여부 결정

    if 성공:
        st.session_state.cnt = 단계  # 성공 시 단계 증가
        st.write(f"강화 성공! 현재 단계: {st.session_state.cnt}")
    else:
        # 최고 기록 갱신
        if st.session_state.cnt > st.session_state.max_record:
            st.session_state.max_record = st.session_state.cnt  # 최고 기록 업데이트
        st.session_state.cnt = 1  # 실패 시 1단계로 초기화
        st.write(f"강화 실패! 현재 단계는 1로 초기화되었습니다.")

st.write(f"현재 단계: {st.session_state.cnt}")
st.write(f"최고 기록: {st.session_state.max_record}")
