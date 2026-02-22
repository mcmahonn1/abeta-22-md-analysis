# Load the necessary library
library(ggplot2)

# Read the val_min.out file
file_path <- "C:/Week 8/Water_simulations/abf_min.log"
lines <- readLines(file_path)

# Initialize vectors to store steps and potential energy values
steps <- numeric(0)
potential_energy <- numeric(0)

# Loop through each line in the file and extract the data
for (line in lines) {
  # Check if the line starts with "ENERGY:"
  if (grepl("^ENERGY:", line)) {
    # Split the line into individual components
    parts <- unlist(strsplit(line, "\\s+"))
    # Extract minimization step and potential energy
    steps <- c(steps, as.numeric(parts[2]))  # Step is the second value
    potential_energy <- c(potential_energy, as.numeric(parts[3]))  # Potential energy is the third value
  }
}

# Create a data frame for easier plotting
energy_data <- data.frame(Step = steps, PotentialEnergy = potential_energy)

# Plot potential energy vs minimization steps using ggplot2
ggplot(energy_data, aes(x = Step, y = PotentialEnergy)) +
  geom_line(color = "blue") +  # Plot a line graph
  labs(title = "Potential Energy vs Minimization Steps", 
       x = "Minimization Step", 
       y = "Potential Energy (kcal/mol)") +
  theme_minimal()

