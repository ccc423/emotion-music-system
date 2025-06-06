import streamlit as st
import pandas as pd

# 頁面設定
st.set_page_config(page_title="情緒音樂推薦系統", layout="centered")
st.title("🎧 情緒音樂推薦系統")
st.markdown("請輸入一句話，系統將分析你的情緒並推薦對應的音樂")

# 讀取資料庫
music_data = pd.read_csv("music_db.csv")

# 情緒判斷函式（關鍵字邏輯）
def detect_emotion(text):
    text = text.lower()
    if any(word in text for word in ["開心", "快樂", "開朗", "喜悅"]):
        return "開心"
    elif any(word in text for word in ["平靜", "安靜", "放鬆", "冷靜"]):
        return "平靜"
    elif any(word in text for word in ["難過", "悲傷", "憂鬱", "失落"]):
        return "憂鬱"
    elif any(word in text for word in ["激動", "衝動", "興奮", "熱血"]):
        return "激昂"
    else:
        return "未知"

# 文字輸入區
user_input = st.text_input("請描述你現在的心情：")

if user_input:
    emotion = detect_emotion(user_input)
    st.markdown(f"🧠 判斷情緒：**{emotion}**")

    if emotion != "未知":
        recommendation = music_data[music_data["情緒"] == emotion]
        if not recommendation.empty:
            st.subheader("🎶 推薦音樂")
            for idx, row in recommendation.iterrows():
                st.markdown(f"🎵 **{row['歌名']}** by {row['歌手']}")
                st.markdown(f"[▶ 點我收聽]({row['連結']})")
        else:
            st.warning("資料庫中沒有符合此情緒的音樂。")
    else:
        st.warning("無法判斷你的情緒，請換個方式描述看看～")
