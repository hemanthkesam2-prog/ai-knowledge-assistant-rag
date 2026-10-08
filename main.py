import streamlit as st

st.set_page_config(
    page_title="AI Knowledge Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Knowledge Assistant")
st.write("Welcome to your AI Knowledge Assistant!")

uploaded_file = st.file_uploader(
    "Upload your knowledge file",
    type=["txt", "md"]
)

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")

    st.success("File uploaded successfully! ✅")

    question = st.text_input("Ask a question:")

    if question:
        st.subheader("Answer")

        question_lower = question.lower()

        if "python" in question_lower:
            st.write(
                "Python is a high-level, general-purpose programming language "
                "used for web development, data analysis, AI, machine learning, "
                "automation, and many other applications."
            )
        else:
            st.write(
                "I found your document, but I don't have an answer "
                "for this question yet."
            )

        st.subheader("Source")
        st.write(uploaded_file.name)