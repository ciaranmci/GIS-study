# Simple tutorial on "How to make interactive maps in R Shiny" available from
# https://medium.com/@joyplumeri/how-to-make-interactive-maps-in-r-shiny-brief-tutorial-c2e1ef0447da
#
# There is an error in the author's syntax for specifying the <depth_type>
# variable that meant she never identified "Deep" earthquakes. I fixed this and 
# used magrittr() pipe syntax to do it.
#
# The only other changes are:
#   1. the use of the here::here() command for locating the 
#      data;
#   2. a little syntax at the start to install and import only the packages
#      that are not installed or imported;
#   3. renaming of variables
#

############
## Set up ##
############
# ----
here::i_am("Shiny_earthquake.R")
# Load prerequisites.
list_of_packages <- c("shiny", "leaflet","leaflet.extras", "tidyverse", "here")
new_packages <- list_of_packages[!(list_of_packages %in% installed.packages()[,"Package"])]
if(length(new_packages)) install.packages(new_packages)
for (i in 1:length(list_of_packages))
{
  library(list_of_packages[i],character.only = T)
}

# Load data.
data_quake <- readr::read_csv(here::here("data/USGS quake data.csv"))

# Categorise earthquake depth
data_quake <- data_quake %>%
  mutate(
        depth_type = case_when(
                          .$depth <= 70 ~ "Shallow",
                          .$depth <= 300 ~ "Intermediate",
                          .$depth > 300 ~ "Deep",
                          TRUE ~ "Other"
                              )
         )
# ----


##############
## Shiny UI ##
##############
# ----
ui_quake <- fluidPage(
  mainPanel( 
    leafletOutput(outputId = "map_quake"),
    absolutePanel(top = 60, left = 20, 
                  checkboxInput("markers", "Depth", FALSE),
                  checkboxInput("heat", "Heatmap", FALSE)
    )
  ))

# ----


##################
## Shiny server ##
##################
# ----
server_quake <- function(input, output, session)
  {
  # Define the colour palatte for the magnitude of the earthquake.
  pal <- colorNumeric(
                      palette = c('gold', 'orange', 'dark orange',
                                  'orange red', 'red', 'dark red'),
                      domain = data_quake$mag
                      )
  
  # Define the colour of for the depth of the earthquakes.
  pal2 <- colorFactor(
                      palette = c('blue', 'yellow', 'red'),
                      domain = data_quake$depth_type
                     )
  # Create the map.
  output$map_quake <- renderLeaflet({
    leaflet(data_quake) %>% 
      setView(lng = -99, lat = 45, zoom = 2)  %>%
      addTiles() %>% 
      addCircles(data = data_quake, lat = ~ latitude, lng = ~ longitude,
                 weight = 1, radius = ~sqrt(mag)*25000,
                 popup = ~as.character(mag),
                 label = ~as.character(paste0("Magnitude: ",
                                              sep = " ", mag)),
                 color = ~pal(mag), fillOpacity = 0.5)
  })
  
  # Make the checkboxes dynamic.
  observe({
    proxy <- leafletProxy("map_quake", data = data_quake)
    proxy %>% clearMarkers()
    if (input$markers) {
      proxy %>% addCircleMarkers(stroke = FALSE, color = ~pal2(depth_type),
                                 fillOpacity = 0.2,
                                 label = ~as.character(paste0("Magnitude: ", sep = " ", mag))) %>%
        addLegend("bottomright", pal = pal2, values = data_quake$depth_type,
                  title = "Depth Type",
                  opacity = 1)
                        } # End of IF statement.
    else {
      proxy %>% clearMarkers() %>% clearControls()
          }
        }) # End of observe({})

  observe({
    proxy <- leafletProxy("map_quake", data = data_quake)
    proxy %>% clearMarkers()
    if (input$heat) {
      proxy %>% addHeatmap(lng = ~longitude, lat = ~latitude, intensity = ~mag,
                           blur =  10, max = 0.05, radius = 15) 
                    } # End of IF statement.
    else{
      proxy %>% clearHeatmap()
        }
    
    
        }) # End of observe({})

  } # End of server_quake()
# ----

# Launch Shiny app.
shinyApp(ui_quake, server_quake)
