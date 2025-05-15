import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------
# 1. Setup
# ----------------------------------------
st.set_page_config(page_title="Child Depression Risk Calculator", layout="centered")
st.title("Child Depression Risk Calculator")
st.markdown("""
Please answer the following questions based on your child's behaviors in the past few weeks.

Use this scale:
- 0 = Never
- 1 = Sometimes
- 2 = Often
""")

# ----------------------------------------
# 2. Load cleaned baseline data
# ----------------------------------------
@st.cache_data
def load_baseline():
    df = pd.read_csv("filtered_merged_variables.csv")
    top_vars = [
        'ksads_sleepprob_raw_814_p', 'cbcl_q71_p', 'famhx_ss_parent_prf_p',
        'ksads_asd_raw_562_p', 'cbcl_q04_p', 'asr_q47_p', 'cbcl_q86_p',
        'sds_p_ss_does', 'cbcl_q22_p', 'fhx_3hb_p', 'cbcl_q09_p', 'asr_q116_p'
    ]
    return df[top_vars].dropna()

baseline_df = load_baseline()

# ----------------------------------------
# 3. Logistic Regression Coefficients
# ----------------------------------------
intercept = -0.7241

coefficients = {
    'ksads_sleepprob_raw_814_p': 0.1580,
    'cbcl_q71_p': 0.1264,
    'famhx_ss_parent_prf_p': 0.1170,
    'ksads_asd_raw_562_p': -0.1068,
    'cbcl_q04_p': 0.1030,
    'asr_q47_p': 0.1008,
    'cbcl_q86_p': 0.0986,
    'sds_p_ss_does': 0.0963,
    'cbcl_q22_p': 0.0947,
    'fhx_3hb_p': 0.0884,
    'cbcl_q09_p': 0.0876,
    'asr_q116_p': 0.0864
}

labels = {
    'ksads_sleepprob_raw_814_p': "Sleep problems (e.g., difficulty falling/staying asleep)",
    'cbcl_q71_p': "Self-conscious or easily embarrassed",
    'famhx_ss_parent_prf_p': "Parent has professional mental health diagnosis",
    'ksads_asd_raw_562_p': "Repetitive behaviors (ASD-related symptom)",
    'cbcl_q04_p': "Cries a lot",
    'asr_q47_p': "Feels overwhelmed by responsibilities",
    'cbcl_q86_p': "Talks about suicide",
    'sds_p_ss_does': "Social activity involvement",
    'cbcl_q22_p': "Gets in many fights",
    'fhx_3hb_p': "Family history of behavioral health problems",
    'cbcl_q09_p': "Cannot concentrate, easily distracted",
    'asr_q116_p': "Feels disliked or unaccepted"
}

# ----------------------------------------
# 4. Inputs + Plots
# ----------------------------------------
responses = {}
for var in coefficients:
    label = labels.get(var, var)
    col1, col2 = st.columns([2, 3])

    with col1:
        if var in ['famhx_ss_parent_prf_p', 'ksads_asd_raw_560_p', 'sai_ss_basket_nyr_p']:
            val = st.selectbox(f"{label} (0 = No, 1 = Yes)", options=[0, 1], index=0, key=var)
        else:
            val = st.selectbox(f"{label}", options=[0, 1, 2], index=0, key=var)
        responses[var] = val

    with col2:
        fig, ax = plt.subplots()
        sns.histplot(baseline_df[var], bins='auto', ax=ax, kde=False)
        ax.axvline(val, color='red', linestyle='--', label="Your response")
        ax.set_title("ABCD Distribution")
        ax.set_xlabel("Response")
        ax.set_ylabel("Count")
        ax.legend()
        st.pyplot(fig)

# ----------------------------------------
# 5. Risk Score
# ----------------------------------------
if st.button("Calculate Depression Risk"):
    log_odds = intercept + sum(responses[v] * coef for v, coef in coefficients.items())
    probability = 1 / (1 + np.exp(-log_odds))

    st.markdown(f"### Estimated Depression Risk: **{probability:.1%}**")

    if probability < 0.25:
        st.success("Low risk")
    elif probability < 0.5:
        st.warning("Moderate risk")
    else:
        st.error("High risk – please consider a professional evaluation.")
