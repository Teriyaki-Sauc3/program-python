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

# --- CALCULATION BUTTON ---
if st.button("= Calculate"):
    # sample formula (you can adjust weights)
    def compute_grade(absences, exam, quizzes, requirements, recitation):
        if absences >= 4:
            return None, "FAILED due to 4 or more absences"
        attendance = max(0, 100 - (absences * 10))
        class_standing = (0.4 * quizzes) + (0.3 * requirements) + (0.3 * recitation)
        return (0.6 * exam) + (0.1 * attendance) + (0.3 * class_standing), None

    prelim, err1 = compute_grade(absences_prelim, prelim_exam, prelim_quizzes, prelim_requirements, prelim_recitation)
    midterm, err2 = compute_grade(absences_midterm, midterm_exam, midterm_quizzes, midterm_requirements, midterm_recitation)
    finals, err3 = compute_grade(absences_finals, finals_exam, finals_quizzes, finals_requirements, finals_recitation)

    if err1 or err2 or err3:
        st.error(err1 or err2 or err3)
    else:
        overall = (0.2 * prelim) + (0.3 * midterm) + (0.5 * finals)
        st.success(f"📊 Prelim: {prelim:.2f} | Midterm: {midterm:.2f} | Finals: {finals:.2f}")
        st.info(f"⭐ Overall Grade: {overall:.2f}")
