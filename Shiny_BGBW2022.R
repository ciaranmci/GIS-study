# Shiny version of a ArcGIS Shiney123 survey I made.
# The Survey123 app is here:
# https://survey123.arcgis.com/share/4aaa15ffb39b49a2a304abe4f99808c7
# https://medium.com/@joyplumeri/how-to-make-interactive-maps-in-r-shiny-brief-tutorial-c2e1ef0447da
#
#


############
## Set up ##
############
# ----
here::i_am("Shiny_BGBW2022.R")
# Load prerequisites.
list_of_packages <- c("shiny", "leaflet","leaflet.extras", "tidyverse", "here")
new_packages <- list_of_packages[!(list_of_packages %in% installed.packages()[,"Package"])]
if(length(new_packages)) install.packages(new_packages)
for (i in 1:length(list_of_packages))
{
  library(list_of_packages[i],character.only = T)
}

# Load data.
#data_quake <- readr::read_csv(here::here("data/USGS quake data.csv"))


# ----


##############
## Shiny UI ##
##############
# ----
# Maybe get images with radio buttons using
# this syntax: https://stackoverflow.com/questions/65035326/images-for-radiobutton-r-shiny
ui_BGBW <- fluidPage(
  radioButtons(inputId = "bird", label = "Which bird?",
               choiceNames = list(
                              img(src = here::here("data","RSPB birds","blackbird.JPG")),
                              img(src = here::here("data","RSPB birds","blue_tit,JPG")),
                              img(src = here::here("data","RSPB birds","chaffinch.JPG")),
                              img(src = here::here("data","RSPB birds","goldfinch.JPG")),
                              img(src = here::here("data","RSPB birds","great_tit.JPG")),
                              img(src = here::here("data","RSPB birds","house_sparrow.JPG")),
                              img(src = here::here("data","RSPB birds","magpie.JPG")),
                              img(src = here::here("data","RSPB birds","robin.JPG")),
                              img(src = here::here("data","RSPB birds","starling.JPG")),
                              img(src = here::here("data","RSPB birds","wood_pigeon.JPG"))
                              ),
               # choiceNames = list("Blackbird",
               #                    "Blue tit",
               #                    "Chaffinch",
               #                    "Goldfinch",
               #                    "Great tit",
               #                    "House sparrow",
               #                    "Magpie",
               #                    "Robin",
               #                    "Starling",
               #                    "Wood pigeon"),
               choiceValues = list("blackbird",
                                   "blue_tit",
                                   "chaffinch",
                                   "goldfinch",
                                   "great_tit",
                                   "house_sparrow",
                                   "magpie",
                                   "robin",
                                   "starling",
                                   "wood_pigeon")
               ),
  textOutput("txt")
) # End of fluidPage. 

# ----


##################
## Shiny server ##
##################
# ----
server_BGBW <- function(input, output) {
  output$txt <- renderText({
    paste("You chose", input$bird)
  })
} # End of server_quake()
# ----

# Launch Shiny app.
shinyApp(ui_BGBW, server_BGBW)
