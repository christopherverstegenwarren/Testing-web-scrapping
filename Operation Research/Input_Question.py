import streamlit as st

def main():
    st.title("Operations Research Solver AI")
    question = st.text_area("Enter your OR question:")
    if st.button("Solve"):
        result = process_or_question(question)
        st.write("Status:", result['status'])
        st.write("Solution:", result['solution'])
        st.write("Objective Value:", result['objective'])

if __name__ == "__main__":
    main()
