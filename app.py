import streamlit as st
import random

conversation_map = {
    "feeling_off": {
        "keywords": ["feel off", "not myself", "feeling strange", "something wrong", "don't know why", "feeling weird"],
        "user_message": "I don't even know why I'm texting you. I just feel… off. Like I'm not myself anymore.",
        "bot_response": "I'm really glad you texted me. You don't need to have it all figured out to reach out. Feeling 'off' can be heavy on its own, and I'm here to listen—no judgment, just support."
    },
    "pretending": {
        "keywords": ["pretending", "fake", "exhausting", "acting", "pretend", "keep doing", "exhausted", "tired of pretending", "mask"],
        "user_message": "I've been pretending I'm okay around everyone, but it's exhausting. I don't think I can keep doing it.",
        "bot_response": "That sounds incredibly hard. Keeping everything inside and putting on a brave face can wear you down. You deserve a space to be real, and I'm proud of you for opening up to me. You're not a burden, ever."
    },
    "not_matter": {
        "keywords": ["don't matter", "not important", "disappeared", "nothing would change", "make a difference", "purpose", "point", "meaningless"],
        "user_message": "I just don't feel like I matter that much. Like if I disappeared, nothing would really change.",
        "bot_response": "It hurts to feel that way, and I want you to know you do matter. Sometimes our minds lie to us when we're overwhelmed. But your presence makes a difference, even if it's hard to see it right now. I see you. I'm with you."
    },
    "validation": {
        "keywords": ["really", "you think", "sure", "mean it", "believe that", "actually"],
        "user_message": "You really think so?",
        "bot_response": "Absolutely. The world isn't the same without you in it. Your thoughts, your energy, your story—everything about you is uniquely valuable. It's okay to struggle. It doesn't make you any less worthy of love or support."
    },
    "numb": {
        "keywords": ["numb", "hard to believe", "don't feel", "can't feel", "empty", "hollow", "void", "emotionless", "nothing"],
        "user_message": "It's just hard to believe that when I feel so numb all the time.",
        "bot_response": "Numbness can feel scary and confusing, like being stuck in a fog. But it's also your brain's way of protecting you when you've been through too much. That doesn't mean you're broken—it means you've been trying to survive. And that takes strength."
    },
    "tired": {
        "keywords": ["tired", "not strong", "weak", "exhausted", "drained", "no energy", "fatigue", "worn out"],
        "user_message": "I don't feel strong. I feel tired. Like all the time.",
        "bot_response": "Being tired after carrying so much makes perfect sense. Strength isn't about pushing through without feeling—it's about surviving the weight, and you've done that every day. I'm here to help share some of that weight, even just a little."
    },
    "gratitude": {
        "keywords": ["thanks", "thank you", "appreciate", "helped", "grateful", "not judging", "understanding", "listening"],
        "user_message": "Thanks for not judging me. I thought I'd sound weak.",
        "bot_response": "Not even a little. What you've shared takes courage. You're showing up, being real, and facing your feelings—that's strength. And I'm honored to be here with you through it."
    },
    "greeting": {
        "keywords": ["hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening"],
        "user_message": "Hello",
        "bot_response": "Hello. How are you feeling today? You can share anything that's on your mind."
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "talk later", "leaving", "going away"],
        "user_message": "Goodbye",
        "bot_response": "Take care of yourself. Remember, I'm here whenever you need to talk. Be gentle with yourself."
    }
}

# Helper function to get responses
def get_response(user_input):
    for key, value in conversation_map.items():
        if any(keyword in user_input.lower() for keyword in value["keywords"]):
            return value["bot_response"]
    return "I'm here to listen. Could you tell me more about what's on your mind?"

# Custom CSS for a warmer, more comforting interface
def apply_custom_css():
    st.markdown("""
    <style>
    .stApp {
        background-color: #f9f3ea;
    }
    .main {
        background-color: #f9f3ea;
        border-radius: 15px;
        padding: 20px;
    }
    .stTextInput > div > div > input {
        background-color: #fff8ee;
        border-radius: 10px;
        border: 1px solid #e0d5c4;
        padding: 10px 15px;
    }
    .stButton > button {
        background-color: #7aa6c2;
        color: white;
        border-radius: 20px;
        padding: 5px 20px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #6295b5;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .user-message {
        background-color: #e1f0f9;
        padding: 12px 18px;
        border-radius: 15px 15px 3px 15px;
        margin: 5px 0;
        display: inline-block;
        max-width: 80%;
    }
    .bot-message {
        background-color: #f5e9d9;
        padding: 12px 18px;
        border-radius: 15px 15px 15px 3px;
        margin: 5px 0;
        display: inline-block;
        max-width: 80%;
        border-left: 3px solid #d4a373;
    }
    h1 {
        color: #5e8ca7;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stMarkdown {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# Supportive quotes to display at random
supportive_quotes = [
    "Take a deep breath. You're doing better than you think.",
    "Your feelings are valid, and you deserve kindness—especially from yourself.",
    "Small steps are still progress. I'm proud of you for being here.",
    "It's okay to not be okay sometimes. You're human, and that's beautiful.",
    "You matter. Your story matters. And these difficult feelings won't last forever.",
    "Sharing how you feel is an act of courage. I'm here with you.",
]

# Streamlit UI with warmer design
st.set_page_config(page_title="Sthira", page_icon="💙", layout="centered")
apply_custom_css()

st.title("💙 Sthira : Your Best Friend")
st.markdown("""
<div style="padding:15px; background-color:#f0e6d6; border-radius:10px; margin-bottom:20px; border-left:4px solid #d4a373;">
Welcome to your safe space. Whatever you're feeling right now is okay. 
I'm here to listen without judgment and offer support when you need it.
</div>
""", unsafe_allow_html=True)

# Display a random supportive quote
st.markdown(f"""
<div style="text-align:center; font-style:italic; color:#5e8ca7; padding:10px; margin:15px 0;">
{random.choice(supportive_quotes)}
</div>
""", unsafe_allow_html=True)

# Chat interface
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Create a container for chat messages with scrolling
chat_container = st.container()

# Input form at the bottom
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Share what's on your mind...", placeholder="Type here... I'm listening")
    cols = st.columns([4, 1])
    with cols[1]:
        submitted = st.form_submit_button("Send 💙")

if submitted and user_input:
    # Append user message
    st.session_state["messages"].append({"user": user_input})
    # Get bot response
    bot_response = get_response(user_input)
    st.session_state["messages"].append({"bot": bot_response})

# Display chat messages in the container with custom styling
with chat_container:
    for message in st.session_state["messages"]:
        if "user" in message:
            st.markdown(f"""
            <div style="text-align: right;">
                <div class="user-message">
                    <strong>You:</strong> {message['user']}
                </div>
            </div>
            """, unsafe_allow_html=True)
        elif "bot" in message:
            st.markdown(f"""
            <div style="text-align: left;">
                <div class="bot-message">
                    {message['bot']}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Add breathing space at the bottom of chat
    st.markdown("<div style='height: 100px'></div>", unsafe_allow_html=True)

# Add footer with self-care reminders
st.markdown("""
<div style="text-align:center; padding:15px; color:#888; font-size:0.9em; margin-top:20px;">
    Remember to take care of yourself today. Drink some water, take a few deep breaths, and be gentle with yourself.
</div>
""", unsafe_allow_html=True)