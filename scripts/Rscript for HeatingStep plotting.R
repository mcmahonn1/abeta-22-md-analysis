library(ggplot2)
file_path <- "C:/Week 8/Water_simulations/abf_heat.log"
lines <- readLines(file_path)
 #initializing vectors to store steps, temp, and PE
steps <-numeric(0)
temperature <-numeric(0)
potential_energy <-numeric(0)

#loop to extract data for temp and Pe
for(line in lines){
  if (grepl("^ENERGY:", line)) {
    #split line up
    parts <-unlist(strsplit(line, "\\s+"))
    #Extract minimization step 
    steps <- c(steps, as.numeric(parts[2]))
    #extract T 12th value
    temperature <-c(temperature, as.numeric(parts[13]))
    #Extract Pe
    potential_energy <-c(potential_energy, as.numeric(parts[11]))
  }
}
#Data frame for easier plotting
heat_data <- data.frame(Step=steps, Temperature= temperature, PotentialEnergy= potential_energy)
#Plotting temp and Pe
p1 <- ggplot(heat_data, aes(x=Step, y= Temperature))+
  geom_line(color="orange")+
  labs(title="Temp vs heating steps",
       x= "Heating Step",
       y= "Temperature (K)")+
  theme_minimal()

p2 <- ggplot(heat_data, aes(x= Step, y= potential_energy))+
  geom_line(color="blue") +
  labs(title="Potential Energy Ep(t) vs heating Steps",
       x="Heating Step",
       y="Potential Energy (kcal/mol") +
  theme_minimal()

print(p1)
print(p2)
print(range(temperature))



