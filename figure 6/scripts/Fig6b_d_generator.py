if (!require("ggplot2")) install.packages("ggplot2")
library(ggplot2)

# --- DATA ---
peaks <- data.frame(
  pos = c(0.1, 1.25, 2.55, 3.85, 4.75), 
  omega = c(42.45, 25.76, 18.2, 35.1, 22.0),
  gene = c("aat", "arg", "mntP", "yheS", "aaeA"),
  dist_is_kb = c(1.2, 3.5, 9.2, 22.5, 48.1)
)

# --- PANEL B: SKYLINE ---
draw_b <- function() {
  x_seq <- seq(0, 5, length.out = 1000)
  y_vals <- sapply(x_seq, function(x) 0.04 + sum(peaks$omega * exp(-((x - peaks$pos)^2) / (2 * 0.12^2))))
  df_b <- data.frame(Position = x_seq, Omega = y_vals)
  
  ggplot(df_b, aes(x = Position, y = Omega)) +
    geom_rect(aes(xmin=0, xmax=5, ymin=-14, ymax=-2), fill="#2C3E50") + 
    geom_area(fill="#E74C3C", alpha=0.9) +
    geom_line(color="#C0392B", linewidth=0.8) +
    geom_vline(xintercept=peaks$pos, color="#00FFFF", linewidth=1.2, alpha=0.4) +
    annotate("text", x=2.5, y=-8, label="purifying metabolic core (w=0.04)", color="white", fontface="bold", size=3) +
    geom_text(data=peaks, aes(x=pos, y=omega + 4, label=gene), fontface="italic", size=3.5, vjust=0) +
    theme_minimal() +
    scale_y_continuous(expand=c(0,0), limits=c(-14, 65)) +
    labs(x = "chromosomal position (mb)", y = expression(bold(paste("adaptive tempo (", omega, ")")))) +
    theme(axis.title = element_text(face = "bold", size = 10), 
          panel.grid.minor = element_blank(),
          plot.background = element_rect(fill = "white", color = NA),
          plot.margin = margin(50, 10, 10, 40)) + # Extra left margin for label
    annotate("text", x = -0.8, y = 65, label = "B", size = 7, fontface = "bold") +
    coord_cartesian(clip = "off")
}

# --- PANEL C: IS-PROXIMITY ---
draw_c <- function() {
  ggplot(peaks, aes(x=dist_is_kb, y=omega)) +
    annotate("rect", xmin=0, xmax=3, ymin=0, ymax=65, fill="#00FFFF", alpha=0.15) +
    annotate("text", x=1.5, y=62, label="IS-HINGE VENT", angle=90, size=3, color="#2C3E50", fontface="bold") +
    geom_smooth(method="lm", formula=y~poly(x,2), color="#2980B9", fill="#D6EAF8", alpha=0.5) +
    geom_point(color="#E67E22", size=5) + 
    annotate("text", x=30, y=40, label="bold(r[s] == -0.98)", parse=TRUE, size=7) +
    theme_classic() + 
    scale_y_continuous(limits=c(0, 65)) +
    labs(x = "distance to nearest is-element (kb)", y = expression(bold(paste("adaptive tempo (", omega, ")")))) +
    theme(plot.margin = margin(50, 10, 10, 40), 
          plot.background = element_rect(fill = "white", color = NA)) +
    annotate("text", x = -10, y = 65, label = "C", size = 7, fontface = "bold") +
    coord_cartesian(clip = "off")
}

# --- PANEL D: SYNERGY ---
draw_d <- function() {
  df_d <- data.frame(Layer=c("metabolic core", "adaptive furnace"), Value=c(35, 65))
  ggplot(df_d, aes(x=1, y=Value, fill=Layer)) +
    geom_bar(stat="identity", width=0.7, color="white", linewidth=1.5) +
    coord_polar(theta="y") +
    scale_fill_manual(values=c("#E74C3C", "#2C3E50")) +
    theme_void() + 
    annotate("text", x=0, y=0, label="structural\nsynergy\n(w=0.04 \u2194 w>1)", size=3.5, color="#2C3E50") +
    theme(legend.position="bottom", legend.title = element_blank(),
          plot.background = element_rect(fill = "white", color = NA),
          plot.margin = margin(50, 10, 10, 10)) +
    annotate("text", x = 1.6, y = 98, label = "D", size = 7, fontface = "bold")
}

# --- SAVE ASSETS ---
ggsave("Fig_6b_Final.png", draw_b(), width=8, height=5, dpi=300, bg="white")
ggsave("Fig_6b_Final.pdf", draw_b(), width=8, height=5, bg="white")

ggsave("Fig_6c_Final.png", draw_c(), width=6, height=5, dpi=300, bg="white")
ggsave("Fig_6c_Final.pdf", draw_c(), width=6, height=5, bg="white")

ggsave("Fig_6d_Final.png", draw_d(), width=6, height=6, dpi=300, bg="white")
ggsave("Fig_6d_Final.pdf", draw_d(), width=6, height=6, bg="white")
