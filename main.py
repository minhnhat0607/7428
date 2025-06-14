import streamlit as st
import random

# Cấu hình trang
st.set_page_config(page_title="Cờ Cá Ngựa Có Ô", page_icon="🐴")
st.title("🐴 Cờ Cá Ngựa Mini – Bản đơn giản")

# Khởi tạo trạng thái nếu chưa có
if "position" not in st.session_state:
    st.session_state.position = 0
if "log" not in st.session_state:
    st.session_state.log = []

# Gieo xúc xắc
if st.button("🎲 Gieo xúc xắc"):
    dice = random.randint(1, 6)
    if st.session_state.position + dice <= 56:
        st.session_state.position += dice
        st.success(f"Gieo được {dice} → đến ô {st.session_state.position}")
    else:
        st.warning(f"Gieo {dice} → Vượt quá 56, không di chuyển.")
    st.session_state.log.append(f"Gieo {dice}, đến ô {st.session_state.position}")

# Vẽ bàn cờ (56 ô)
def draw_board(position):
    board_html = ""
    for i in range(1, 57):
        if i == position:
            content = "🐴"  # Quân cờ
            color = "#FFEB3B"
        else:
            content = str(i)
            color = "#FFFFFF"
        board_html += f"""
        <div style='
            width: 40px; height: 40px; 
            background-color: {color}; 
            display: inline-flex;
            justify-content: center;
            align-items: center;
            border: 1px solid #000;
            margin: 2px;
            font-weight: bold;
        '>{content}</div>
        """
    # Hiển thị bàn cờ dạng grid 8x7 (56 ô)
    st.markdown(f"<div style='display:flex; flex-wrap: wrap; width: 360px;'>{board_html}</div>", unsafe_allow_html=True)

draw_board(st.session_state.position)

# Thắng
if st.session_state.position == 56:
    st.balloons()
    st.success("🎉 Chúc mừng! Bạn đã về đích!")

# Lịch sử lượt chơi
with st.expander("📜 Lịch sử lượt chơi"):
    for log in reversed(st.session_state.log):
        st.markdown(f"- {log}")

# Nút reset
if st.button("🔄 Chơi lại"):
    st.session_state.position = 0
    st.session_state.log = []
    st.info("Đã đặt lại trò chơi.")
