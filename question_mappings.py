# question_mappings.py

"""
Mappings from feature IDs to user-facing questions, scales, and Z-score conversions.
This version is updated to use 12 specific questions based on logistic regression model features,
with question text refined for clarity and parent-direction.
"""

QUESTION_MAPPINGS = [
    {
        'id': 'ksads_sleepprob_raw_814_p',
        'question_text': '**Does your child often have trouble sleeping (e.g., falling or staying asleep)?**',
        'scale_type': 'YN',
        'options': {'No': 0, 'Yes': 1}, # Values for backend; Streamlit options will be keys
        'z_score_map': {0: -0.75, 1: 0.75} # Mapping numeric values to Z-scores
    },
    {
        'id': 'cbcl_q71_p',
        'question_text': '**Is your child often self-conscious or easily embarrassed?**',
        'scale_type': '012',
        'options': {'Not true': 0, 'Somewhat or sometime true': 1, 'Very true or often true': 2},
        'z_score_map': {0: -0.75, 1: 0.0, 2: 0.75}
    },
    {
        'id': 'famhx_ss_parent_prf_p',
        'question_text': '**As the parent answering, have you received a professional mental health diagnosis?**',
        'scale_type': 'YN',
        'options': {'No': 0, 'Yes': 1},
        'z_score_map': {0: -0.75, 1: 0.75}
    },
    {
        'id': 'ksads_asd_raw_562_p',
        'question_text': '**Does your child often show repetitive behaviors (e.g., movements or routines)?**',
        'scale_type': 'YN',
        'options': {'No': 0, 'Yes': 1},
        'z_score_map': {0: -0.75, 1: 0.75}
    },
    {
        'id': 'cbcl_q04_p',
        'question_text': '**Does your child seem to cry a lot?**',
        'scale_type': '012',
        'options': {'Not true': 0, 'Somewhat true': 1, 'Very true': 2}, # Standard CBCL scoring often implies this kind of scale
        'z_score_map': {0: -0.75, 1: 0.0, 2: 0.75}
    },
    {
        'id': 'asr_q47_p',
        'question_text': '**Does your child often seem overwhelmed by their responsibilities?**',
        'scale_type': '012',
        'options': {'Not true': 0, 'Somewhat true': 1, 'Very true': 2}, # Assuming similar scale to other 0-2 Likerts
        'z_score_map': {0: -0.75, 1: 0.0, 2: 0.75}
    },
    {
        'id': 'cbcl_q86_p',
        'question_text': '**Does your child talk about suicide?**',
        'scale_type': '012',
        'options': {'Not true': 0, 'Somewhat true': 1, 'Very true': 2},
        'z_score_map': {0: -0.75, 1: 0.0, 2: 0.75}
    },
    {
        'id': 'sds_p_ss_does',
        'question_text': '**Is your child actively involved in social activities?**',
        'scale_type': 'YN',
        'options': {'No': 0, 'Yes': 1},
        'z_score_map': {0: 0.75, 1: -0.75} # 'Yes' is protective
    },
    {
        'id': 'cbcl_q22_p',
        'question_text': '**Does your child get into many fights?**',
        'scale_type': '012',
        'options': {'Not true': 0, 'Somewhat true': 1, 'Very true': 2},
        'z_score_map': {0: -0.75, 1: 0.0, 2: 0.75}
    },
    {
        'id': 'fhx_3hb_p',
        'question_text': '**Is there a history of behavioral health problems in your child\'s biological family?**',
        'scale_type': 'YN',
        'options': {'No': 0, 'Yes': 1},
        'z_score_map': {0: -0.75, 1: 0.75}
    },
    {
        'id': 'cbcl_q09_p',
        'question_text': '**Does your child often have trouble concentrating or get easily distracted?**',
        'scale_type': '012',
        'options': {'Not true': 0, 'Somewhat true': 1, 'Very true': 2},
        'z_score_map': {0: -0.75, 1: 0.0, 2: 0.75}
    },
    {
        'id': 'asr_q116_p',
        'question_text': '**Does your child often feel disliked or unaccepted by others?**',
        'scale_type': '012',
        'options': {'Not true': 0, 'Somewhat true': 1, 'Very true': 2},
        'z_score_map': {0: -0.75, 1: 0.0, 2: 0.75}
    }
]

# The get_question_by_id function is no longer needed by prediction_calculator_logic.py
# as it now uses a direct lookup from a dictionary generated from QUESTION_MAPPINGS.
# If it were needed elsewhere, it would look like this:
# def get_question_by_id(feature_id):
#     """Helper function to retrieve a question mapping by its ID."""
#     for q_map in QUESTION_MAPPINGS:
#         if q_map['id'] == feature_id:
#             return q_map
#     return None
