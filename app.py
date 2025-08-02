import streamlit as st

st.set_page_config(page_title="Trial App", layout="centered")

st.title("🚀 Trial App: Facilitate The Process")
st.markdown("Welcome to your trial app running on Hostinger VPS!")

st.markdown("### ✅ Quick Links")
st.link_button("Go to Recruit Platform", "https://recruit.facilitatetheprocess.com", use_container_width=True)
st.link_button("Visit 28 Foot Marketing", "https://28footmarketing.com", use_container_width=True)

st.markdown("---")
st.success("If you're seeing this, your VPS Streamlit setup is working!")
