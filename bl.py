import streamlit as st

# --- Page config ---
st.set_page_config(page_title="Catch the Heart 💖", page_icon="💖", layout="centered")

# --- Session state ---
if "caught" not in st.session_state:
    st.session_state.caught = False
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "bucketlist" not in st.session_state:
    st.session_state.bucketlist = {
        "Masai Mara 🐘": False,
        "Swiss Alps Road Trip 🚗": False,
        "Paris Trip 🗼": False,
        "Italian Summer 🍝": False,
        "Disneyland Paris 🎢": False,
    }

# --- Custom CSS for floating heart ---
st.markdown("""
<style>
@keyframes float {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-30px); }
  100% { transform: translateY(0px); }
}

.center {
  text-align: center;
  margin-top: 50px;
  font-size: 28px;
  color: white;
}

.floating-heart {
  font-size: 100px;
  animation: float 2s ease-in-out infinite;
  cursor: pointer;
}
body {
  background: linear-gradient(to right, #ff9a9e, #fad0c4);
}
</style>
""", unsafe_allow_html=True)

# --- Page 1: Catch the heart ---
if not st.session_state.caught:
    st.markdown('<div class="center">Catch the heart to see what\'s inside 😉</div>', unsafe_allow_html=True)
    if st.button("💖", key="catch"):
        st.session_state.caught = True
        st.experimental_rerun()

# --- Page 2: Floating heart login ---
elif not st.session_state.logged_in:
    st.markdown('<div class="center">You caught it! 💕 Click the floating heart to unlock our secret ✨</div>', unsafe_allow_html=True)
    if st.button("💖", key="login"):
        st.session_state.logged_in = True
        st.experimental_rerun()

    # Background music using HTML audio tag
    st.markdown("""
    <audio autoplay loop>
      <source src="https://www.bensound.com/bensound-music/bensound-romantic.mp3" type="audio/mpeg">
    </audio>
    """, unsafe_allow_html=True)

# --- Page 3: Bucket list ---
else:
    st.title("Our Love Bucket List 💕")
    st.write("Let's make memories together ✨")
    
    for item in st.session_state.bucketlist:
        st.session_state.bucketlist[item] = st.checkbox(item, value=st.session_state.bucketlist[item])
    
    completed = sum(st.session_state.bucketlist.values())
    total = len(st.session_state.bucketlist)
    st.success(f"Completed: {completed}/{total} adventures 💖")
    
    # Surprise ending
    if completed == total:
        st.balloons()
        st.success("❤️ I love you forever! ❤️")