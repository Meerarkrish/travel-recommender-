import streamlit as st

def main():
    # 1. Page Config for a clean look
    st.set_page_config(page_title="A Surprise for You 💖", page_icon="🎈", layout="centered")

    # 2. Initialize the "Locked" state
    if 'unlocked' not in st.session_state:
        st.session_state.unlocked = False

    # 3. Custom CSS for the Background and Floating Heart Animation
    st.markdown("""
        <style>
        /* The entire page is now a soft pastel pink */
        .main {
            background-color: #ffe0e9; /* Pastel Pink */
        }
        
        /* Animation: Makes the heart drift up and down smoothly */
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-30px); }
            100% { transform: translateY(0px); }
        }
        
        /* The Container and Style for the Floating Heart */
        .balloon-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 70vh; /* Centers the heart vertically */
            cursor: pointer; /* Changes the cursor to a hand on hover */
        }
        .heart-balloon {
            font-size: 150px; /* Big, impactful heart */
            animation: float 4s ease-in-out infinite; /* Apply the float animation */
            filter: drop-shadow(0 15px 20px rgba(255,0,0,0.4)); /* Soft shadow for depth */
            transition: transform 0.3s;
        }
        .heart-balloon:hover {
            transform: scale(1.1) rotate(5deg); /* Grows and rotates on hover */
        }

        /* Styling for the text that appears *above* the heart */
        .catch-text {
            font-family: 'Comic Sans MS', 'Courier New', sans-serif; /* Playful font */
            font-size: 36px;
            color: #FF4B4B;
            margin-bottom: -50px; /* Pulls the heart up slightly toward the text */
            font-weight: bold;
        }
        
        /* --- Styles for Screen 2 (The Reveal) --- */
        .love-message {
            font-family: 'Helvetica Neue', sans-serif;
            font-size: 60px;
            color: white;
            background-color: #FF4B4B;
            padding: 20px;
            border-radius: 20px;
            text-align: center;
            margin-top: 50px;
            font-weight: bold;
        }
        .blush-message {
            font-family: 'Courier New', sans-serif;
            font-size: 24px;
            color: #FF4B4B;
            text-align: center;
            margin-top: 30px;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- SCREEN 1: THE LOCK (Floating Balloon Only) ---
    if not st.session_state.unlocked:
        # We start by displaying the playful instruction
        st.markdown('<div class="balloon-container"><div class="catch-text">catch the heart</div><div class="heart-balloon">❤️</div></div>', unsafe_allow_html=True)
        
        # When he clicks *anywhere* in the container, the button is triggered
        if st.button("❤️ CATCH IT! 😉", use_container_width=True):
            st.session_state.unlocked = True
            st.balloons() # Immediate celebration
            st.rerun() # Refresh the page to show Screen 2

    # --- SCREEN 2: THE REVELATION (The Surprise) ---
    else:
        # Celebratory balloons continue to fly
        st.balloons() 
        
        # The main 'I love you!' message
        st.markdown('<div class="love-message">I love you!</div>', unsafe_allow_html=True)
        
        # The playful follow-up text and emoji
        st.markdown('<div class="blush-message">I know you are blushing and smiling 😊</div>', unsafe_allow_html=True)
        
        # Add a playful spacer
        st.write("")
        st.write("")

        if st.button("Go back to start"):
            st.session_state.unlocked = False
            st.rerun()

if __name__ == "__main__":
    main()