import csv
import matplotlib.pyplot as py
from scipy.stats.stats import pearsonr  


def csvTolist(fname):
	week=[];
	weekcsv = csv.reader(open(fname, 'rb'), delimiter=',');
	for line in weekcsv :
		week.append(line);
	return week[1:];

def col(mylist,i,integer):
	mycol=[];
	for row in mylist :
		if integer :
			mycol.append(int(row[i]));
		else :
			mycol.append(str(row[i]));
	return mycol;

def combine(weeks) :
	AllWeeks=[];
	for i in range(0,len(weeks)):
		AllWeeks.extend(weeks[i]);
	return AllWeeks;

def frequency(data,maxval):
	f=[data.count(x) for x in range(0,maxval+1)]
	return f;

def cfrequency(opens,clicks,maxval):
	nclicks=[];	
	for i in range(0,len(clicks)):
		if opens[i]>0 :
			nclicks.append(clicks[i])
	f=[nclicks.count(x) for x in range(0,maxval+1)]
	return f;

def same(str1,str2):
	if str(str1)==str(str2):	
		return 1 ;
	else :
		return 0;
def index(str1):
	if str(str1)==str("get_threads_highest_reputation_participants"):	
		return 2 ;
	else :
		if str(str1)==str("get_threads_most_popular") :
			return 1;
		else :
			return 0;

def clicked(opens,clicks,greetings,val) :
	if len(opens)!=len(clicks) or len(clicks)!=len(greetings) or len(opens)!=len(greetings) :
		print "Some Length Error Check Args\n"
		return 0;
	ctr = 0		
	for i in range(0,len(opens)) :
		if opens[i]>0 and clicks[i]>0 and greetings[i]==val :
			ctr=ctr+1;
	return ctr;		

def opened(opens,greetings,val) :
	if len(opens)!=len(greetings) :
		print "Some Length Error Check Args\n"
		return 0;
	ctr = 0		
	for i in range(0,len(opens)) :
		if opens[i]>0 and greetings[i]==val :
			ctr=ctr+1;
	return ctr;		

week1,week2,week3,week4,week5,AllWeeks=[], [], [] ,[] , [] ,[];

week1=csvTolist('week1.csv');
week2=csvTolist('week2.csv');
week3=csvTolist('week3.csv');
week4=csvTolist('week4.csv');
week5=csvTolist('week5.csv');
AllWeeks=combine([week1,week2,week3,week4,week5]);

print("\nLength of weekwise data :\nWeek1 "+str(len(week1))+"\nWeek2 "+str(len(week2))+"\nWeek3 "+str(len(week3))+"\nWeek4 "+str(len(week4))+"\nWeek5 "+str(len(week5)));
users=col(AllWeeks,0,False)

#<------------------------------------ OPENS ---------------------------------------------------->

#Get Time Wise Frequency for Opens  
maxOpens=max(col(AllWeeks,1,True));

opens1=col(week1,1,True);
freq1=frequency(opens1,maxOpens);
p1=[ (100*float(x)/sum(freq1)) for x in freq1];
print(p1);

opens2=col(week2,1,True);
freq2=frequency(opens2,maxOpens);
p2=[ (100*float(x)/sum(freq2)) for x in freq2];
print(p2);

opens3=col(week3,1,True);
freq3=frequency(opens3,maxOpens);
p3=[ (100*float(x)/sum(freq3)) for x in freq3];
print(p3);

opens4=col(week4,1,True);
freq4=frequency(opens4,maxOpens);
p4=[ (100*float(x)/sum(freq4)) for x in freq4];
print(p4);

opens5=col(week5,1,True);
freq5=frequency(opens5,maxOpens);
p5=[ (100*float(x)/sum(freq5)) for x in freq5];
print(p5);

#Weekwise No. of opens
print(sum(freq1[1:]));
print(sum(freq2[1:]));
print(sum(freq3[1:]));
print(sum(freq4[1:]));
print(sum(freq5[1:]));

