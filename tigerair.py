import time
import threading
class myThread (threading.Thread):
	def __init__(self, threadID,year,mon,day):
		
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.year = year
		self.mon = mon
		self.day = day
	def run (self):
		crawlerchina(self.year,self.mon,self.day)
    

def crawlerchina(year,mon,day):
	import requests
	y = year
	m = mon
	d = day
	rs = requests.session()
	while True:
		url = "https://tiger-wkgk.matchbyte.net/wkapi/v1.0/flightsearch?adults=1&children=0&infants=0&originStation=TPE&originStation=KIX&destinationStation=KIX&destinationStation=TPE&departureDate="+str(y)+"-"+str(m)+"-"+str(d)+"&departureDate="+str(y)+"-"+str(m)+"-"+str(d)+"&includeoverbooking=false&daysBeforeAndAfter=4&locale=en-US"
		res = rs.get(url)

		# print("[INFO] crawling ")
		if len(str(m)) == 1 and len(str(d)) == 1:
			with open('D:/test/tigerair/tigerair'+str(y)+"0"+str(m)+"0"+str(d)+'.json','w') as f:
				f.write(res.text)
			print(str(y)+"0"+str(m)+"0"+str(d))
		elif len(str(m)) == 1:
			with open('D:/test/tigerair/tigerair'+str(y)+"0"+str(m)+str(d)+'.json','w') as f:
				f.write(res.text)
			print(str(y)+"0"+str(m)+str(d))
		elif len(str(d)) == 1:
			with open('D:/test/tigerair/tigerair'+str(y)+str(m)+"0"+str(d)+'.json','w') as f:
				f.write(res.text)
			print(str(y)+str(m)+"0"+str(d))
		else:
			with open('D:/test/tigerair/tigerair'+str(y)+str(m)+str(d)+'.json','w') as f:
				f.write(res.text)
			print(str(y)+str(m)+str(d))
		if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
			if d == 31:
				d = 0
				m += 1
		if m == 4 or m == 6 or m == 9 or m == 11:
			if d == 30:
				d = 0
				m += 1
		if m == 2 and d == 28:
			d = 0
			m += 1
		d += 1
		if m == 4 or m == 7 or m == 10 or m == 1:
			if d == 1:
				break
		time.sleep(5)
if __name__ == '__main__':
	start_time = time.time()
	thread1 = myThread(1, 2017, 1, 1)
	thread2 = myThread(2, 2017, 4, 1)
	thread3 = myThread(3, 2017, 7, 1)
	thread4 = myThread(4, 2017, 10, 1)
	# y = 2017
	# m = 8
	# d = 1
	try:
		thread1.start()
		thread2.start()
		thread3.start()
		thread4.start()
		end_time = time.time()
		print("spend " + str((end_time-start_time)/60) + " min")
	except:
		pass


	















