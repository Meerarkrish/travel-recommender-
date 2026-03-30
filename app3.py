import streamlit as st

def main():
    # 1. Wide Layout & Page Config
    st.set_page_config(page_title="2026 Elite Travels", page_icon="✈️", layout="wide")
    
    # Custom CSS for a "Dark Mode Luxury" look
    st.markdown("""
        <style>
        .main {
            background-color: #0e1117;
        }
        .stButton>button {
            width: 100%;
            border-radius: 20px;
            height: 3em;
            background-color: #FF4B4B;
            color: white;
        }
        </style>
        """, unsafe_allow_stdio=True)

    # 2. Hero Header
    st.title("🏙️ 2026 Elite Travel Curator")
    st.markdown("---")

    # 3. Sidebar for Navigation
    with st.sidebar:
        st.header("Select Your Mood")
        choice = st.radio("", ["Adventure", "Magic", "Scenery"])
        st.write("---")
        if st.button("❤️ CATCH THE HEART"):
            st.balloons()
            st.toast("Heart Caught! 💖", icon="😍")

    # 4. Destination Database with Premium Images
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

    # 5. Displaying Content in Cards (Columns)
    st.subheader(f"Results for: {choice}")
    
    cols = st.columns(2)
    matches = data[choice]

    for i, match in enumerate(matches):
        with cols[i % 2]:
            st.image(match['img'], use_container_width=True, caption=match['name'])
            st.markdown(f"### {match['name']}")
            st.link_button(f"Book {match['name']} Now →", match['url'], use_container_width=True)
            st.write(" ") # Spacer

    # 6. Interactive Footer
    st.markdown("---")
    st.caption("© 2026 Boutique Travel Agency | Curated for Elite Travelers")

if __name__ == "__main__":
    main()