#Weekwise Increase/Decrease No. of opens
#Weekwise Increase/Decrease in size
opens=[sum(freq1[1:]),sum(freq2[1:]),sum(freq3[1:]),sum(freq4[1:]),sum(freq5[1:])];
data_size=[len(week1),len(week2),len(week3),len(week4),len(week5)];
popens=[sum(p1[1:]),sum(p2[1:]),sum(p3[1:]),sum(p4[1:]),sum(p5[1:])];

print pearsonr(opens,data_size);
print pearsonr(popens,data_size);

delta_opens=[sum(freq2[1:])-sum(freq1[1:]),sum(freq3[1:])-sum(freq2[1:]),sum(freq4[1:])-sum(freq3[1:]),sum(freq5[1:])-sum(freq4[1:])];
delta_size=[len(week2)-len(week1),len(week3)-len(week2),len(week4)-len(week3),len(week5)-len(week4)];
print pearsonr(delta_opens,delta_size);

print pearsonr(delta_opens,data_size[1:5]);

#Weekwise %opens
print(sum(p1[1:]));
print(sum(p2[1:]));
print(sum(p3[1:]));
print(sum(p4[1:]));
print(sum(p5[1:]));

#<--------------------------------------------------- CLICKS -------------------------------------------------->

#Get Time Wise Frequency for Clicks
maxClicks=max(col(AllWeeks,2,True));

clicks1=col(week1,2,True);
freq1=cfrequency(opens1,clicks1,maxClicks);
p1=[ (100*float(x)/sum(freq1)) for x in freq1];
print(p1);

clicks2=col(week2,2,True);
freq2=cfrequency(opens2,clicks2,maxClicks);
p2=[ (100*float(x)/sum(freq2)) for x in freq2];
print(p2);

clicks3=col(week3,2,True);
freq3=cfrequency(opens3,clicks3,maxClicks);
p3=[ (100*float(x)/sum(freq3)) for x in freq3];
print(p3);

clicks4=col(week4,2,True);
freq4=cfrequency(opens4,clicks4,maxClicks);
p4=[ (100*float(x)/sum(freq4)) for x in freq4];
print(p4);

clicks5=col(week5,2,True);
freq5=cfrequency(opens5,clicks5,maxClicks);
p5=[ (100*float(x)/sum(freq5)) for x in freq5];
print(p5);

#Weekwise No. of clicks
print(sum(freq1[1:]));
print(sum(freq2[1:]));
print(sum(freq3[1:]));
print(sum(freq4[1:]));
print(sum(freq5[1:]));

#Weekwise %clicks
totalpopens1=sum(p1[1:]);
totalpopens2=sum(p2[1:]);
totalpopens3=sum(p3[1:]);
totalpopens4=sum(p4[1:]);
totalpopens5=sum(p5[1:]);

#No. of clicks %wise distribution if clicked

dist1=[ float(p1i)/totalpopens1 for p1i in p1[1:] ];
dist2=[ float(p2i)/totalpopens2 for p2i in p2[1:] ];
dist3=[ float(p3i)/totalpopens3 for p3i in p3[1:] ];
dist4=[ float(p4i)/totalpopens4 for p4i in p4[1:] ];
dist5=[ float(p5i)/totalpopens5 for p5i in p5[1:] ];

print(dist1);
print(dist2);
print(dist3);
print(dist4);
print(dist5);

print(sum(dist1[0:5]));
print(sum(dist2[0:5]));
print(sum(dist3[0:5]));
print(sum(dist4[0:5]));
print(sum(dist5[0:5]));

#Weekwise Increase/Decrease No. of opens
#Weekwise Increase/Decrease in size
clicks=[sum(freq1[1:]),sum(freq2[1:]),sum(freq3[1:]),sum(freq4[1:]),sum(freq5[1:])];
pclicks=[sum(p1[1:]),sum(p2[1:]),sum(p3[1:]),sum(p4[1:]),sum(p5[1:])];
print pearsonr(clicks,data_size);
print pearsonr(opens,clicks);

