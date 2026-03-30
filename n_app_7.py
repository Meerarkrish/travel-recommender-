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

# --- CSS (WORKING FLOATING HEART) ---
st.markdown("""
<style>
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-50px); }
  100% { transform: translateY(0px); }
}

.center {
  text-align: center;
  font-size: 26px;
  margin-top: 40px;
}

.floating-heart {
  font-size: 120px;
  text-align: center;
  animation: float 2.5s ease-in-out infinite;
}

/* Make button invisible but clickable */
div.stButton > button {
  background: transparent;
  border: none;
  color: transparent;
  height: 120px;
}

</style>
""", unsafe_allow_html=True)

# --- PAGE 1 ---
if not st.session_state.caught:
    st.markdown('<div class="center">Catch the heart to see what\'s inside 😉</div>', unsafe_allow_html=True)

    st.markdown('<div class="floating-heart">💖</div>', unsafe_allow_html=True)

    if st.button("catch", key="catch"):
        st.session_state.caught = True
        st.rerun()

# --- PAGE 2 ---
elif not st.session_state.logged_in:
    st.markdown('<div class="center">You caught it! 💕 Catch the heart balloon to unlock our secret ✨</div>', unsafe_allow_html=True)

    st.markdown('<div class="floating-heart">🎈💖</div>', unsafe_allow_html=True)

    if st.button("login", key="login"):
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
