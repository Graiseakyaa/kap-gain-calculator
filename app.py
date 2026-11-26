import streamlit as st

st.set_page_config(page_title="KAP Gain Prediction Calculator", page_icon="📈", layout="centered")
st.title("KAP Gain Prediction Calculator")
st.caption("Linear prediction calculator using the supplied regression equation.")

st.info(
    "This calculator returns the model's predicted overall KAP gain (the fitted value). "
    "It does not include the residual error term ε."
)

st.subheader("Enter participant characteristics")
c1, c2 = st.columns(2)
with c1:
    age = st.number_input("Age (years)", min_value=0, max_value=120, value=25, step=1)
    gender = st.selectbox("Gender", ["Female (reference)", "Male"])
    ethnicity = st.selectbox(
        "Ethnicity",
        ["Akan (reference)", "Ewe", "Ga", "Northern", "Other/rare"]
    )
with c2:
    residence = st.selectbox("Residence", ["Rural (reference)", "Suburban", "Urban"])
    school_program = st.selectbox(
        "School programme",
        ["Reference programme (not listed)", "Midwifery", "NTC", "Nursing"]
    )
    baseline = st.number_input("Baseline overall KAP score", value=0.0, step=0.5, format="%.4f")

# Dummy variables use the reference categories indicated in the supplied equation.
gender_male = 1 if gender == "Male" else 0
eth_ewe = 1 if ethnicity == "Ewe" else 0
eth_ga = 1 if ethnicity == "Ga" else 0
eth_northern = 1 if ethnicity == "Northern" else 0
eth_other = 1 if ethnicity == "Other/rare" else 0
res_suburban = 1 if residence == "Suburban" else 0
res_urban = 1 if residence == "Urban" else 0
prog_midwifery = 1 if school_program == "Midwifery" else 0
prog_ntc = 1 if school_program == "NTC" else 0
prog_nursing = 1 if school_program == "Nursing" else 0

pred = (
    3.884463
    - 0.006193 * age
    + 0.099093 * gender_male
    + 0.070168 * eth_ewe
    + 0.210170 * eth_ga
    + 0.046137 * eth_northern
    + 0.030121 * eth_other
    + 0.020079 * res_suburban
    + 0.080205 * res_urban
    + 0.118485 * prog_midwifery
    + 0.053628 * prog_ntc
    - 0.055829 * prog_nursing
    - 0.864958 * baseline
)

st.divider()
st.subheader("Predicted overall KAP gain")
st.metric("Model-predicted gain", f"{pred:.4f}")
st.caption("Prediction is on the same scale as the outcome used to fit the regression model.")

with st.expander("View calculation details"):
    st.code(
        f"""Predicted gain = 3.884463
  - 0.006193 × Age ({age})
  + 0.099093 × Gender_MALE ({gender_male})
  + 0.070168 × Ethnicity_EWE ({eth_ewe})
  + 0.210170 × Ethnicity_GA ({eth_ga})
  + 0.046137 × Ethnicity_NORTHERN ({eth_northern})
  + 0.030121 × Ethnicity_Other/rare ({eth_other})
  + 0.020079 × Residence_SUBURBAN ({res_suburban})
  + 0.080205 × Residence_URBAN ({res_urban})
  + 0.118485 × School_program_MIDWIFERY ({prog_midwifery})
  + 0.053628 × School_program_NTC ({prog_ntc})
  - 0.055829 × School_program_NURSING ({prog_nursing})
  - 0.864958 × Baseline_Overall_KAP ({baseline})
= {pred:.6f}"""
    )

st.warning(
    "Important: Confirm the original model's omitted/reference categories and score coding before research use. "
    "The app assumes Female, Akan, Rural, and 'Reference programme (not listed)' are the reference categories. "
    "The equation's ε is a random residual and is not added to an individual point prediction. "
    "This is a statistical estimate, not a clinical or educational decision rule."
)