print pearsonr(pclicks,data_size);
print pearsonr(popens,pclicks);
print pearsonr(opens,pclicks);
print pearsonr(popens,clicks);


delta_clicks=[sum(freq2[1:])-sum(freq1[1:]),sum(freq3[1:])-sum(freq2[1:]),sum(freq4[1:])-sum(freq3[1:]),sum(freq5[1:])-sum(freq4[1:])];
print pearsonr(delta_clicks,delta_size);
print pearsonr(delta_clicks,delta_opens);
print pearsonr(delta_clicks,data_size[1:5]);

#<------------------------------------------------------------------- FEATURES ------------------------------------------------------------------------------------>

#<---------------------------GREETINGS-------------------------------------->

# TREATMENT DISTRIBUTION OVER WEEK FOR ALL WEEKS
temp=col(week1,3,False);
greetings1=[ same(str(x),str("prepare_social_greeting_html")) for x in temp ];
print(float(greetings1.count(0))/len(greetings1));

temp=col(week2,3,False);
greetings2=[ same(str(x),str("prepare_social_greeting_html")) for x in temp ];
print(float(greetings2.count(0))/len(greetings2));

temp=col(week3,3,False);
greetings3=[ same(str(x),str("prepare_social_greeting_html")) for x in temp ];
print(float(greetings3.count(0))/len(greetings3));

temp=col(week4,3,False);
greetings4=[ same(str(x),str("prepare_social_greeting_html")) for x in temp ];
print(float(greetings4.count(0))/len(greetings4));

temp=col(week5,3,False);
greetings5=[ same(str(x),str("prepare_social_greeting_html")) for x in temp ];
print(float(greetings5.count(0))/len(greetings5));

greetings=combine([greetings1,greetings2,greetings3,greetings4,greetings5]);
print(float(greetings.count(0))/len(greetings));

# clicks(if opened) depending on greetings
print("\nweek1\n")

print(float(len(opens1)-opens1.count(0))/len(opens1))
print(float(100*opened(opens1,greetings1,1))/(opened(opens1,greetings1,1)+opened(opens1,greetings1,0)))

print(float(100*clicked(opens1,clicks1,greetings1,1))/(clicked(opens1,clicks1,greetings1,1)+clicked(opens1,clicks1,greetings1,0)))
print(float(clicked(opens1,clicks1,greetings1,1)+clicked(opens1,clicks1,greetings1,0))/(len(opens1)-opens1.count(0)))
print(float(clicked(opens1,clicks1,greetings1,1)+clicked(opens1,clicks1,greetings1,0))/(len(clicks1)-clicks2.count(0)))

print("\nweek2\n")

print(float(len(opens2)-opens2.count(0))/len(opens2))
print(float(100*opened(opens2,greetings2,1))/(opened(opens2,greetings2,1)+opened(opens2,greetings2,0)))

print(float(100*clicked(opens2,clicks2,greetings2,1))/(clicked(opens2,clicks2,greetings2,1)+clicked(opens2,clicks2,greetings2,0)))
print(float(clicked(opens2,clicks2,greetings2,1)+clicked(opens2,clicks2,greetings2,0))/(len(opens2)-opens2.count(0)))
print(float(clicked(opens2,clicks2,greetings2,1)+clicked(opens2,clicks2,greetings2,0))/(len(clicks2)-clicks2.count(0)))

print("\nweek3\n")

print(float(len(opens3)-opens3.count(0))/len(opens3))
print(float(100*opened(opens3,greetings3,1))/(opened(opens3,greetings3,1)+opened(opens3,greetings3,0)))

