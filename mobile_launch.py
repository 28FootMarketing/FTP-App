import streamlit as st

st.set_page_config(page_title="Facilitate The Process", page_icon="🏀", layout="centered")

# --- Branding Header ---
st.markdown("""
<div style='position:sticky;top:0;background-color:#ffffff;padding:10px 0;text-align:center;border-bottom:1px solid #ddd;z-index:999;'>
    <img src='https://recruit.facilitatetheprocess.com/favicon.png' width='40'/>
    <span style='font-size:20px;font-weight:bold;margin-left:10px;'>Facilitate The Process</span><br>
    <small>Recruiting Tools. Fast Access. On the Go.</small>
</div>
""", unsafe_allow_html=True)

st.markdown("## 📋 Choose a Recruiting Tool")

# --- Searchable Dropdown ---
option = st.selectbox("What do you want to access?", [
    "🎯 Starter Package",
    "📋 Recruiting List",
    "👨‍👩‍👧 Parent GPT",
    "✉️ Coach Message GPT",
    "📊 Level Finder GPT",
    "📞 Contact Us"
])

# --- Link Mapping ---
link_map = {
    "🎯 Starter Package": "https://recruit.facilitatetheprocess.com/",
    "📋 Recruiting List": "https://recruit.facilitatetheprocess.com/free-recruiting-list-page",
    "👨‍👩‍👧 Parent GPT": "https://chat.openai.com/g/g-680164288ea88191b5579446ecf1f2fd-diy-athletic-recruiting",
    "✉️ Coach Message GPT": "https://chat.openai.com/gpt-name",
    "📊 Level Finder GPT": "https://chat.openai.com/gpt-name",
    "📞 Contact Us": "mailto:anthony@facilitatetheprocess.com"
}

if st.button("🚀 Launch Tool"):
    st.markdown(f"[Click here to open {option}]({link_map[option]})", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center;'>📲 Powered by <a href='https://28footmarketing.com' target='_blank'>28 Foot Marketing</a></p>", unsafe_allow_html=True)

# --- Floating CTA Button ---
st.markdown("""
<style>
    .floating-button {
        position: fixed;
        bottom: 25px;
        right: 25px;
        background-color: #4CAF50;
        color: white;
        border-radius: 50%;
        padding: 16px;
        font-size: 20px;
        text-align: center;
        z-index: 1000;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
</style>
<a href="mailto:anthony@facilitatetheprocess.com" class="floating-button">📩</a>
""", unsafe_allow_html=True)
