import streamlit as st

# MBTI별 포켓몬 추천 딕셔너리
mbti_pokemon = {
    "ISTJ": ("이상해씨", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/001.png", "책임감 있고 신중한 이상해씨!"),
    "ISFJ": ("이브이", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png", "배려심 많고 순한 이브이!"),
    "INFJ": ("뮤", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/151.png", "신비롭고 따뜻한 뮤!"),
    "INTJ": ("뮤츠", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/150.png", "전략적인 천재 뮤츠!"),
    "ISTP": ("파이리", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png", "과감하고 도전적인 파이리!"),
    "ISFP": ("푸린", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/039.png", "감성 넘치는 푸린!"),
    "INFP": ("피카츄", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png", "따뜻하고 용감한 피카츄!"),
    "INTP": ("메타몽", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/132.png", "창의적이고 유연한 메타몽!"),
    "ESTP": ("리자몽", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/006.png", "역동적이고 강한 리자몽!"),
    "ESFP": ("토게피", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/175.png", "사교적이고 귀여운 토게피!"),
    "ENFP": ("피츄", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/172.png", "생기발랄한 피츄!"),
    "ENTP": ("나옹", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/052.png", "재치 넘치는 나옹!"),
    "ESTJ": ("거북왕", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/009.png", "단호하고 신뢰가는 거북왕!"),
    "ESFJ": ("라프라스", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/131.png", "친절하고 따뜻한 라프라스!"),
    "ENFJ": ("루기아", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/249.png", "영감을 주는 리더, 루기아!"),
    "ENTJ": ("갸라도스", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/130.png", "카리스마 넘치는 갸라도스!"),
}

# 앱 제목
st.title("💖 MBTI별 포켓몬 추천기")

st.markdown("당신의 MBTI 유형을 선택하면, 성격에 어울리는 귀여운 포켓몬 친구를 추천해드릴게요!")

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택해주세요:", list(mbti_pokemon.keys()))

# 추천 결과 출력
if mbti:
    name, image_url, description = mbti_pokemon[mbti]
    st.subheader(f"🧬 {mbti} 유형에게 추천하는 포켓몬은...")
    st.image(image_url, width=200)
    st.markdown(f"### 🎉 {name}!")
    st.markdown(f"_{description}_")
