import streamlit as st

st.title(" Student Grade Calculator")

# --- INPUTS ---
absences = st.number_input("Number of absences", min_value=0, step=1)

Prelim_Exam = st.number_input("Prelim Exam Grade (0-100)", min_value=0.0, max_value=100.0, step=0.1)
Quizzes = st.number_input("Quizzes Grade (0-100)", min_value=0.0, max_value=100.0, step=0.1)
Requirements = st.number_input("Requirements Grade (0-100)", min_value=0.0, max_value=100.0, step=0.1)
Recitation = st.number_input("Recitation Grade (0-100)", min_value=0.0, max_value=100.0, step=0.1)

if absences >= 4:
    st.error("FAILED due to 4 or more absences")
else:
    attendance = 100 - (absences * 10)
    class_standing = (0.4 * Quizzes) + (0.3 * Requirements) + (0.3 * Recitation)
    prelim = (0.6 * Prelim_Exam) + (0.1 * attendance) + (0.3 * class_standing)

    st.success(f" Prelim Grade: {prelim:.2f}")

    Midterm = st.number_input("Midterm Grade (0-100)", min_value=0.0, max_value=100.0, step=0.1)
    Finals = st.number_input("Finals Grade (0-100)", min_value=0.0, max_value=100.0, step=0.1)

    overall = (0.2 * prelim) + (0.3 * Midterm) + (0.5 * Finals)
    st.info(f"Overall Grade: {overall:.2f}")

    # Targets
    target_pass = 75
    midterm_pass = (target_pass - (0.2 * prelim)) / 0.8
    finals_pass = midterm_pass

    target_dl = 90
    midterm_dl = (target_dl - (0.2 * prelim)) / 0.8
    finals_dl = midterm_dl

    st.write("###  Required Grades")
    st.write(f"To PASS (75%): Midterm = {midterm_pass:.2f}, Finals = {finals_pass:.2f}")
    st.write(f"To be DEAN'S LISTER (90%): Midterm = {midterm_dl:.2f}, Finals = {finals_dl:.2f}")
