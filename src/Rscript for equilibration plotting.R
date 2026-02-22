library(ggplot2)
file_path <- "C:/Week 8/Water_simulations/abf_equil.log"
lines <- readLines(file_path)

# Initialize vectors to store steps, temperature, and unit cell size
steps <- numeric(0)
temperature <- numeric(0)
unit_cell_size <- numeric(0)

# Loop through each line in the file and extract the data
for (line in lines) {
  # Check if the line starts with "ENERGY:"
  if (grepl("^ENERGY:", line)) {
    # Split the line into individual components
    parts <- unlist(strsplit(line, "\\s+"))
    # Extract minimization step (first value)
    steps <- c(steps, as.numeric(parts[2]))  # Step is the second value
    # Extract temperature (12th value)
    temperature <- c(temperature, as.numeric(parts[13]))  # Temperature is the 12th value
    # Extract unit cell volume (18th value)
    volume <- as.numeric(parts[19])  # Volume is the 18th value
    # Calculate unit cell size (L = V^1/3)
    unit_cell_size <- c(unit_cell_size, volume^(1/3))  # Unit cell size is the third of volume
  }
}

# Create a data frame for easier plotting
equil_data <- data.frame(Step = steps, Temperature = temperature, UnitCellSize = unit_cell_size)

# Plot temperature vs equilibration steps using ggplot2
p1 <- ggplot(equil_data, aes(x = Step, y = Temperature)) +
  geom_line(color = "red") +
  labs(title = "Instantaneous Temperature T(t) vs unitcellsize", 
       x = "unit cell size ", 
       y = "Temperature (K)") +
  theme_minimal()

# Plot unit cell size vs equilibration steps
p2 <- ggplot(equil_data, aes(x = Step, y = UnitCellSize)) +
  geom_line(color = "blue") +
  labs(title = "Unit Cell Size L(t) vs equilibration steps", 
       x = "equilibration steps", 
       y = "Unit Cell Size (A)") +
  theme_minimal()

# Print both plots
print(p1)
print(p2)
