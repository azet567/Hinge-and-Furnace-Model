# Run this to install packages for GBE-260370
required_packages <- c("ggplot2", "dplyr", "tidyr", "readr", "ggpubr")

new_packages <- required_packages[!(required_packages %in% installed.packages()[,"Package"])]
if(length(new_packages)) install.packages(new_packages, repos = "http://cran.us.r-project.org")

print("Environment check complete.")