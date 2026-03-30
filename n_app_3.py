import streamlit as st

st.set_page_config(page_title="Catch the Heart 💖", page_icon="💖", layout="centered")

# --- SESSION STATE ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "caught" not in st.session_state:
    st.session_state.caught = False

if "bucketlist" not in st.session_state:
    st.session_state.bucketlist = {
        "Masai Mara 🐘": False,
        "Swiss Alps Road Trip 🚗": False,
        "Paris Trip 🗼": False,
        "Italian Summer 🍝": False,
        "Disneyland Paris 🎢": False,
    }

# --- CUSTOM CSS ---
st.markdown("""
<style>
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-60px); }
  100% { transform: translateY(0px); }
}

.center {
  text-align: center;
  font-size: 26px;
  margin-top: 40px;
}

.big-heart {
  font-size: 100px;
  text-align: center;
  animation: float 2.5s ease-in-out infinite;
}

.balloon {
  font-size: 120px;
  text-align: center;
  animation: float 3s ease-in-out infinite;
  cursor: pointer;
}

button[kind="primary"] {
  font-size: 40px !important;
  padding: 20px 40px !important;
  border-radius: 50px !important;
}
</style>
""", unsafe_allow_html=True)

# --- PAGE 1 ---
if not st.session_state.caught:
    st.markdown('<div class="center">Catch the heart❤️😉</div>', unsafe_allow_html=True)

    st.markdown('<div class="big-heart">💖</div>', unsafe_allow_html=True)

    if st.button("Catch 💖"):
        st.session_state.caught = True
        st.rerun()

# --- PAGE 2 (IMPROVED FLOATING BALLOON LOGIN) ---
elif not st.session_state.logged_in:
    st.markdown('<div class="center">You caught it! 💕 Tap the heart balloon to unlock our secret ✨</div>', unsafe_allow_html=True)

    st.markdown('<div class="balloon">🎈💖</div>', unsafe_allow_html=True)

    if st.button("Open 💕"):
        st.session_state.logged_in = True
        st.rerun()

# --- PAGE 3 ---
else:
    st.title("Our Love Bucket List 💕")
    st.write("Let\'s make memories together ✨")

    for item in st.session_state.bucketlist:
        st.session_state.bucketlist[item] = st.checkbox(
            item,
            value=st.session_state.bucketlist[item]
        )

    st.write("---")

    completed = sum(st.session_state.bucketlist.values())
    total = len(st.session_state.bucketlist)

    st.success(f"Completed: {completed}/{total} adventures 💖")

    if completed == total:
        st.balloons()
        st.success("We did it! More adventures soon ❤️")

# --- FOOTER ---
st.markdown("---")
st.caption("Made with love 💖")