import streamlit as st

def main():
    # 1. Wide Layout & Page Config
    st.set_page_config(page_title="2026 Elite Travels", page_icon="💖", layout="wide")
    
    # 2. 💖 THE FLOATING HEART & WINK ANIMATION 💖
    # We use custom CSS and HTML for actual drifting movement
    # that Streamlit cannot do on its own.
    st.markdown("""
        <style>
        /* This is the container for the floating effect */
        .heart-float {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1000;
        }

        /* This defines a single heart element */
        .heart {
            position: absolute;
            bottom: -50px;
            font-size: 30px;
            opacity: 0.8;
            animation: floatHeart 6s ease-in-out infinite;
        }

        /* The Animation itself: Up and Fade */
        @keyframes floatHeart {
            0% {
                transform: translateY(0) translateX(0);
                opacity: 1;
            }
            100% {
                transform: translateY(-110vh) translateX(20px);
                opacity: 0;
            }
        }

        /* Styling for the new Catch the Heart button with the Wink */
        .wink-button {
            display: inline-block;
            padding: 10px 20px;
            font-size: 24px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            outline: none;
            color: white;
            background-color: #FF4B4B;
            border: none;
            border-radius: 20px;
            box-shadow: 0 5px #999;
            transition: 0.3s;
        }
        .wink-button:active {
            background-color: #f7a5a5;
            box-shadow: 0 2px #666;
            transform: translateY(4px);
        }
        </style>

        <div class="heart-float">
            <div class="heart" style="left: 10%; animation-delay: 0s;">💖 😉</div>
            <div class="heart" style="left: 30%; animation-delay: 1.5s;">💖 😜</div>
            <div class="heart" style="left: 50%; animation-delay: 0.5s;">💖 🥰</div>
            <div class="heart" style="left: 70%; animation-delay: 2s;">💖 😉</div>
            <div class="heart" style="left: 90%; animation-delay: 1s;">💖 😜</div>
        </div>
        """, unsafe_allow_html=True)

    # 3. App Header
    st.title("🏙️ 2026 Elite Travel Curator")
    st.markdown("---")

    # 4. Interactive Sidebar
    with st.sidebar:
        st.header("What’s Your Vibe?")
        choice = st.radio("", ["Adventure", "Magic", "Scenery"])
        st.write("---")
        
        # This button triggers Streamlit's built-in extra balloons as a "Catch"
        if st.button("❤️ CATCH THE HEART 😉", key="wink_btn"):
            st.balloons()
            st.toast("Heart Caught! May your 2026 be full of adventure! 🥂", icon="😍")

    # 5. Destination Gallery (Images + Direct Links)
    data = {
        "Adventure": [
            {"name": "Masai Mara Safari", "img": "https://images.unsplash.com/photo-1516422213484-214249580c74?w=800", "url": "https://www.maasaimara.com/"},
            {"name": "Sossusvlei Dunes", "img": "https://images.unsplash.com/photo-150531053ea66-64673c683b5f?w=800", "url": "https://www.namibianamibia.com/"}
        ],
        "Magic": [
            {"name": "Disneyland Paris", "img": "https://images.unsplash.com/photo-1603566133036-963d763a0333?w=800", "url": "https://www.disneylandparis.com/"},
            {"name": "Arctic Lapland", "img": "https://images.unsplash.com/photo-1517154596047-466865d49510?w=800", "url": "https://www.visitrovaniemi.fi/"}
        ],
        "Scenery": [
            {"name": "Swiss Alps Drive", "img": "https://images.unsplash.com/photo-1531310197839-ccf54634509e?w=800", "url": "https://www.myswitzerland.com/"},
            {"name": "Wild Atlantic Way", "img": "https://images.unsplash.com/photo-1505672678657-cc7037095e60?w=800", "url": "https://www.thewildatlanticway.com/"}
        ]
    }

    # Display results as visual cards
    st.subheader(f"Results for: {choice}")
    
    # Grid Layout
    cols = st.columns(2)
    matches = data[choice]

    for i, match in enumerate(matches):
        with cols[i % 2]:
            st.image(match['img'], use_container_width=True, caption=match['name'])
            st.markdown(f"### 📍 {match['name']}")
            # Direct link button that is wide and clear
            st.link_button(f"Book {match['name']} Now →", match['url'], use_container_width=True)
            st.write(" ") # Spacer

    # 6. Footer
    st.markdown("---")
    st.caption("© 2026 Boutique Travel Agency | Curated for Elite Travelers")

if __name__ == "__main__":
    main()