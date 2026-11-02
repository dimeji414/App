import streamlit as st
import time

st.set_page_config(page_title="Custom Study & AI Practice App", page_icon="🧠", layout="centered")

st.title("🧠 My Personal AI Study & Practice Hub")
st.write("Beat the exam-hall blank-out with active recall, AI practice, and a built-in focus timer.")

# Sidebar for Settings & Timer
st.sidebar.header("Study Settings")
subject = st.sidebar.selectbox("Select Subject", ["Mathematics", "Physics", "Chemistry", "General Studies"])
difficulty = st.sidebar.select_slider("Difficulty Level", options=["Warmup", "Exam-Level", "Tricky Trap"])

st.sidebar.markdown("---")
st.sidebar.header("⏱️ Focus Timer")
timer_minutes = st.sidebar.number_input("Set Timer (Minutes)", min_value=1, max_value=60, value=25)

if "timer_running" not in st.session_state:
    st.session_state.timer_running = False

col1, col2 = st.sidebar.columns(2)
if col1.button("Start Timer"):
    st.session_state.timer_running = True
if col2.button("Reset Timer"):
    st.session_state.timer_running = False

timer_placeholder = st.sidebar.empty()

if st.session_state.timer_running:
    total_seconds = timer_minutes * 60
    for remaining in range(total_seconds, -1, -1):
        if not st.session_state.timer_running:
            break
        mins, secs = divmod(remaining, 60)
        timer_placeholder.markdown(f"**Time Remaining: {mins:02d}:{secs:02d}**")
        time.sleep(1)
    if st.session_state.timer_running:
        st.sidebar.success("Time's up! Take a short break.")
        st.session_state.timer_running = False
else:
    timer_placeholder.markdown(f"Timer set to {timer_minutes} minutes.")

# Main Section: AI Question Generator Simulator
st.subheader(f"📝 {subject} Practice Generator")
st.write(f"Current Target: **{subject}** at **{difficulty}** difficulty.")

if st.button("Generate Practice Question"):
    st.success("Question Generated Successfully!")
    
    if subject == "Mathematics":
        st.markdown("**Question:** Evaluate the integral of $\\frac{1}{x^2 + 4}$ using standard substitution.")
        with st.expander("Click to see Step-by-Step Solution"):
            st.write("1. Recognize this matches the standard arctangent integral formula.")
            st.write("2. Apply the formula: $\\frac{1}{2}\\arctan\\left(\\frac{x}{2}\\right) + C$.")
    else:
        st.markdown(f"**Question:** Explain a core concept in {subject} under the {difficulty} category and test your application logic.")
        with st.expander("Click to see Solution / Explanation"):
            st.write("Core principle breakdown goes here...")

# Personal Tricky Formula Log
st.markdown("---")
st.subheader("📌 Tricky Formula / Concept Log")
user_note = st.text_input("Add a formula or tricky concept to review:")
if st.button("Save to Log"):
    if "notes" not in st.session_state:
        st.session_state.notes = []
    st.session_state.notes.append(f"[{subject}] {user_note}")
    st.success("Saved!")

if "notes" in st.session_state and st.session_state.notes:
    st.write("### Your Saved Review List:")
    for i, note in enumerate(st.session_state.notes, 1):
        st.write(f"{i}. {note}")
