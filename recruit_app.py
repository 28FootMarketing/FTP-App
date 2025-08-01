import streamlit as st

st.set_page_config(
    page_title="Facilitate The Process",
    layout="wide",
    page_icon="🏀",
)

# Sidebar: Mobile nav & links
with st.sidebar:
    st.title("🏆 Recruit Access")
    st.markdown("Quick links and tools:")

    st.markdown("- [📋 Recruiting List](https://recruit.facilitatetheprocess.com/free-recruiting-list-page)")
    st.markdown("- [🧠 Recruiting GPT](https://chat.openai.com/g/g-680164288ea88191b5579446ecf1f2fd-diy-athletic-recruiting)")
    st.markdown("- [📱 Link in Bio](https://recruit.facilitatetheprocess.com/)")

    st.markdown("---")
    st.markdown("Powered by [28 Foot Marketing](https://facilitatetheprocess.com)")

# Main app content
st.markdown(
    """
    <style>
        iframe {
            height: 95vh;
            width: 100%;
            border: none;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🚀 Facilitate The Process On-the-Go")

st.components.v1.iframe("https://recruit.facilitatetheprocess.com", height=800, scrolling=True)
