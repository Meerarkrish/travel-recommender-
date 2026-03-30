import streamlit as st

def main():
    st.set_page_config(page_title="2026 Travel Planner", page_icon="✈️")
    st.title("🌍 Boutique Travel Planner")
    st.subheader("Find your next bucket-list destination")

    destinations = [
        {"name": "Masai Mara, Kenya", "type": "Adventure", "vibe": "Wildlife & Savanna"},
        {"name": "Disneyland Paris", "type": "Magic", "vibe": "Themed Luxury & Family"},
        {"name": "Swiss Alps Road Trip", "type": "Scenery", "vibe": "Mountain Peaks & Driving"},
        {"name": "Rovaniemi, Lapland", "type": "Magic", "vibe": "Arctic Winter & Northern Lights"},
        {"name": "Sossusvlei, Namibia", "type": "Adventure", "vibe": "Desert Dunes & Solitude"},
        {"name": "Wild Atlantic Way, Ireland", "type": "Scenery", "vibe": "Coastal Cliffs & Castles"},
        {"name": "Tokyo DisneySea", "type": "Magic", "vibe": "Immersive Nautical Fantasy"}
    ]

    choice = st.selectbox(
        "What is your primary goal for this trip?",
        ["Adventure", "Magic", "Scenery"]
    )

    if choice:
        st.divider()
        st.write(f"### Top Recommendations for {choice}:")
        matches = [d for d in destinations if d["type"] == choice]
        
        for match in matches:
            with st.expander(f"📍 {match['name']}"):
                st.write(f"**Vibe:** {match['vibe']}")

if __name__ == "__main__":
    main()