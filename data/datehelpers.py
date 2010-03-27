import datetime
def check_date(dat,inc=True):
	r=False
	now=datetime.datetime.now()
	y=dat[0]
	m=dat[1]
	if inc:
		m+=1
	d=dat[2]
	if y<now.year: y=now.year
	if y==now.year:
		if m<now.month: m=now.month
		if m==now.month:
			if d<now.day: d=now.day
			if d==now.day: r=True
	newdat=(y,m,d)
	try:
		newdat=newdat+(dat[3],dat[4])
	except:
		pass
	return newdat,r
	
def check_time(hours,minutes):
	now=datetime.datetime.now()
	if hours<now.hour:hours=now.hour
	if hours==now.hour:
		if minutes<now.minute: minutes=now.minute+1
	return hours,minutes
	
def time_to_tuple(dat):
	dat=str(dat)
	dat=dat.replace(" ","")
	dat=dat.replace("(","")
	dat=dat.replace(")","")
	dat=dat.split(",")
	datl=dat
	dat=()
	for i in datl:
		a=int(i)
		dat=dat+(a,)
	return dat
	
