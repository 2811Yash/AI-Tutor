import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini


# Define Physics Tutor Agent
physics_agent = Agent(
    name="Physics Tutor",
    role="Expert physics tutor who explains concepts clearly using real-world examples and equations.",
    model=Gemini(id="gemini-2.0-flash"),
    instructions=[
        "Answer as a physics tutor.",
        "Use simple language with analogies.",
        "Provide formulas and diagrams (as markdown if needed).",
        "Be patient and explain step-by-step."
    ],
    markdown=True
)

# Define Chemistry Tutor Agent
chemistry_agent = Agent(
    name="Chemistry Tutor",
    role="Expert chemistry tutor who explains chemical reactions, structures, and concepts clearly.",
    model=Gemini(id="gemini-2.0-flash"),
    instructions=[
        "Answer as a chemistry tutor.",
        "Use basic examples to explain.",
        "Break down chemical equations step by step.",
        "Explain concepts like atomic structure, bonding, and reactions clearly."
    ],
    markdown=True
)

# Streamlit UI
st.title("🧪 AI Tutor Agents")

subject = st.selectbox("Select a subject", ["Physics", "Chemistry"])
query = st.text_area("Ask your question:")

if st.button("Get Answer"):
    if query.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            if subject == "Physics":
                response=physics_agent.print_response(query)
                print(response)
                st.write(response)
            else:
                response = chemistry_agent.run(query, stream=False)
                print(response)
        st.markdown("### 📘 Answer:")
        st.markdown(response.content)