print(float(100*clicked(opens3,clicks3,greetings3,1))/(clicked(opens3,clicks3,greetings3,1)+clicked(opens3,clicks3,greetings3,0)))
print(float(clicked(opens3,clicks3,greetings3,1)+clicked(opens3,clicks3,greetings3,0))/(len(opens3)-opens3.count(0)))
print(float(clicked(opens3,clicks3,greetings3,1)+clicked(opens3,clicks3,greetings3,0))/(len(clicks3)-clicks3.count(0)))

print("\nweek4\n")

print(float(len(opens4)-opens4.count(0))/len(opens4))
print(float(100*opened(opens4,greetings4,1))/(opened(opens4,greetings4,1)+opened(opens4,greetings4,0)))

print(float(100*clicked(opens4,clicks4,greetings4,1))/(clicked(opens4,clicks4,greetings4,1)+clicked(opens4,clicks4,greetings4,0)))
print(float(clicked(opens4,clicks4,greetings4,1)+clicked(opens4,clicks4,greetings4,0))/(len(opens4)-opens4.count(0)))
print(float(clicked(opens4,clicks4,greetings4,1)+clicked(opens4,clicks4,greetings4,0))/(len(clicks4)-clicks4.count(0)))

print("\nweek5\n")

print(float(len(opens5)-opens5.count(0))/len(opens5))
print(float(100*opened(opens5,greetings5,1))/(opened(opens5,greetings5,1)+opened(opens5,greetings5,0)))

print(float(100*clicked(opens5,clicks5,greetings5,1))/(clicked(opens5,clicks5,greetings5,1)+clicked(opens5,clicks5,greetings5,0)))
print(float(clicked(opens5,clicks5,greetings5,1)+clicked(opens5,clicks5,greetings5,0))/(len(opens5)-opens5.count(0)))
print(float(clicked(opens5,clicks5,greetings5,1)+clicked(opens5,clicks5,greetings5,0))/(len(clicks5)-clicks5.count(0)))

print("\nAllweeks\n")
opens=col(AllWeeks,1,True)
clicks=col(AllWeeks,2,True)

print(float(len(opens)-opens.count(0))/len(opens))
print(float(100*opened(opens,greetings,1))/(opened(opens,greetings,1)+opened(opens,greetings,0)))

print(float(100*clicked(opens,clicks,greetings,1))/(clicked(opens,clicks,greetings,1)+clicked(opens,clicks,greetings,0)))
print(float(clicked(opens,clicks,greetings,1)+clicked(opens,clicks,greetings,0))/(len(opens)-opens.count(0)))
print(float(clicked(opens,clicks,greetings,1)+clicked(opens,clicks,greetings,0))/(len(clicks)-clicks.count(0)))

#<-----------------------BODY--------------------------------> 

# TREATMENT DISTRIBUTION OVER WEEK FOR ALL WEEKS
temp=col(week1,4,False);
body1=[ same(str(x),str("prepare_social_greeting_html")) for x in temp ];
print(float(body1.count(0))/len(body1));

temp=col(week2,4,False);
body2=[ same(str(x),str("prepare_social_greeting_html")) for x in temp ];
print(float(body2.count(0))/len(body2));

temp=col(week3,4,False);
body3=[ same(str(x),str("prepare_social_greeting_html")) for x in temp ];
print(float(body3.count(0))/len(body3));

temp=col(week4,4,False);
body4=[ same(str(x),str("prepare_social_greeting_html")) for x in temp ];
print(float(body4.count(0))/len(body4));

temp=col(week5,4,False);
body5=[ same(str(x),str("prepare_social_greeting_html")) for x in temp ];
print(float(body5.count(0))/len(body5));

body=combine([body1,body2,body3,body4,body5]);
print(float(body.count(0))/len(body));

# clicks(if opened) depending on body
print("\nweek1\n")

print(float(len(opens1)-opens1.count(0))/len(opens1))
print(float(100*opened(opens1,body1,1))/(opened(opens1,body1,1)+opened(opens1,body1,0)))

