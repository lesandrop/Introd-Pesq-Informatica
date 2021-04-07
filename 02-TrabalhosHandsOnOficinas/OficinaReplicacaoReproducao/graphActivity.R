library(ggplot2)

setwd("C:\\Users\\lesandrop\\Desktop")
df_activity <- read.table("activity.data", header = TRUE, sep=",")

df_activity

pl <- ggplot(df_activity,aes(x = Rank, y=Frequency)) +
  scale_x_log10(breaks = scales::trans_breaks("log10", function(x) 10^x), labels = scales::trans_format("log10", scales::math_format(10^.x))) +
  scale_y_log10(breaks = scales::trans_breaks("log10", function(x) 10^x), labels = scales::trans_format("log10", scales::math_format(10^.x))) +
  theme_bw(base_size = 11) + geom_point(shape=1,size=3) + ylab("Frequency (no. of days)")

print(pl)