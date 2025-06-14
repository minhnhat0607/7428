import streamlit as st
import random

# Cấu hình tiêu đề trang
st.set_page_config(page_title="Cờ Cá Ngựa HTML", page_icon="🐴")
st.title("🐴 Cờ Cá Ngựa Mini – Giao diện HTML")

# Khởi tạo trạng thái nếu chưa có
if "position" not in st.session_state:
    st.session_state.position = 0
if "log" not in st.session_state:
    st.session_state.log = []

# Nút gieo xúc xắc
if st.button("🎲 Gieo xúc xắc", key="roll_button"):
    dice = random.randint(1, 6)
    new_pos = st.session_state.position + dice
    if new_pos <= 56:
        st.session_state.position = new_pos
        st.success(f"Gieo được {dice}, đến ô {new_pos}")
    else:
        st.warning(f"Gieo {dice}, vượt quá ô 56 nên không di chuyển.")
    st.session_state.log.append(f"🎲 Gieo {dice} → Vị trí: {st.session_state.position}")

# Giao diện CSS cho bàn cờ
st.markdown("""
    <style>
    .board-container {
        display: flex;
        flex-wrap: wrap;
        width: 360px;
    }
    .cell {
        width: 40px;
        height: 40px;
        border: 1px solid #ccc;
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: bold;
        margin: 2px;
        font-size: 15px;
    }
    .cell.normal {
        background-color: #f0f0f0;
    }
    .cell.current {
        background-color: #ffe066;
    }
    </style>
""", unsafe_allow_html=True)

# Hàm vẽ bàn cờ
def draw_board(position):
    html = '<div class="board-container">'
    for i in range(1, 57):
        if i == position:
            html += '<div class="cell current">🐴</div>'
        else:
            html += f'<div class="cell normal">{i}</div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

# Hiển thị bàn cờ
draw_board(st.session_state.position)

# Nếu đến ô 56 thì hiển thị chúc mừng
if st.session_state.position == 56:
    st.success("🎉 Bạn đã về đích! Chúc mừng!")
    st.balloons()

# Hiển thị lịch sử lượt chơi
with st.expander("📜 Lịch sử lượt chơi"):
    for log in reversed(st.session_state.log):
        st.markdown(f"- {log}")

# Nút reset game (đã thêm key để tránh lỗi trùng ID)
if st.button("🔄 Chơi lại", key="reset_button"):
    st.session_state.position = 0
    st.session_state.log = []
    st.info("🧹 Game đã được đặt lại.")
