import streamlit as st
import random

# Cấu hình tiêu đề trang
st.set_page_config(page_title="Cờ Cá Ngựa HTML", page_icon="🐴")
st.title("🐴 Cờ Cá Ngựa Mini – Giao diện HTML")

# Khởi tạo trạng thái
if "position" not in st.session_state:
    st.session_state.position = 0
if "log" not in st.session_state:
    st.session_state.log = []

# Gieo xúc xắc
if st.button("🎲 Gieo xúc xắc"):
    dice = random.randint(1, 6)
    new_pos = st.session_state.position + dice
    if new_pos <= 56:
        st.session_state.position = new_pos
        st.success(f"Gieo được {dice}, tiến đến ô {new_pos}")
    else:
        st.warning(f"Gieo được {dice}, nhưng vượt quá ô 56.")
    st.session_state.log.append(f"🎲 Gieo {dice} → Vị trí: {st.session_state.position}")

# Vẽ bàn cờ bằng HTML
def draw_html_board(position):
    st.markdown(
        """
        <style>
        .board-container {
            display: flex;
            flex-wrap: wrap;
            width: 360px;
        }
        .cell {
            width: 40px;
            height: 40px;
            border: 1px solid #999;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 2px;
            font-weight: bold;
            font-size: 16px;
        }
        .cell.normal {
            background-color: #f1f1f1;
        }
        .cell.current {
            background-color: #ffe066;
        }
        </style>
        """, unsafe_allow_html=True
    )

    html_board = '<div class="board-container">'
    for i in range(1, 57):
        if i == position:
            html_board += f"<div class='cell current'>🐴</div>"
        else:
            html_board += f"<div class='cell normal'>{i}</div>"
    html_board += '</div>'
    st.markdown(html_board, unsafe_allow_html=True)

# Hiển thị bàn cờ
draw_html_board(st.session_state.position)

# Thông báo chiến thắng
if st.session_state.position == 56:
    st.balloons()
    st.success("🎉 Chúc mừng! Bạn đã về đích!")

# Hiển thị lịch sử
with st.expander("📜 Lịch sử lượt chơi"):
    for log in reversed(st.session_state.log):
        st.markdown(log)

# Reset trò chơi
if st.button("🔄 Chơi lại"):
    st.session_state.position = 0
    st.session_state.log = []
    st.info("Đã đặt lại trò chơi.")

# Nút reset
if st.button("🔄 Chơi lại"):
    st.session_state.position = 0
    st.session_state.log = []
    st.info("Đã đặt lại trò chơi.")
