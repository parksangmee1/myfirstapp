import streamlit as st
import pandas as pd
import altair as alt

st.title("🌍 국가별 최다 MBTI 유형 분석기")

st.markdown("기본 데이터 파일(`countriesMBTI_16types.csv`)을 사용하여 각 국가에서 가장 많은 MBTI 유형을 시각화합니다.")

# 기본 데이터 파일 경로
default_file_path = "countriesMBTI_16types.csv"

try:
    # CSV 파일 읽기
    df = pd.read_csv(default_file_path)

    # MBTI 유형 컬럼 목록
    mbti_types = [col for col in df.columns if col != "Country"]

    # 각 국가별 가장 높은 MBTI 유형 찾기
    def get_top_mbti(row):
        top_type = row[mbti_types].idxmax()
        top_value = row[top_type]
        return pd.Series([top_type, top_value], index=["Top_MBTI", "Top_Value"])

    df_top = df.copy()
    df_top[["Top_MBTI", "Top_Value"]] = df_top.apply(get_top_mbti, axis=1)

    # 테이블 출력
    st.subheader("📌 국가별 최다 MBTI 유형 테이블")
    st.dataframe(df_top[["Country", "Top_MBTI", "Top_Value"]].sort_values(by="Top_Value", ascending=False))

    # Altair 시각화
    st.subheader("📊 시각화: 국가별 최다 MBTI 유형")
    chart = alt.Chart(df_top).mark_bar().encode(
        x=alt.X("Country:N", sort="-y", title="국가"),
        y=alt.Y("Top_Value:Q", title="비율"),
        color=alt.Color("Top_MBTI:N", title="MBTI"),
        tooltip=["Country", "Top_MBTI", "Top_Value"]
    ).properties(
        width=800,
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

except FileNotFoundError:
    st.error("❌ 'countriesMBTI_16types.csv' 파일을 찾을 수 없습니다. 파일이 현재 폴더에 존재하는지 확인해주세요.")
