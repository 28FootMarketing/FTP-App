import streamlit as st

st.set_page_config(
    page_title="Facilitate The Process",
    page_icon="🏀",
    layout="centered"
)

st.markdown("<h2 style='text-align: center;'>🏀 Facilitate The Process</h2>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: gray;'>Recruiting Tools & Support – On the Go</h5>", unsafe_allow_html=True)

st.markdown("---")

# Spaced Buttons for Mobile
st.markdown("### 📋 Recruiting Tools")

col1, col2 = st.columns(2)

with col1:
    st.link_button("Starter Package", "https://recruit.facilitatetheprocess.com/", use_container_width=True)
    st.link_button("Recruiting List", "https://recruit.facilitatetheprocess.com/free-recruiting-list-page", use_container_width=True)

with col2:
    st.link_button("Parent GPT", "https://chat.openai.com/g/g-680164288ea88191b5579446ecf1f2fd-diy-athletic-recruiting", use_container_width=True)
    st.link_button("📬 Contact Us", "mailto:anthony@facilitatetheprocess.com", use_container_width=True)

st.markdown("---")

st.markdown("### 🧠 GPT Tools")

st.link_button("Coach Message GPT", "https://chat.openai.com/g/gpt-name", use_container_width=True)
st.link_button("Level Finder GPT", "https://chat.openai.com/gpt-name", use_container_width=True)
st.link_button("Recruit Readiness GPT", "https://chat.openai.com/gpt-name", use_container_width=True)

st.markdown("---")

st.markdown("<p style='text-align: center;'>📲 Powered by <a href='https://28footmarketing.com' target='_blank'>28 Foot Marketing</a></p>", unsafe_allow_html=True)
