import streamlit as st

st.set_page_config(page_title="Grade Calculator", layout="wide")
st.title("📘 Student Grade Calculator")

st.markdown(
    """
    <style>
        .stTabs [data-baseweb="tab-list"] {
            gap: 20px;
        }
        .grade-card {
            padding: 20px;
            border-radius: 12px;
            background: #f9f9ff;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        .grade-header {
            font-weight: bold;
            font-size: 1.1rem;
            color: #4b0082;
            margin-bottom: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Helper function ----
def compute_grade(absences, exam, quizzes, requirements, recitation):
    attendance = max(0, 100 - (absences * 10))
    class_standing = (0.4 * quizzes) + (0.3 * requirements) + (0.3 * recitation)
    return (0.6 * exam) + (0.1 * attendance) + (0.3 * class_standing)

# ---- Tabs for grading periods ----
tabs = st.tabs(["📖 Prelim", "📚 Midterm", "📝 Finals"])

with tabs[0]:
    st.markdown('<div class="grade-card"><div class="grade-header">Prelim Inputs</div>', unsafe_allow_html=True)
    c = st.columns(5)
    absences_prelim = c[0].number_input("Absences", min_value=0, step=1, key="abs_prelim")
    prelim_exam = c[1].number_input("Exam", min_value=0.0, max_value=100.0, step=0.1, key="exam_prelim")
    prelim_quizzes = c[2].number_input("Quizzes", min_value=0.0, max_value=100.0, step=0.1, key="quiz_prelim")
    prelim_requirements = c[3].number_input("Requirements", min_value=0.0, max_value=100.0, step=0.1, key="req_prelim")
    prelim_recitation = c[4].number_input("Recitation", min_value=0.0, max_value=100.0, step=0.1, key="recit_prelim")
    st.markdown("</div>", unsafe_allow_html=True)

with tabs[1]:
    st.markdown('<div class="grade-card"><div class="grade-header">Midterm Inputs</div>', unsafe_allow_html=True)
    c = st.columns(5)
    absences_midterm = c[0].number_input("Absences", min_value=0, step=1, key="abs_midterm")
    midterm_exam = c[1].number_input("Exam", min_value=0.0, max_value=100.0, step=0.1, key="exam_midterm")
    midterm_quizzes = c[2].number_input("Quizzes", min_value=0.0, max_value=100.0, step=0.1, key="quiz_midterm")
    midterm_requirements = c[3].number_input("Requirements", min_value=0.0, max_value=100.0, step=0.1, key="req_midterm")
    midterm_recitation = c[4].number_input("Recitation", min_value=0.0, max_value=100.0, step=0.1, key="recit_midterm")
    st.markdown("</div>", unsafe_allow_html=True)

with tabs[2]:
    st.markdown('<div class="grade-card"><div class="grade-header">Finals Inputs</div>', unsafe_allow_html=True)
    c = st.columns(5)
    absences_finals = c[0].number_input("Absences", min_value=0, step=1, key="abs_finals")
    finals_exam = c[1].number_input("Exam", min_value=0.0, max_value=100.0, step=0.1, key="exam_finals")
    finals_quizzes = c[2].number_input("Quizzes", min_value=0.0, max_value=100.0, step=0.1, key="quiz_finals")
    finals_requirements = c[3].number_input("Requirements", min_value=0.0, max_value=100.0, step=0.1, key="req_finals")
    finals_recitation = c[4].number_input("Recitation", min_value=0.0, max_value=100.0, step=0.1, key="recit_finals")
    st.markdown("</div>", unsafe_allow_html=True)

# ---- Calculation ----
if st.button("= Calculate", use_container_width=True):
    total_absences = absences_prelim + absences_midterm + absences_finals

    if total_absences >= 4:
        st.error(f"❌ FAILED due to {total_absences} total absences (limit is 3)")
    else:
        prelim = compute_grade(absences_prelim, prelim_exam, prelim_quizzes, prelim_requirements, prelim_recitation)
        midterm = compute_grade(absences_midterm, midterm_exam, midterm_quizzes, midterm_requirements, midterm_recitation)
        finals = compute_grade(absences_finals, finals_exam, finals_quizzes, finals_requirements, finals_recitation)

        overall = (0.2 * prelim) + (0.3 * midterm) + (0.5 * finals)

        # ---- Dashboard ----
        st.subheader("📊 Results Dashboard")

        st.progress(min(overall / 100, 1.0))

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Prelim", f"{prelim:.2f}")
        col2.metric("Midterm", f"{midterm:.2f}")
        col3.metric("Finals", f"{finals:.2f}")
        col4.metric("Overall", f"{overall:.2f}")

        if overall < 75:
            st.error("📉 Status: FAILED")
        elif overall >= 90:
            st.success("🏅 Status: Dean's Lister")
        else:
            st.info("✅ Status: PASSED")

        # ---- Required Grades ----
        target_pass, target_dl = 75, 90
        midterm_pass = (target_pass - (0.2 * prelim)) / 0.8
        finals_pass = midterm_pass
        midterm_dl = (target_dl - (0.2 * prelim)) / 0.8
        finals_dl = midterm_dl

        st.subheader("🎯 Required Grades")
        st.write(f"To **PASS (75%)** → Midterm: `{midterm_pass:.2f}`, Finals: `{finals_pass:.2f}`")
        st.write(f"To be **Dean's Lister (90%)** → Midterm: `{midterm_dl:.2f}`, Finals: `{finals_dl:.2f}`")
