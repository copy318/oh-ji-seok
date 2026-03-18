import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, time

st.set_page_config(page_title="Streamlit 요소 시연", layout="wide")

st.title("🎈 Streamlit 주요 요소 시연")
st.markdown("Streamlit이 제공하는 다양한 UI 요소들을 확인해보세요.")

# 사이드바
st.sidebar.title("📋 네비게이션")
page = st.sidebar.radio("항목 선택", [
    "텍스트 요소",
    "사용자 입력",
    "데이터 표시",
    "차트",
    "미디어",
    "레이아웃",
    "상태 관리"
])

# ============ 텍스트 요소 ============
if page == "텍스트 요소":
    st.header("📝 텍스트 요소")
    
    st.subheader("제목들")
    st.write("이것은 st.write()로 표시된 텍스트입니다.")
    st.markdown("**굵은 텍스트**, *기울임*, `코드`, [링크](https://streamlit.io)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("✅ 성공 메시지")
        st.info("ℹ️ 정보 메시지")
    with col2:
        st.warning("⚠️ 경고 메시지")
        st.error("❌ 에러 메시지")

# ============ 사용자 입력 ============
elif page == "사용자 입력":
    st.header("👆 사용자 입력 요소")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("텍스트 입력")
        name = st.text_input("이름을 입력하세요:", "홍길동")
        text_area = st.text_area("설명을 입력하세요:", "여기에 긴 텍스트를 작성하세요...")
        
    with col2:
        st.subheader("숫자 입력")
        age = st.number_input("나이:", min_value=0, max_value=120, value=30)
        score = st.slider("점수를 선택하세요:", 0, 100, 50)
    
    st.subheader("선택 요소")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        checkbox = st.checkbox("동의합니다")
        radio = st.radio("선택하세요:", ["옵션 A", "옵션 B", "옵션 C"])
    
    with col2:
        selectbox = st.selectbox("드롭다운 선택:", ["선택 1", "선택 2", "선택 3"])
        multiselect = st.multiselect("복수 선택:", ["A", "B", "C", "D"], default=["A"])
    
    with col3:
        date = st.date_input("날짜 선택:", datetime.now())
        time_val = st.time_input("시간 선택:", time(12, 0))
    
    st.subheader("입력 결과")
    if st.button("결과 표시"):
        st.write(f"이름: {name}, 나이: {age}, 점수: {score}")
        st.write(f"선택사항: {radio}, 동의: {checkbox}")

# ============ 데이터 표시 ============
elif page == "데이터 표시":
    st.header("📊 데이터 표시 요소")
    
    # 샘플 데이터 생성
    df = pd.DataFrame({
        "이름": ["Alice", "Bob", "Charlie", "David"],
        "나이": [25, 30, 35, 28],
        "도시": ["서울", "부산", "대구", "인천"],
        "판매액": [100, 200, 150, 300]
    })
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("총 인원", len(df))
    with col2:
        st.metric("평균 나이", f"{df['나이'].mean():.1f}")
    with col3:
        st.metric("총 판매액", df["판매액"].sum())
    with col4:
        st.metric("최대 판매액", df["판매액"].max())
    
    st.subheader("테이블")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**DataFrames**")
        st.dataframe(df, use_container_width=True)
    with col2:
        st.write("**정적 테이블**")
        st.table(df)

# ============ 차트 ============
elif page == "차트":
    st.header("📈 차트 요소")
    
    # 샘플 데이터
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["A 상품", "B 상품", "C 상품"]
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("선 그래프")
        st.line_chart(chart_data)
        
        st.subheader("영역 그래프")
        st.area_chart(chart_data)
    
    with col2:
        st.subheader("막대 그래프")
        st.bar_chart(chart_data)
        
        st.subheader("산점도")
        scatter_data = pd.DataFrame(
            np.random.randn(100, 2),
            columns=["X", "Y"]
        )
        st.scatter_chart(scatter_data)

# ============ 미디어 ============
elif page == "미디어":
    st.header("🎬 미디어 요소")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("이미지")
        st.image("https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", 
                width=300)
    
    with col2:
        st.subheader("오디오/비디오")
        st.info("오디오/비디오는 URL이나 로컬 파일을 사용할 수 있습니다.")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# ============ 레이아웃 ============
elif page == "레이아웃":
    st.header("🎨 레이아웃 요소")
    
    st.subheader("열(Columns)")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("### 열 1")
        st.write("첫 번째 열의 내용")
    with col2:
        st.write("### 열 2")
        st.write("두 번째 열의 내용")
    with col3:
        st.write("### 열 3")
        st.write("세 번째 열의 내용")
    
    st.subheader("탭(Tabs)")
    tab1, tab2, tab3 = st.tabs(["탭 1", "탭 2", "탭 3"])
    with tab1:
        st.write("탭 1의 내용입니다.")
    with tab2:
        st.write("탭 2의 내용입니다.")
    with tab3:
        st.write("탭 3의 내용입니다.")
    
    st.subheader("확장 영역(Expander)")
    with st.expander("자세히 보기"):
        st.write("숨겨진 내용이 여기에 있습니다.")
        st.code("print('Hello Streamlit!')")
    
    st.subheader("컨테이너(Container)")
    container = st.container(border=True)
    container.write("### 테두리가 있는 컨테이너")
    container.write("이것은 테두리로 구분된 영역입니다.")

# ============ 상태 관리 ============
elif page == "상태 관리":
    st.header("💾 상태 관리 (Session State)")
    
    st.write("""
    Session State를 사용하면 사용자 상호작용 간에 데이터를 유지할 수 있습니다.
    """)
    
    if "counter" not in st.session_state:
        st.session_state.counter = 0
    
    if "input_text" not in st.session_state:
        st.session_state.input_text = ""
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("증가 +"):
            st.session_state.counter += 1
    with col2:
        if st.button("감소 -"):
            st.session_state.counter -= 1
    with col3:
        if st.button("초기화"):
            st.session_state.counter = 0
    
    st.metric("카운터 값", st.session_state.counter)
    
    st.subheader("텍스트 저장")
    st.session_state.input_text = st.text_input("텍스트 입력:", 
                                                 value=st.session_state.input_text)
    st.write(f"저장된 텍스트: {st.session_state.input_text}")

# 푸터
st.divider()
st.markdown("""
---
**학습 자료**
- [Streamlit 공식 문서](https://docs.streamlit.io/)
- [Streamlit 갤러리](https://streamlit.io/gallery)
- [Streamlit 치트시트](https://cheat-sheet.streamlit.app/)
""")