print(float(100*clicked(opens1,clicks1,body1,1))/(clicked(opens1,clicks1,body1,1)+clicked(opens1,clicks1,body1,0)))
print(float(clicked(opens1,clicks1,body1,1)+clicked(opens1,clicks1,body1,0))/(len(opens1)-opens1.count(0)))
print(float(clicked(opens1,clicks1,body1,1)+clicked(opens1,clicks1,body1,0))/(len(clicks1)-clicks2.count(0)))

print("\nweek2\n")

print(float(len(opens2)-opens2.count(0))/len(opens2))
print(float(100*opened(opens2,body2,1))/(opened(opens2,body2,1)+opened(opens2,body2,0)))

print(float(100*clicked(opens2,clicks2,body2,1))/(clicked(opens2,clicks2,body2,1)+clicked(opens2,clicks2,body2,0)))
print(float(clicked(opens2,clicks2,body2,1)+clicked(opens2,clicks2,body2,0))/(len(opens2)-opens2.count(0)))
print(float(clicked(opens2,clicks2,body2,1)+clicked(opens2,clicks2,body2,0))/(len(clicks2)-clicks2.count(0)))

print("\nweek3\n")

print(float(len(opens3)-opens3.count(0))/len(opens3))
print(float(100*opened(opens3,body3,1))/(opened(opens3,body3,1)+opened(opens3,body3,0)))

print(float(100*clicked(opens3,clicks3,body3,1))/(clicked(opens3,clicks3,body3,1)+clicked(opens3,clicks3,body3,0)))
print(float(clicked(opens3,clicks3,body3,1)+clicked(opens3,clicks3,body3,0))/(len(opens3)-opens3.count(0)))
print(float(clicked(opens3,clicks3,body3,1)+clicked(opens3,clicks3,body3,0))/(len(clicks3)-clicks3.count(0)))

print("\nweek4\n")

print(float(len(opens4)-opens4.count(0))/len(opens4))
print(float(100*opened(opens4,body4,1))/(opened(opens4,body4,1)+opened(opens4,body4,0)))

print(float(100*clicked(opens4,clicks4,body4,1))/(clicked(opens4,clicks4,body4,1)+clicked(opens4,clicks4,body4,0)))
print(float(clicked(opens4,clicks4,body4,1)+clicked(opens4,clicks4,body4,0))/(len(opens4)-opens4.count(0)))
print(float(clicked(opens4,clicks4,body4,1)+clicked(opens4,clicks4,body4,0))/(len(clicks4)-clicks4.count(0)))

print("\nweek5\n")

print(float(len(opens5)-opens5.count(0))/len(opens5))
print(float(100*opened(opens5,body5,1))/(opened(opens5,body5,1)+opened(opens5,body5,0)))

print(float(100*clicked(opens5,clicks5,body5,1))/(clicked(opens5,clicks5,body5,1)+clicked(opens5,clicks5,body5,0)))
print(float(clicked(opens5,clicks5,body5,1)+clicked(opens5,clicks5,body5,0))/(len(opens5)-opens5.count(0)))
print(float(clicked(opens5,clicks5,body5,1)+clicked(opens5,clicks5,body5,0))/(len(clicks5)-clicks5.count(0)))

print("\nAllweeks\n")
opens=col(AllWeeks,1,True)
clicks=col(AllWeeks,2,True)

print(float(len(opens)-opens.count(0))/len(opens))
print(float(100*opened(opens,body,1))/(opened(opens,body,1)+opened(opens,body,0)))

print(float(100*clicked(opens,clicks,body,1))/(clicked(opens,clicks,body,1)+clicked(opens,clicks,body,0)))
print(float(clicked(opens,clicks,body,1)+clicked(opens,clicks,body,0))/(len(opens)-opens.count(0)))
print(float(clicked(opens,clicks,body,1)+clicked(opens,clicks,body,0))/(len(clicks)-clicks.count(0)))

#<-----------------------THREADS--------------------------------> 

