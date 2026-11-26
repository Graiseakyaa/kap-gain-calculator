library(shiny)

ui <- fluidPage(
  titlePanel("KAP Gain Prediction Calculator"),
  p("Linear prediction calculator using the supplied regression equation."),
  helpText("The predicted value excludes the random residual term epsilon."),
  sidebarLayout(
    sidebarPanel(
      numericInput("age", "Age (years)", value = 25, min = 0, max = 120, step = 1),
      selectInput("gender", "Gender", choices = c("Female (reference)" = 0, "Male" = 1)),
      selectInput("ethnicity", "Ethnicity", choices = c(
        "Akan (reference)" = "akan", "Ewe" = "ewe", "Ga" = "ga",
        "Northern" = "northern", "Other/rare" = "other"
      )),
      selectInput("residence", "Residence", choices = c(
        "Rural (reference)" = "rural", "Suburban" = "suburban", "Urban" = "urban"
      )),
      selectInput("program", "School programme", choices = c(
        "Reference programme (not listed)" = "reference",
        "Midwifery" = "midwifery", "NTC" = "ntc", "Nursing" = "nursing"
      )),
      numericInput("baseline", "Baseline overall KAP score", value = 0, step = 0.5)
    ),
    mainPanel(
      h3("Predicted overall KAP gain"),
      verbatimTextOutput("prediction"),
      h4("Interpretation"),
      p("The output is the fitted value on the same scale as the outcome used to fit the model."),
      tags$hr(),
      p("Confirm the original model's reference categories and score coding before research use. ",
        "This app assumes Female, Akan, Rural, and the unlisted reference programme are reference categories. ",
        "The residual error term epsilon is not added to an individual point prediction.")
    )
  )
)

server <- function(input, output, session) {
  output$prediction <- renderText({
    gender_male <- as.numeric(input$gender)
    eth_ewe <- as.numeric(input$ethnicity == "ewe")
    eth_ga <- as.numeric(input$ethnicity == "ga")
    eth_northern <- as.numeric(input$ethnicity == "northern")
    eth_other <- as.numeric(input$ethnicity == "other")
    res_suburban <- as.numeric(input$residence == "suburban")
    res_urban <- as.numeric(input$residence == "urban")
    prog_midwifery <- as.numeric(input$program == "midwifery")
    prog_ntc <- as.numeric(input$program == "ntc")
    prog_nursing <- as.numeric(input$program == "nursing")

    pred <- 3.884463 -
      0.006193 * input$age +
      0.099093 * gender_male +
      0.070168 * eth_ewe +
      0.210170 * eth_ga +
      0.046137 * eth_northern +
      0.030121 * eth_other +
      0.020079 * res_suburban +
      0.080205 * res_urban +
      0.118485 * prog_midwifery +
      0.053628 * prog_ntc -
      0.055829 * prog_nursing -
      0.864958 * input$baseline

    sprintf("%.6f", pred)
  })
}

shinyApp(ui = ui, server = server)
