import streamlit as st

def main():
    st.set_page_config(page_title="A Surprise for You 💖", page_icon="❤️", layout="centered")

    if 'unlocked' not in st.session_state:
        st.session_state.unlocked = False

    # --- LUXURY STYLING ---
    st.markdown("""
        <style>
        /* Pastel Pink Background */
        .stApp {
            background-color: #ffe0e9;
        }
        
        /* Floating Heart Animation */
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-30px); }
            100% { transform: translateY(0px); }
        }

        /* Instructions Text */
        .instruction-text {
            text-align: center;
            font-family: 'Comic Sans MS', cursive;
            font-size: 32px;
            color: #FF4B4B;
            margin-bottom: 20px;
            margin-top: 50px;
        }

        /* This makes the Streamlit button invisible but covers the heart */
        div.stButton > button {
            background-color: transparent;
            color: transparent;
            border: none;
            height: 300px;
            width: 300px;
            position: absolute;
            z-index: 10;
            cursor: pointer;
        }
        
        div.stButton > button:hover {
            border: none;
            color: transparent;
            background-color: transparent;
        }

        /* The Animated Heart Visual */
        .heart-visual {
            font-size: 150px;
            animation: float 3s ease-in-out infinite;
            text-align: center;
            display: block;
            margin-top: -50px;
        }

        /* The Revelation Styles */
        .love-box {
            background-color: #FF4B4B;
            color: white;
            padding: 40px;
            border-radius: 30px;
            text-align: center;
            font-size: 60px;
            font-weight: bold;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        .blush-text {
            color: #FF4B4B;
            text-align: center;
            font-size: 26px;
            margin-top: 20px;
            font-family: 'Helvetica Neue', sans-serif;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- SCREEN 1: THE FLOATING HEART ---
    if not st.session_state.unlocked:
        st.markdown('<div class="instruction-text">catch the heart to see what\'s inside 😉</div>', unsafe_allow_html=True)
        
        # This layout centers the "Invisible Button" over the "Floating Heart"
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            # The heart is displayed here
            st.markdown('<div class="heart-visual">❤️</div>', unsafe_allow_html=True)
            # The button is placed exactly on top of the heart but is invisible
            if st.button(" ", key="heart_trigger"):
                st.session_state.unlocked = True
                st.rerun()

    # --- SCREEN 2: THE MESSAGE ---
    else:
        st.balloons()
        st.write("") # Spacer
        st.markdown('<div class="love-box">I love you!</div>', unsafe_allow_html=True)
        st.markdown('<div class="blush-text">I know you are blushing and smiling 😊</div>', unsafe_allow_html=True)
        
        st.write("")
        if st.button("Back to start"):
            st.session_state.unlocked = False
            st.rerun()

if __name__ == "__main__":
    main()