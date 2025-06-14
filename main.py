import streamlit as st
import random

st.set_page_config(page_title="Game Tài Xỉu", page_icon="🎲")

st.title("🎲 Trò Chơi Tài Xỉu (Mô phỏng học thuật)")
st.markdown("Chọn **Tài (11–17)** hoặc **Xỉu (3–10)** để bắt đầu.")

# Lựa chọn người chơi
choice = st.radio("Bạn chọn cửa nào?", ["Tài", "Xỉu"])

# Nút bắt đầu
if st.button("🎯 Gieo xúc xắc"):
    dice = [random.randint(1, 6) for _ in range(3)]
    total = sum(dice)

    st.write(f"🎲 Kết quả: {dice[0]} + {dice[1]} + {dice[2]} = {total}")

    if 3 <= total <= 10:
        result = "Xỉu"
    else:
        result = "Tài"

    if choice == result:
        st.success(f"✅ Bạn thắng! Kết quả là {result}.")
    else:
        st.error(f"❌ Bạn thua! Kết quả là {result}.")