# TREATMENT DISTRIBUTION OVER WEEK FOR ALL WEEKS
temp=col(week1,5,False);
threads1=[ index(str(x)) for x in temp ];
print(float(threads1.count(0))/len(threads1));
print(float(threads1.count(1))/len(threads1));
print(float(threads1.count(2))/len(threads1));

temp=col(week2,5,False);
threads2=[ index(str(x)) for x in temp ];
print(float(threads2.count(0))/len(threads2));
print(float(threads2.count(1))/len(threads2));
print(float(threads2.count(2))/len(threads2));

temp=col(week3,5,False);
threads3=[ index(str(x)) for x in temp ];
print(float(threads3.count(0))/len(threads3));
print(float(threads3.count(1))/len(threads3));
print(float(threads3.count(2))/len(threads3));

temp=col(week4,5,False);
threads4=[ index(str(x)) for x in temp ];
print(float(threads4.count(0))/len(threads4));
print(float(threads4.count(1))/len(threads4));
print(float(threads4.count(2))/len(threads4));

temp=col(week5,5,False);
threads5=[ index(str(x)) for x in temp ];
print(float(threads5.count(0))/len(threads5));
print(float(threads5.count(1))/len(threads5));
print(float(threads5.count(2))/len(threads5));

threads=combine([threads1,threads2,threads3,threads4,threads5]);
print(float(threads.count(0))/len(threads));
print(float(threads.count(1))/len(threads));
print(float(threads.count(2))/len(threads));


# clicks(if opened) depending on threads
print("\nweek1\n")

print(float(len(opens1)-opens1.count(0))/len(opens1))
print(float(100*opened(opens1,threads1,0))/(opened(opens1,threads1,1)+opened(opens1,threads1,0)+opened(opens1,threads1,2)))
print(float(100*opened(opens1,threads1,1))/(opened(opens1,threads1,1)+opened(opens1,threads1,0)+opened(opens1,threads1,2)))
print(float(100*opened(opens1,threads1,2))/(opened(opens1,threads1,1)+opened(opens1,threads1,0)+opened(opens1,threads1,2)))

print(float(100*clicked(opens1,clicks1,threads1,0))/(clicked(opens1,clicks1,threads1,1)+clicked(opens1,clicks1,threads1,0)+clicked(opens1,clicks1,threads1,2)))
print(float(100*clicked(opens1,clicks1,threads1,1))/(clicked(opens1,clicks1,threads1,1)+clicked(opens1,clicks1,threads1,0)+clicked(opens1,clicks1,threads1,2)))
print(float(100*clicked(opens1,clicks1,threads1,2))/(clicked(opens1,clicks1,threads1,1)+clicked(opens1,clicks1,threads1,0)+clicked(opens1,clicks1,threads1,2)))

print(float(clicked(opens1,clicks1,threads1,1)+clicked(opens1,clicks1,threads1,0)+clicked(opens1,clicks1,threads1,2))/(len(opens1)-opens1.count(0)))
print(float(clicked(opens1,clicks1,threads1,1)+clicked(opens1,clicks1,threads1,0)+clicked(opens1,clicks1,threads1,2))/(len(clicks1)-clicks1.count(0)))

print("\nweek2\n")

print(float(len(opens2)-opens2.count(0))/len(opens2))
print(float(100*opened(opens2,threads2,0))/(opened(opens2,threads2,1)+opened(opens2,threads2,0)+opened(opens2,threads2,2)))
print(float(100*opened(opens2,threads2,1))/(opened(opens2,threads2,1)+opened(opens2,threads2,0)+opened(opens2,threads2,2)))
print(float(100*opened(opens2,threads2,2))/(opened(opens2,threads2,1)+opened(opens2,threads2,0)+opened(opens2,threads2,2)))

