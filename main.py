import streamlit as st
import random

# --- Cấu hình trang ---
st.set_page_config(page_title="Tiến Lên", page_icon="🃏")
st.title("🃏 Game Rút Bài – Tiến Lên Miền Nam")

# --- Khởi tạo bộ bài ---
suits = ["♠", "♥", "♦", "♣"]
ranks = ["2", "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3"]
deck = [f"{rank}{suit}" for suit in suits for rank in ranks]

# --- Tải hình ảnh bài ---
def get_card_url(card):
    suit_map = {"♠": "S", "♥": "H", "♦": "D", "♣": "C"}
    rank_map = {"A": "A", "K": "K", "Q": "Q", "J": "J", "10": "T", "9": "9", "8": "8", "7": "7", "6": "6", "5": "5", "4": "4", "3": "3", "2": "2"}
    rank = "".join([c for c in card if c.isalnum()])
    suit = card[-1]
    return f"https://raw.githubusercontent.com/hayeah/playing-cards-assets/master/png/{rank_map[rank]}{suit_map[suit]}.png"

# --- Trạng thái người chơi ---
if "drawn_cards" not in st.session_state:
    st.session_state.drawn_cards = []

# --- Rút bài ---
if st.button("🎲 Rút 1 lá bài", key="draw_button"):
    available_cards = list(set(deck) - set(st.session_state.drawn_cards))
    if available_cards:
        drawn = random.choice(available_cards)
        st.session_state.drawn_cards.append(drawn)
    else:
        st.warning("🛑 Bạn đã rút hết tất cả 52 lá bài!")

# --- Hiển thị các lá đã rút ---
st.subheader("🃏 Các lá bài đã rút:")
cols = st.columns(8)
for i, card in enumerate(st.session_state.drawn_cards):
    with cols[i % 8]:
        st.image(get_card_url(card), width=80)
        st.caption(card)

# --- Nút chơi lại ---
if st.button("🔄 Chơi lại", key="reset_button"):
    st.session_state.drawn_cards = []
    st.experimental_rerun()
