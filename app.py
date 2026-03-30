import streamlit as st

def main():
    st.set_page_config(page_title="2026 Travel Planner", page_icon="💖")
    
    # Title and Intro
    st.title("🌍 Boutique Travel Planner")
    st.subheader("Find your next bucket-list destination")

    # The Interactive "Catch the Heart" Section
    st.markdown("---")
    st.write("### ✨ Feeling Lucky?")
    if st.button("❤️ Catch the Heart!"):
        st.balloons()  # This creates the floating effect
        st.success("You caught it! May your 2026 travels be full of love! ✈️")
    st.markdown("---")

    destinations = [
        {"name": "Masai Mara, Kenya", "type": "Adventure", "vibe": "Wildlife & Savanna", "url": "https://www.maasaimara.com/"},
        {"name": "Disneyland Paris", "type": "Magic", "vibe": "Themed Luxury & Family", "url": "https://www.disneylandparis.com/"},
        {"name": "Swiss Alps Road Trip", "type": "Scenery", "vibe": "Mountain Peaks & Driving", "url": "https://www.myswitzerland.com/"},
        {"name": "Rovaniemi, Lapland", "type": "Magic", "vibe": "Arctic Winter & Northern Lights", "url": "https://www.visitrovaniemi.fi/"},
        {"name": "Sossusvlei, Namibia", "type": "Adventure", "vibe": "Desert Dunes & Solitude", "url": "https://www.namibianamibia.com/"},
        {"name": "Wild Atlantic Way, Ireland", "type": "Scenery", "vibe": "Coastal Cliffs & Castles", "url": "https://www.thewildatlanticway.com/"}
    ]

    choice = st.selectbox(
        "Where should we go?",
        ["Adventure", "Magic", "Scenery"]
    )

    if choice:
        st.write(f"### Top Recommendations for {choice}:")
        matches = [d for d in destinations if d["type"] == choice]
        
        for match in matches:
            with st.expander(f"📍 {match['name']}"):
                st.write(f"**Vibe:** {match['vibe']}")
                # The clickable link button
                st.link_button(f"Explore {match['name']}", match['url'])

if __name__ == "__main__":
    main()