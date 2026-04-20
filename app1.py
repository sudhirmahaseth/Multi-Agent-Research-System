import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent Research System")
st.write("Search → Read → Write → Critique")

topic = st.text_input("Enter Topic", placeholder="Artificial Intelligence Trends 2026")

if st.button("Run Research"):
    if topic.strip():
        with st.spinner("Agents are working..."):
            result = run_research_pipeline(topic)

        st.success("Research Completed ✅")

        if isinstance(result, dict):
            if "search_results" in result:
                st.subheader("🔎 Search Results")
                st.write(result["search_results"])

            if "summary" in result:
                st.subheader("📘 Reader Summary")
                st.write(result["summary"])

            if "article" in result:
                st.subheader("✍️ Final Article")
                st.write(result["article"])

            if "feedback" in result:
                st.subheader("🧠 Critic Feedback")
                st.write(result["feedback"])
        else:
            st.write(result)
    else:
        st.warning("Please enter a topic.")