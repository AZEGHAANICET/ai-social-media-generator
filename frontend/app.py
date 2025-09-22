import streamlit as st
import requests


API_URL = "http://backend:8000"

st.title("AI Social Media Content Generator")

platform = st.selectbox("Platform", ["Instagram", "Twitter", "Facebook", "LinkedIn"])
tone = st.selectbox("Tone", ["Professional", "Casual", "Funny", "Inspirational"])
content_type = st.selectbox("Content Type", ["Caption", "Hashtag", "Post Idea"])
prompt = st.text_area("Prompt", placeholder="What is your post about?")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating..."):
            try:
                response = requests.post(
                    f"{API_URL}/generate/",
                    json={
                        "platform": platform,
                        "tone": tone.lower(),
                        "content_type": content_type.lower(),
                        "prompt": prompt
                    }
                )
                if response.status_code == 200:
                    content = response.json()
                    st.success("Generated successfully!")
                    st.write(content["generated_text"])
                else:
                    st.error("Error generating content")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt")