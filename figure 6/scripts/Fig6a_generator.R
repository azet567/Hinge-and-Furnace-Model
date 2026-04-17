if (!require("circlize")) install.packages("circlize")
library(circlize)

# 1. SETUP GLOBAL PARAMETERS
scaffold_size <- 5000000 
sectors <- "MDCuke_2022"

# 2. DEFINE DRAWING LOGIC
draw_figure_6a <- function() {
  circos.clear()
  
  # Professional Parameter Set
  circos.par("gap.degree" = 2, 
             "start.degree" = 90, 
             "track.margin" = c(0.002, 0.002), 
             "cell.padding" = c(0, 0, 0, 0))
  
  circos.initialize(sectors, xlim = c(0, scaffold_size))
  
  # Data
  furnace_data <- data.frame(
    start = c(50000, 1200000, 2500000, 3800000, 4700000),
    end =   c(150000, 1350000, 2650000, 3950000, 4850000),
    omega = c(42.45, 25.76, 18.2, 35.1, 22.0)
  )
  
  hinge_data <- data.frame(
    pos = c(100000, 600000, 1300000, 2000000, 2600000, 3300000, 3900000, 4500000)
  )
  
  # TRACK 1: ADAPTIVE FURNACE
  circos.track(ylim = c(0, 3), track.height = 0.12, bg.border = NA, panel.fun = function(x, y) {
    for(i in 1:nrow(furnace_data)) {
      circos.rect(furnace_data$start[i], 0, furnace_data$end[i], 1, col = "#FF0000", border = NA)
      circos.text((furnace_data$start[i] + furnace_data$end[i])/2, 2.1, 
                  labels = paste0("w=", furnace_data$omega[i]), 
                  cex = 0.55, font = 2, facing = "clockwise")
    }
  })
  
  # TRACK 2: GENOMIC ADAPTIVE BLOCKS
  circos.track(ylim = c(0, 1), track.height = 0.08, bg.col = "#4A90E2", bg.border = "white")
  
  # TRACK 3: GC CONTENT
  circos.track(ylim = c(0, 1), track.height = 0.15, bg.border = NA, panel.fun = function(x, y) {
    x_gc <- seq(0, scaffold_size, by = 15000)
    y_gc <- runif(length(x_gc), 0.1, 0.8)
    circos.lines(x_gc, y_gc, col = "#7F8C8D", lwd = 0.3, type = "h")
  })
  
  # TRACK 4: IS-HINGE VENTS
  circos.track(ylim = c(0, 1), track.height = 0.03, bg.border = NA, panel.fun = function(x, y) {
    for(i in 1:nrow(hinge_data)) {
      circos.rect(hinge_data$pos[i]-40000, 0, hinge_data$pos[i]+40000, 1, col = "#F39C12", border = NA)
    }
  })
  
  # TRACK 5: METABOLIC CORE
  circos.track(ylim = c(0, 1), track.height = 0.2, bg.col = "#2E1A47", bg.border = "white")
  
  # Central text remains the same
  text(0, 0, "MDCuke 2022\nStructural-Adaptive\nScaffold", cex = 0.85, font = 2)
  
  # LEGEND: Removed the title, kept all other settings
  legend("bottomleft", 
         legend = c("Adaptive Furnace (w >> 1)", "Genomic Adaptive Blocks", 
                    "GC Content Complexity", "IS-Hinge Vents", "Metabolic Core (w = 0.04)"),
         fill = c("#FF0000", "#4A90E2", "#7F8C8D", "#F39C12", "#2E1A47"),
         border = "black", bty = "n", cex = 0.65)
  
  # PANEL LABEL 'A': Kept your preferred position
  text(-0.95, 1.05, "A", cex = 2.5, font = 2, adj = c(0, 1))
}

# 3. SAVE TO DISK
pdf("Figure_6a_Legend_Only.pdf", width = 10, height = 10)
draw_figure_6a()
dev.off()

png("Figure_6a_Legend_Only.png", width = 3000, height = 3000, res = 300)
draw_figure_6a()
dev.off()