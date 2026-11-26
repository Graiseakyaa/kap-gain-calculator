# KAP Gain Prediction Calculator

This package contains two implementations of the supplied linear prediction equation:

- `app.py`: Streamlit app (recommended for straightforward online deployment)
- `app.R`: Shiny app (for deployment to shinyapps.io or a Shiny server)

## Equation implemented

Predicted Gain_Overall KAP =
3.884463 - 0.006193×Age + 0.099093×Gender_MALE
+ 0.070168×Ethnicity_EWE + 0.210170×Ethnicity_GA
+ 0.046137×Ethnicity_NORTHERN + 0.030121×Ethnicity_Other/rare
+ 0.020079×Residence_SUBURBAN + 0.080205×Residence_URBAN
+ 0.118485×School_program_MIDWIFERY + 0.053628×School_program_NTC
- 0.055829×School_program_NURSING - 0.864958×Baseline_Overall_KAP

The random residual term epsilon is not added to the point prediction.

## Important model assumptions

The calculator assumes these reference categories:
- Gender: Female
- Ethnicity: Akan
- Residence: Rural
- School programme: the omitted/reference programme not listed in the equation

Confirm these against the original regression output and data coding before using results in research or making decisions. The input score must use exactly the same scale as `Baseline_Overall_KAP` in the model, and the predicted outcome uses the same scale as the fitted gain outcome.

## Deploy the Streamlit version online (free option)

1. Create or sign in to a GitHub account.
2. Create a new public repository, e.g. `kap-gain-calculator`.
3. Upload `app.py` and `requirements.txt` to the repository root.
4. Open https://share.streamlit.io/ (or Streamlit Community Cloud from Streamlit's website) and connect GitHub.
5. Choose the repository, branch (`main`), and main file path (`app.py`), then deploy.
6. The platform will provide a public URL after deployment completes.

This package does not itself deploy the app, and no live URL exists until you complete deployment in an account you control.

## Deploy the R Shiny version

1. Create an account at https://www.shinyapps.io/.
2. Install R and the `shiny` package locally.
3. Open `app.R` in RStudio and use the shinyapps.io publishing workflow, or configure `rsconnect` and deploy the app.
4. Copy the public URL provided after deployment.

## Quick local test

Python:
```bash
pip install -r requirements.txt
streamlit run app.py
```

R:
```r
install.packages("shiny")
shiny::runApp()
```
