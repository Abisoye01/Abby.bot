import streamlit as st
import random

# Set page config
st.set_page_config(page_title="Abby Bot Tester", layout="wide", initial_sidebar_state="expanded")

st.title("🎮 Abby Bot - Streamlit Debug Console")
st.markdown("Test your bot commands without connecting to the real Highrise server")

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Bot Configuration")
    
    bot_token = st.text_input("Bot Token", value="eaf0508f50fe0e7f66fe5ba7b69e27fae0aa1b7c732a92ec53b03ef2b68a7a0b", type="password")
    room_id = st.text_input("Room ID", value="6813ae5a9e0a5942f1555fe7")
    test_username = st.text_input("Test Username", value="TestPlayer")
    
    st.divider()
    
    st.subheader("Moderator Access")
    is_moderator = st.checkbox("Is Moderator?", value=True)
    
    if is_moderator:
        st.success("✅ Moderator Mode Enabled")
    else:
        st.info("ℹ️ Regular User Mode")

# Main Dashboard
st.header("🧪 Command Tester")

# Create tabs for different command categories
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Emotes", 
    "Game Commands", 
    "Moderator", 
    "Teleport", 
    "Custom Test"
])

# ==================== TAB 1: EMOTES ====================
with tab1:
    st.subheader("Emote Commands")
    
    col1, col2 = st.columns(2)
    
    with col1:
        emote_buttons = ["Wrong", "Fashion", "Kiss", "Hello", "Wave", "Shy", "Hot", "Kawaii"]
        selected_emote = st.selectbox("Select Emote", emote_buttons)
        
        if st.button(f"Send /{selected_emote.lower()}", key="emote_btn"):
            st.success(f"✅ Sent: `/{selected_emote.lower()}`")
            st.code(f"await self.highrise.send_emote('emote-{selected_emote.lower()}')", language="python")
    
    with col2:
        st.info("💡 These commands trigger emote responses")
        emote_list = ["Wrong", "Fashion", "Gravity", "Icecream", "Casual", "Kiss", "No", "Sad", "Yes", "Laughing"]
        st.write(f"Available emotes: {', '.join(emote_list[:5])}...")

# ==================== TAB 2: GAME COMMANDS ====================
with tab2:
    st.subheader("Game Action Commands")
    
    col1, col2 = st.columns(2)
    
    with col1:
        game_commands = ["/fish", "/bomb", "/stab", "/shoot", "/bandage", "/play", "/marry me?"]
        selected_game_cmd = st.selectbox("Select Game Command", game_commands)
        
        if st.button(f"Execute {selected_game_cmd}", key="game_btn"):
            st.success(f"✅ Executed: `{selected_game_cmd}`")
            
            # Simulate responses
            responses = {
                "/fish": "🥈 YOU WON THE MEDAL: SILVER FISHERMAN 🥈",
                "/bomb": "💣🧟‍♂️ You Threw a Bomb on 2x Boss Zombie 💣",
                "/stab": "🧟🔪 You Stabbed 6x Zombie 🔪🧟",
                "/shoot": "🧟 You Shot 5x Zombie 🧟",
                "/bandage": "🔴 You Used the Bandage Your Life Is at: 100