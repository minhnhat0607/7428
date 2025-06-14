import streamlit as st
import random

st.set_page_config(page_title="Cờ Cá Ngựa Đơn Giản", page_icon="🐴")
st.title("🐴 Trò chơi Cờ Cá Ngựa (Giản lược – 1 người)")

# Sử dụng session_state để giữ trạng thái
if "position" not in st.session_state:
    st.session_state.position = 0
if "log" not in st.session_state:
    st.session_state.log = []

# Hiển thị vị trí hiện tại
st.markdown(f"🎯 Vị trí hiện tại: `{st.session_state.position}` / 56")

# Nút gieo xúc xắc
if st.button("🎲 Gieo xúc xắc"):
    dice = random.randint(1, 6)
    new_pos = st.session_state.position + dice
    if new_pos > 56:
        new_pos = st.session_state.position  # không đi quá đích
        st.warning(f"Bạn gieo được {dice}, nhưng không thể đi quá 56.")
    else:
        st.session_state.position = new_pos
        st.success(f"🎲 Bạn gieo được {dice}, tiến lên {dice} ô!")

    # Thêm lịch sử
    st.session_state.log.append(f"🎲 Gieo: {dice} ➡️ Vị trí: {st.session_state.position}")

# Kiểm tra thắng
if st.session_state.position == 56:
    st.balloons()
    st.success("🎉 Chúc mừng! Bạn đã về đích!")

# Hiển thị lịch sử
with st.expander("📜 Lịch sử lượt chơi"):
    for item in reversed(st.session_state.log):
        st.markdown(item)

# Nút chơi lại
if st.button("🔄 Chơi lại"):
    st.session_state.position = 0
    st.session_state.log = []
    st.info("Game đã được reset!")
