import streamlit as st
import random

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

# --- CUSTOM CSS FOR FLOATING HEART ---
st.markdown("""
<style>
@keyframes float {
  0% {transform: translateY(0px);} 
  50% {transform: translateY(-40px);} 
  100% {transform: translateY(0px);} 
}

.heart {
  font-size: 80px;
  text-align: center;
  cursor: pointer;
  animation: float 2s ease-in-out infinite;
}

.center {
  text-align: center;
  font-size: 24px;
}
</style>
""", unsafe_allow_html=True)

# --- PAGE 1: CATCH THE HEART ---
if not st.session_state.caught:
    st.markdown('<div class="center">Catch the heart to see what\'s inside 😉</div>', unsafe_allow_html=True)

    if st.button("💖", key="heart_button"):
        st.session_state.caught = True
        st.rerun()

# --- PAGE 2: LOGIN ---
elif not st.session_state.logged_in:
    st.markdown('<div class="center">You caught it! 💕 Click again to unlock our secret ✨</div>', unsafe_allow_html=True)

    if st.button("🎈💖", key="login_heart"):
        st.session_state.logged_in = True
        st.rerun()

# --- PAGE 3: BUCKET LIST ---
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