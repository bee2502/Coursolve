import csv
from itertools import groupby

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
			mycol.append(row[i]);
	return mycol;

def combine(weeks) :
	AllWeeks=[];
	for i in range(0,len(weeks)):
		AllWeeks.extend(weeks[i]);
	return AllWeeks;

def frequency(data,maxval):
	f=[data.count(x) for x in range(0,maxval+1)]
	return f;


week1,week2,week3,week4,week5,AllWeeks=[], [], [] ,[] , [] ,[];
week1=csvTolist('week1.csv');
week2=csvTolist('week2.csv');
week3=csvTolist('week3.csv');
week4=csvTolist('week4.csv');
week5=csvTolist('week5.csv');
AllWeeks=combine([week1,week2,week3,week4,week5]);

#Get Time Wise Frequency
maxOpens=max(col(AllWeeks,2,True));

opens1=col(week1,2,True);
freq1=frequency(opens1,maxOpens);
p1=[ (100*float(x)/sum(freq1)) for x in freq1];
print(p1);

opens2=col(week2,2,True);
freq2=frequency(opens2,maxOpens);
p2=[ (100*float(x)/sum(freq2)) for x in freq2];
print(p2);



