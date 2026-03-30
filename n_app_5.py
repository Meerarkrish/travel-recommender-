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

/* ONLY TARGET BIG BUTTON */
.big-button button {
  font-size: 110px !important;
  background: none !important;
  border: none !important;
  cursor: pointer;
  animation: float 3s ease-in-out infinite;
}

.small-button button {
  font-size: 70px !important;
  background: none !important;
  border: none !important;
}

</style>
""", unsafe_allow_html=True)

# --- PAGE 1 ---
if not st.session_state.caught:
    st.markdown('<div class="center">Catch the heart to see what\'s inside 😉</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<div class="small-button">', unsafe_allow_html=True)
        if st.button("💖", key="catch"):
            st.session_state.caught = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- PAGE 2 (FIXED CLICKABLE FLOATING BALLOON) ---
elif not st.session_state.logged_in:
    st.markdown('<div class="center">You caught it! 💕 Tap the heart balloon to unlock our secret ✨</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('<div class="big-button">', unsafe_allow_html=True)
        if st.button("🎈💖", key="login"):
            st.session_state.logged_in = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

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