print(float(100*clicked(opens2,clicks2,threads2,0))/(clicked(opens2,clicks2,threads2,1)+clicked(opens2,clicks2,threads2,0)+clicked(opens2,clicks2,threads2,2)))
print(float(100*clicked(opens2,clicks2,threads2,1))/(clicked(opens2,clicks2,threads2,1)+clicked(opens2,clicks2,threads2,0)+clicked(opens2,clicks2,threads2,2)))
print(float(100*clicked(opens2,clicks2,threads2,2))/(clicked(opens2,clicks2,threads2,1)+clicked(opens2,clicks2,threads2,0)+clicked(opens2,clicks2,threads2,2)))

print(float(clicked(opens2,clicks2,threads2,1)+clicked(opens2,clicks2,threads2,0)+clicked(opens2,clicks2,threads2,2))/(len(opens2)-opens2.count(0)))
print(float(clicked(opens2,clicks2,threads2,1)+clicked(opens2,clicks2,threads2,0)+clicked(opens2,clicks2,threads2,2))/(len(clicks2)-clicks.count(0)))

print("\nweek3\n")

print(float(len(opens3)-opens3.count(0))/len(opens3))
print(float(100*opened(opens3,threads3,0))/(opened(opens3,threads3,1)+opened(opens3,threads3,0)+opened(opens3,threads3,2)))
print(float(100*opened(opens3,threads3,1))/(opened(opens3,threads3,1)+opened(opens3,threads3,0)+opened(opens3,threads3,2)))
print(float(100*opened(opens3,threads3,2))/(opened(opens3,threads3,1)+opened(opens3,threads3,0)+opened(opens3,threads3,2)))

print(float(100*clicked(opens3,clicks3,threads3,0))/(clicked(opens3,clicks3,threads3,1)+clicked(opens3,clicks3,threads3,0)+clicked(opens3,clicks3,threads3,2)))
print(float(100*clicked(opens3,clicks3,threads3,1))/(clicked(opens3,clicks3,threads3,1)+clicked(opens3,clicks3,threads3,0)+clicked(opens3,clicks3,threads3,2)))
print(float(100*clicked(opens3,clicks3,threads3,2))/(clicked(opens3,clicks3,threads3,1)+clicked(opens3,clicks3,threads3,0)+clicked(opens3,clicks3,threads3,2)))

print(float(clicked(opens3,clicks3,threads3,1)+clicked(opens3,clicks3,threads3,0)+clicked(opens3,clicks3,threads3,2))/(len(opens3)-opens3.count(0)))
print(float(clicked(opens3,clicks3,threads3,1)+clicked(opens3,clicks3,threads3,0)+clicked(opens3,clicks3,threads3,2))/(len(clicks3)-clicks3.count(0)))

print("\nweek4\n")

print(float(len(opens4)-opens4.count(0))/len(opens4))
print(float(100*opened(opens4,threads4,0))/(opened(opens4,threads4,1)+opened(opens4,threads4,0)+opened(opens4,threads4,2)))
print(float(100*opened(opens4,threads4,1))/(opened(opens4,threads4,1)+opened(opens4,threads4,0)+opened(opens4,threads4,2)))
print(float(100*opened(opens4,threads4,2))/(opened(opens4,threads4,1)+opened(opens4,threads4,0)+opened(opens4,threads4,2)))

print(float(100*clicked(opens4,clicks4,threads4,0))/(clicked(opens4,clicks4,threads4,1)+clicked(opens4,clicks4,threads4,0)+clicked(opens4,clicks4,threads4,2)))
print(float(100*clicked(opens4,clicks4,threads4,1))/(clicked(opens4,clicks4,threads4,1)+clicked(opens4,clicks4,threads4,0)+clicked(opens4,clicks4,threads4,2)))
print(float(100*clicked(opens4,clicks4,threads4,2))/(clicked(opens4,clicks4,threads4,1)+clicked(opens4,clicks4,threads4,0)+clicked(opens4,clicks4,threads4,2)))

