import streamlit as st
import chatGPT

page_names = [
    "the Player",
    "Creepers",
    "Biomes",
    "The Nether",
    "The End"
]

def show_wiki_page(page_json):
    st.write(page_json["name"])
    st.write("")
    st.write("HISTORY")
    st.write("   " + page_json["history"])
    st.write("")
    st.write("CHARACTERISTICS")
    st.write("   " + page_json["characteristics"])
    st.write("")
    st.write("TRIVIA")
    st.write("   " + page_json["trivia"])

# Check if 'key' already exists in session_state
# If not, then initialize it
if 'wiki' not in st.session_state:
    wiki = {}
    for page_name in page_names:
        wiki[page_name] = chatGPT.get_json_response(chatGPT.system_prompt, page_name)
    st.session_state["wiki"] = wiki

page_names.insert(0, "Select")

"""
Welcome to the Minecraft Wiki!
"""

page_selection = st.selectbox(
    "Which page would you like to read?",
    page_names
)

if page_selection != "Select":
    show_wiki_page(st.session_state["wiki"][page_selection])
