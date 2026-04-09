import streamlit as st

def main():
    st.set_page_config(page_title="A Surprise for You 💖", page_icon="❤️", layout="centered")

    if 'unlocked' not in st.session_state:
        st.session_state.unlocked = False

    # --- THE "FORCE FLOAT" CSS ---
    st.markdown("""
        <style>
        /* 1. Background */
        .stApp {
            background-color: #ffe0e9 !important;
        }
        
        /* 2. The Animation */
        @keyframes heartFloat {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-40px); }
            100% { transform: translateY(0px); }
        }

        /* 3. Force the Button to BE the Heart */
        /* This targets the specific button and ignores Streamlit's shrinking rules */
        button[kind="secondary"] {
            background-color: transparent !important;
            border: none !important;
            box-shadow: none !important;
            font-size: 160px !important; /* Huge Size */
            color: #FF0000 !important;   /* Bright Red */
            height: 300px !important;
            width: 100% !important;
            display: block !important;
            animation: heartFloat 3s ease-in-out infinite !important;
            cursor: pointer !important;
            padding: 0 !important;
        }

        /* Prevent hover 'grey out' */
        button[kind="secondary"]:hover, button[kind="secondary"]:active, button[kind="secondary"]:focus {
            background-color: transparent !important;
            color: #FF0000 !important;
            border: none !important;
            box-shadow: none !important;
        }

        /* 4. Text Styles */
        .instruction-text {
            text-align: center;
            font-family: 'Comic Sans MS', cursive, sans-serif;
            font-size: 32px;
            color: #FF4B4B;
            margin-top: 60px;
            margin-bottom: 40px;
        }

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
            font-size: 26px;
            margin-top: 30px;
            font-family: 'Helvetica Neue', sans-serif;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- SCREEN 1: THE FLOATING HEART ---
    if not st.session_state.unlocked:
        st.markdown('<div class="instruction-text">catch the heart to see what\'s inside 😉</div>', unsafe_allow_html=True)
        
        # We use a standard button, but the CSS above 'kind="secondary"' transforms it
        if st.button("❤️", key="the_big_heart"):
            st.session_state.unlocked = True
            st.rerun()

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