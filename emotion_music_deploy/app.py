
import streamlit as st
import pandas as pd

# 頁面設定
st.set_page_config(page_title="情緒音樂推薦系統", layout="centered")
st.title("🎧 情緒音樂推薦系統")
st.markdown("請選擇你的情緒，系統將為你推薦音樂！")

# 讀取資料庫
music_data = pd.read_csv("music_db.csv")

# 下拉選單：顯示情緒選項
emotion_option = st.selectbox("請選擇你的情緒：", music_data["情緒"].unique())

# 推薦邏輯：篩選相同情緒的歌曲
recommendation = music_data[music_data["情緒"] == emotion_option]

# 顯示推薦結果
if not recommendation.empty:
    st.subheader("推薦結果")
    for idx, row in recommendation.iterrows():
        st.markdown(f"🎵 **{row['歌名']}** by {row['歌手']}")
        st.markdown(f"[點我收聽]({row['連結']})")
else:
    st.warning("目前沒有符合此情緒的音樂。")
