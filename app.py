import streamlit as st

st.title("Grade Calculator")

# --- PRELIM INPUTS ---
st.header("Prelim Grades")
absences_prelim = st.number_input("Prelim Absences", min_value=0, step=1)
Prelim_Exam = st.number_input("Prelim Exam (0-100)", min_value=0.0, max_value=100.0, step=0.1)
Prelim_Quizzes = st.number_input("Prelim Quizzes (0-100)", min_value=0.0, max_value=100.0, step=0.1)
Prelim_Requirements = st.number_input("Prelim Requirements (0-100)", min_value=0.0, max_value=100.0, step=0.1)
Prelim_Recitation = st.number_input("Prelim Recitation (0-100)", min_value=0.0, max_value=100.0, step=0.1)

# --- MIDTERM INPUTS ---
st.header("Midterm Grades")
absences_midterm = st.number_input("Midterm Absences", min_value=0, step=1)
Midterm_Exam = st.number_input("Midterm Exam (0-100)", min_value=0.0, max_value=100.0, step=0.1)
Midterm_Quizzes = st.number_input("Midterm Quizzes (0-100)", min_value=0.0, max_value=100.0, step=0.1)
Midterm_Requirements = st.number_input("Midterm Requirements (0-100)", min_value=0.0, max_value=100.0, step=0.1)
Midterm_Recitation = st.number_input("Midterm Recitation (0-100)", min_value=0.0, max_value=100.0, step=0.1)

# --- FINALS INPUTS ---
st.header("Finals Grades")
absences_finals = st.number_input("Finals Absences", min_value=0, step=1)
Finals_Exam = st.number_input("Finals Exam (0-100)", min_value=0.0, max_value=100.0, step=0.1)
Finals_Quizzes = st.number_input("Finals Quizzes (0-100)", min_value=0.0, max_value=100.0, step=0.1)
Finals_Requirements = st.number_input("Finals Requirements (0-100)", min_value=0.0, max_value=100.0, step=0.1)
Finals_Recitation = st.number_input("Finals Recitation (0-100)", min_value=0.0, max_value=100.0, step=0.1)


# --- CALCULATIONS ---
def compute_term(exam, quizzes, reqs, rec, absences):
    if absences >= 4:
        return None, "FAILED due to 4 or more absences"
    attendance = max(0, 100 - (absences * 10))
    class_standing = (0.4 * quizzes) + (0.3 * reqs) + (0.3 * rec)
    term_grade = (0.6 * exam) + (0.1 * attendance) + (0.3 * class_standing)
    return term_grade, None

# Compute each term
prelim, error_prelim = compute_term(Prelim_Exam, Prelim_Quizzes, Prelim_Requirements, Prelim_Recitation, absences_prelim)
midterm, error_midterm = compute_term(Midterm_Exam, Midterm_Quizzes, Midterm_Requirements, Midterm_Recitation, absences_midterm)
finals, error_finals = compute_term(Finals_Exam, Finals_Quizzes, Finals_Requirements, Finals_Recitation, absences_finals)

# --- DISPLAY RESULTS ---
if error_prelim:
    st.error(f"Prelim: {error_prelim}")
else:
    st.success(f"Prelim Grade: {prelim:.2f}")

if error_midterm:
    st.error(f"Midterm: {error_midterm}")
else:
    st.success(f"Midterm Grade: {midterm:.2f}")

if error_finals:
    st.error(f"Finals: {error_finals}")
else:
    st.success(f"Finals Grade: {finals:.2f}")

# Overall grade (only if all terms are valid)
if prelim and midterm and finals:
    overall = (0.2 * prelim) + (0.3 * midterm) + (0.5 * finals)
    st.info(f"Overall Grade: {overall:.2f}")

    # Targets
    target_pass = 75
    target_dl = 90

    st.write("### Required Grades for Goals")
    st.write(f"To PASS (75%): Need average ≥ {target_pass}")
    st.write(f"To be DEAN'S LISTER (90%): Need average ≥ {target_dl}")
