
import streamlit as st
from rag_chain import ask_question

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="📚"
)

st.title("📚 Enterprise Knowledge Assistant")
st.caption("Ask questions about company policies and IT documents.")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask a question about company documents...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching documents..."):
            try:
                result = ask_question(question)
                answer = result["answer"]
                sources = result["sources"]

                st.write(answer)

                st.caption("Source documents")
                for source in sources:
                    st.write(f"- {source}")

            except Exception as e:
                answer = f"Something went wrong: {e}"
                st.error(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
