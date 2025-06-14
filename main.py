import streamlit as st
import random

# Cấu hình trang
st.set_page_config(page_title="Cờ Cá Ngựa Có Ô", page_icon="🐴")
st.title("🐴 Cờ Cá Ngựa Mini – Có Bàn Cờ Hiển Thị")

# Khởi tạo trạng thái nếu chưa có
if "position" not in st.session_state:
    st.session_state.position = 0
if "log" not in st.session_state:
    st.session_state.log = []

# Gieo xúc xắc
if st.button("🎲 Gieo xúc xắc"):
    dice = random.randint(1, 6)
    new_pos = st.session_state.position + dice
    if new_pos > 56:
        st.warning(f"Gieo {dice} nhưng không thể vượt quá 56!")
    else:
        st.session_state.position = new_pos
        st.success(f"🎲 Gieo được {dice}, đến ô {new_pos}")
    st.session_state.log.append(f"Gieo {dice}, vị trí: {st.session_state.position}")

# Vẽ bàn cờ
def draw_board(position):
    board_html = ""
    for i in range(1, 57):
        if i == position:
            content = "🐴"  # hình quân cờ
            color = "#FFD700"
        else:
            content = str(i)
            color = "#f0f0f0"
        board_html += f"""
        <div style='
            width: 40px; height: 40px; 
            background-color: {color}; 
            display: inline-flex;
            justify-content: center;
            align-items: center;
            border: 1px solid #ccc;
            margin: 2px;
            font-weight: bold;
        '>{content}</div>
        """
    st.markdown(f"<div style='display:flex; flex-wrap: wrap;'>{board_html}</div>", unsafe_allow_html=True)

draw_board(st.session_state.position)

# Thông báo thắng
if st.session_state.position == 56:
    st.balloons()
    st.success("🎉 Bạn đã về đích!")

# Hiển thị lịch sử
with st.expander("📜 Lịch sử lượt chơi"):
    for log in reversed(st.session_state.log):
        st.markdown(log)

# Nút reset
if st.button("🔄 Chơi lại"):
    st.session_state.position = 0
    st.session_state.log = []
    st.info("Game đã được đặt lại.")
