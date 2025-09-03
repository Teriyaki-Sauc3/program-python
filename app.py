import streamlit as st

st.set_page_config(page_title="Grade Calculator", layout="wide")
st.title("📘 Student Grade Calculator")

# --- PRELIM ---
st.subheader("Prelim")
cols = st.columns(5)
absences_prelim = cols[0].number_input("Absences", min_value=0, step=1, key="abs_prelim")
prelim_exam = cols[1].number_input("Exam", min_value=0.0, max_value=100.0, step=0.1, key="exam_prelim")
prelim_quizzes = cols[2].number_input("Quizzes", min_value=0.0, max_value=100.0, step=0.1, key="quiz_prelim")
prelim_requirements = cols[3].number_input("Requirements", min_value=0.0, max_value=100.0, step=0.1, key="req_prelim")
prelim_recitation = cols[4].number_input("Recitation", min_value=0.0, max_value=100.0, step=0.1, key="recit_prelim")

# --- MIDTERM ---
st.subheader("Midterm")
cols = st.columns(5)
absences_midterm = cols[0].number_input("Absences", min_value=0, step=1, key="abs_midterm")
midterm_exam = cols[1].number_input("Exam", min_value=0.0, max_value=100.0, step=0.1, key="exam_midterm")
midterm_quizzes = cols[2].number_input("Quizzes", min_value=0.0, max_value=100.0, step=0.1, key="quiz_midterm")
midterm_requirements = cols[3].number_input("Requirements", min_value=0.0, max_value=100.0, step=0.1, key="req_midterm")
midterm_recitation = cols[4].number_input("Recitation", min_value=0.0, max_value=100.0, step=0.1, key="recit_midterm")

# --- FINALS ---
st.subheader("Finals")
cols = st.columns(5)
absences_finals = cols[0].number_input("Absences", min_value=0, step=1, key="abs_finals")
finals_exam = cols[1].number_input("Exam", min_value=0.0, max_value=100.0, step=0.1, key="exam_finals")
finals_quizzes = cols[2].number_input("Quizzes", min_value=0.0, max_value=100.0, step=0.1, key="quiz_finals")
finals_requirements = cols[3].number_input("Requirements", min_value=0.0, max_value=100.0, step=0.1, key="req_finals")
finals_recitation = cols[4].number_input("Recitation", min_value=0.0, max_value=100.0, step=0.1, key="recit_finals")

# --- CALCULATION ---
if st.button("= Calculate"):
    def compute_grade(absences, exam, quizzes, requirements, recitation):
        attendance = max(0, 100 - (absences * 10))
        class_standing = (0.4 * quizzes) + (0.3 * requirements) + (0.3 * recitation)
        return (0.6 * exam) + (0.1 * attendance) + (0.3 * class_standing)

    # total absences across all grading periods
    total_absences = absences_prelim + absences_midterm + absences_finals

    if total_absences >= 4:
        st.error(f"FAILED due to {total_absences} total absences (limit is 3)")
    else:
        # compute grades
        prelim = compute_grade(absences_prelim, prelim_exam, prelim_quizzes, prelim_requirements, prelim_recitation)
        midterm = compute_grade(absences_midterm, midterm_exam, midterm_quizzes, midterm_requirements, midterm_recitation)
        finals = compute_grade(absences_finals, finals_exam, finals_quizzes, finals_requirements, finals_recitation)

        overall = (0.2 * prelim) + (0.3 * midterm) + (0.5 * finals)

        # --- RESULTS ---
        col1, col2, col3 = st.columns(3)
        col1.metric("Prelim", f"{prelim:.2f}")
        col2.metric("Midterm", f"{midterm:.2f}")
        col3.metric("Finals", f"{finals:.2f}")

        if overall < 75:
            st.error(f"Overall Grade: {overall:.2f} → FAILED")
        else:
            st.success(f"Overall Grade: {overall:.2f}")

        # --- REQUIRED GRADES ---
        target_pass = 75
        target_dl = 90

        midterm_pass = (target_pass - (0.2 * prelim)) / 0.8
        finals_pass = midterm_pass
        midterm_dl = (target_dl - (0.2 * prelim)) / 0.8
        finals_dl = midterm_dl

        st.subheader("📌 Required Grades")
        st.write(f"To **PASS (75%)**: Midterm = {midterm_pass:.2f}, Finals = {finals_pass:.2f}")
        st.write(f"To be **Dean's Lister (90%)**: Midterm = {midterm_dl:.2f}, Finals = {finals_dl:.2f}")