print(float(clicked(opens4,clicks4,threads4,1)+clicked(opens4,clicks4,threads4,0)+clicked(opens4,clicks4,threads4,2))/(len(opens4)-opens4.count(0)))
print(float(clicked(opens4,clicks4,threads4,1)+clicked(opens4,clicks4,threads4,0)+clicked(opens4,clicks4,threads4,2))/(len(clicks4)-clicks4.count(0)))

print("\nweek5\n")

print(float(len(opens5)-opens5.count(0))/len(opens5))
print(float(100*opened(opens5,threads5,0))/(opened(opens5,threads5,1)+opened(opens5,threads5,0)+opened(opens5,threads5,2)))
print(float(100*opened(opens5,threads5,1))/(opened(opens5,threads5,1)+opened(opens5,threads5,0)+opened(opens5,threads5,2)))
print(float(100*opened(opens5,threads5,2))/(opened(opens5,threads5,1)+opened(opens5,threads5,0)+opened(opens5,threads5,2)))

print(float(100*clicked(opens5,clicks5,threads5,0))/(clicked(opens5,clicks5,threads5,1)+clicked(opens5,clicks5,threads5,0)+clicked(opens5,clicks5,threads5,2)))
print(float(100*clicked(opens5,clicks5,threads5,1))/(clicked(opens5,clicks5,threads5,1)+clicked(opens5,clicks5,threads5,0)+clicked(opens5,clicks5,threads5,2)))
print(float(100*clicked(opens5,clicks5,threads5,2))/(clicked(opens5,clicks5,threads5,1)+clicked(opens5,clicks5,threads5,0)+clicked(opens5,clicks5,threads5,2)))

print(float(clicked(opens5,clicks5,threads5,1)+clicked(opens5,clicks5,threads5,0)+clicked(opens5,clicks5,threads5,2))/(len(opens5)-opens5.count(0)))
print(float(clicked(opens5,clicks5,threads5,1)+clicked(opens5,clicks5,threads5,0)+clicked(opens5,clicks5,threads5,2))/(len(clicks5)-clicks5.count(0)))

print("\nAllweeks\n")
opens=col(AllWeeks,1,True)
clicks=col(AllWeeks,2,True)

print(float(len(opens)-opens.count(0))/len(opens))
print(float(100*opened(opens,threads,0))/(opened(opens,threads,1)+opened(opens,threads,0)+opened(opens,threads,2)))
print(float(100*opened(opens,threads,1))/(opened(opens,threads,1)+opened(opens,threads,0)+opened(opens,threads,2)))
print(float(100*opened(opens,threads,2))/(opened(opens,threads,1)+opened(opens,threads,0)+opened(opens,threads,2)))

print(float(100*clicked(opens,clicks,threads,0))/(clicked(opens,clicks,threads,1)+clicked(opens,clicks,threads,0)+clicked(opens,clicks,threads,2)))
print(float(100*clicked(opens,clicks,threads,1))/(clicked(opens,clicks,threads,1)+clicked(opens,clicks,threads,0)+clicked(opens,clicks,threads,2)))
print(float(100*clicked(opens,clicks,threads,2))/(clicked(opens,clicks,threads,1)+clicked(opens,clicks,threads,0)+clicked(opens,clicks,threads,2)))

print(float(clicked(opens,clicks,threads,1)+clicked(opens,clicks,threads,0)+clicked(opens,clicks,threads,2))/(len(opens)-opens.count(0)))
print(float(clicked(opens,clicks,threads,1)+clicked(opens,clicks,threads,0)+clicked(opens,clicks,threads,2))/(len(clicks)-clicks.count(0)))

print("\nPearson\n")
print pearsonr(opens1,clicks1)
print pearsonr(opens1,greetings1)
print pearsonr(opens1,body1)
print pearsonr(opens1,threads1)
print pearsonr(clicks1,greetings1)
print pearsonr(clicks1,body1)
print pearsonr(clicks1,threads1)

