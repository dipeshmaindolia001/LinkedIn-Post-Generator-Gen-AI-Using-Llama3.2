# import streamlit as st
# from few_shot import FewShotPosts
# from post_generator import generate_post


# # Options for length and language
# length_options = ["Short", "Medium", "Long"]
# language_options = ["English", "Hinglish"]


# # Main app layout
# def main():
#     st.subheader("LinkedIn Post Generator")

#     # Create three columns for the dropdowns
#     col1, col2, col3 = st.columns(3)

#     fs = FewShotPosts()
#     tags = fs.get_tags()
#     with col1:
#         # Dropdown for Topic (Tags)
#         selected_tag = st.selectbox("Topic", options=tags)

#     with col2:
#         # Dropdown for Length
#         selected_length = st.selectbox("Length", options=length_options)

#     with col3:
#         # Dropdown for Language
#         selected_language = st.selectbox("Language", options=language_options)



#     # Generate Button
#     if st.button("Generate"):
#         post = generate_post(selected_length, selected_language, selected_tag)
#         st.write(post)


# # Run the app
# if __name__ == "__main__":
#     main()





import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Page config
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="💼",
    layout="centered",
)

# Options
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# Custom light-theme CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #f5f7fa;
    }
    .main-title {
        font-size: 2.1rem;
        font-weight: 700;
        color: #0a66c2;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        color: #5f6b7a;
        font-size: 1rem;
        margin-bottom: 1.8rem;
    }
    div[data-testid="stSelectbox"] label {
        font-weight: 600;
        color: #1d2530;
    }
    .stButton>button {
        background-color: #0a66c2;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        border: none;
        width: 100%;
        margin-top: 0.5rem;
    }
    .stButton>button:hover {
        background-color: #084d94;
        color: white;
    }
    .post-box {
        background-color: white;
        border: 1px solid #e1e5ea;
        border-radius: 10px;
        padding: 1.4rem;
        margin-top: 1.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        white-space: pre-wrap;
        font-size: 0.98rem;
        color: #1d2530;
        line-height: 1.5;
    }
    </style>
""", unsafe_allow_html=True)


def main():
    st.markdown('<div class="main-title">💼 LinkedIn Post Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Generate ready-to-post content in seconds</div>', unsafe_allow_html=True)

    fs = FewShotPosts()
    tags = fs.get_tags()

    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            selected_tag = st.selectbox("📌 Topic", options=tags)
        with col2:
            selected_length = st.selectbox("📏 Length", options=length_options)
        with col3:
            selected_language = st.selectbox("🌐 Language", options=language_options)

    generate = st.button("✨ Generate Post")

    if generate:
        with st.spinner("Generating your post..."):
            post = generate_post(selected_length, selected_language, selected_tag)
        st.markdown(f'<div class="post-box">{post}</div>', unsafe_allow_html=True)
        st.download_button("⬇️ Download as .txt", data=post, file_name="linkedin_post.txt")


if __name__ == "__main__":
    main()