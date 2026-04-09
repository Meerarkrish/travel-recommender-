import streamlit as st

def main():
    st.set_page_config(page_title="A Surprise for You 💖", page_icon="❤️", layout="centered")

    if 'unlocked' not in st.session_state:
        st.session_state.unlocked = False

    # --- THE MAGIC CSS ---
    st.markdown("""
        <style>
        /* Pastel Pink Background */
        .stApp {
            background-color: #ffe0e9;
        }
        
        /* The Floating Animation */
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-40px); }
            100% { transform: translateY(0px); }
        }

        /* Container that handles the floating for EVERYTHING inside it */
        .floating-container {
            animation: float 3s ease-in-out infinite;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
            height: 300px;
            margin-top: 50px;
        }

        /* The Visual Heart */
        .heart-visual {
            font-size: 150px;
            z-index: 1;
            pointer-events: none; /* Let clicks pass through to the button */
        }

        /* Make the Streamlit Button Invisible but perfectly centered over the heart */
        div.stButton > button {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 180px;
            height: 180px;
            background-color: transparent !important;
            color: transparent !important;
            border: none !important;
            box-shadow: none !important;
            z-index: 10;
            cursor: pointer;
        }
        
        /* Remove hover effects that reveal the button */
        div.stButton > button:hover, div.stButton > button:active {
            background-color: transparent !important;
            color: transparent !important;
            border: none !important;
        }

        .instruction-text {
            text-align: center;
            font-family: 'Comic Sans MS', cursive;
            font-size: 32px;
            color: #FF4B4B;
            margin-top: 60px;
        }

        /* Revelation Style */
        .love-box {
            background-color: #FF4B4B;
            color: white;
            padding: 50px;
            border-radius: 40px;
            text-align: center;
            font-size: 70px;
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
        
        # This div wraps both the heart and the button so they float together
        st.markdown('<div class="floating-container">', unsafe_allow_html=True)
        
        # Center the heart visually
        st.markdown('<div class="heart-visual">❤️</div>', unsafe_allow_html=True)
        
        # The button is now physically placed right here in the floating div
        if st.button(" ", key="heart_click"):
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