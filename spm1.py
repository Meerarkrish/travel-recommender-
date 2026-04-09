import streamlit as st

def main():
    st.set_page_config(page_title="A Surprise for You 💖", page_icon="❤️", layout="centered")

    if 'unlocked' not in st.session_state:
        st.session_state.unlocked = False

    # --- THE FINAL FIX CSS ---
    st.markdown("""
        <style>
        /* Pastel Pink Background */
        .stApp {
            background-color: #ffe0e9;
        }
        
        /* The Animation */
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-40px); }
            100% { transform: translateY(0px); }
        }

        /* This is the magic wrapper that forces the button to float */
        .floating-wrapper {
            animation: float 3s ease-in-out infinite;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 300px;
            margin-top: 20px;
        }

        /* Target the button inside the floating wrapper */
        .floating-wrapper div.stButton > button {
            background-color: transparent !important;
            border: none !important;
            font-size: 150px !important;
            height: 200px !important;
            width: 200px !important;
            color: red !important;
            cursor: pointer;
            box-shadow: none !important;
            transition: transform 0.2s;
        }

        /* Keep it looking like a heart on hover */
        .floating-wrapper div.stButton > button:hover, 
        .floating-wrapper div.stButton > button:active,
        .floating-wrapper div.stButton > button:focus {
            background-color: transparent !important;
            color: red !important;
            border: none !important;
            box-shadow: none !important;
            transform: scale(1.1);
        }

        .instruction-text {
            text-align: center;
            font-family: 'Comic Sans MS', cursive;
            font-size: 32px;
            color: #FF4B4B;
            margin-top: 60px;
        }

        /* Screen 2 - The Message */
        .love-box {
            background-color: #FF4B4B;
            color: white;
            padding: 50px;
            border-radius: 40px;
            text-align: center;
            font-size: 60px;
            font-weight: bold;
            margin-top: 100px;
        }
        .blush-text {
            color: #FF4B4B;
            text-align: center;
            font-size: 28px;
            margin-top: 30px;
            font-family: 'Helvetica Neue', sans-serif;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- SCREEN 1: THE FLOATING HEART ---
    if not st.session_state.unlocked:
        st.markdown('<div class="instruction-text">catch the heart to see what\'s inside 😉</div>', unsafe_allow_html=True)
        
        # We wrap the button in our animated 'floating-wrapper'
        st.markdown('<div class="floating-wrapper">', unsafe_allow_html=True)
        if st.button("❤️", key="heart_trigger_final"):
            st.session_state.unlocked = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # --- SCREEN 2: THE REVELATION ---
    else:
        st.balloons()
        st.markdown('<div class="love-box">I love you!</div>', unsafe_allow_html=True)
        st.markdown('<div class="blush-text">I know you are blushing and smiling 😊</div>', unsafe_allow_html=True)
        
        st.write("")
        if st.button("Restart Surprise"):
            st.session_state.unlocked = False
            st.rerun()

if __name__ == "__main__":
    main()