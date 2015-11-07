week1 <- read.csv("week1.txt");
week2 <- read.csv("week2.txt");
week3 <- read.csv("week3.txt");
week4 <- read.csv("week4.txt");
week5 <- read.csv("week5.txt");
AllWeeks <- rbind(week1,week2,week3,week4,week5);

cat(" Data Size  : AllWeeks ",nrow(AllWeeks),"\n");
cat(" Data Size  : Week 1 ",nrow(week1),"\n");
cat(" Data Size  : Week 2 ",nrow(week2),"\n");
cat(" Data Size  : Week 3 ",nrow(week3),"\n");
cat(" Data Size  : Week 4 ",nrow(week4),"\n");
cat(" Data Size  : Week 5 ",nrow(week5),"\n");

clicks=table(week5$clicks);
cat("\nCLICKS\n")
print(clicks);



#pct <- round(clicks1/sum(clicks1)*100)
#lbls <- paste(names(clicks1))
#lbls <- paste(lbls, pct) # add percents to labels
#lbls <- paste(lbls,"%",sep="") # ad % to labels 
#pie(clicks1, labels = lbls, main="Pie Chart") 
#pclicks1=(clicks1/sum(clicks1))*100


