import splinter
import time
##開啟瀏覽器
browser = splinter.Browser(driver_name='chrome')
browser.driver.set_window_size(1680, 1050)
m = 7	##月
d = 1	##天數
w = 1	##第幾個禮拜
w_count = 2		##一個禮拜的第幾天
data_time = 1060801		##輸出檔案名稱
while True:
	browser.visit('https://www.evaair.com/zh-tw/index.html')	##長榮航空
	time.sleep(1)
	browser.click_link_by_id("home_tab0")	##點網路購票

	
	browser.fill("txt_To","KIX")	##輸入大阪
	time.sleep(1)

	
	kix = browser.find_by_text("大阪 - KIX")	##尋找大阪選項
	time.sleep(2)
	kix.click()

	browser.click_link_by_id("lit_date1")	##點選行程日期

	
	clear = browser.find_by_text("清除")	##清除日期資訊
	clear.click()

	##選擇月
	date = browser.find_by_xpath('//*[@id="datepickers-container"]/div[1]/nav/button')
	date.click()
	
	## 換成9月
	if d > 31 and m == 7:
		m += 1
		d = 5
		w_count = 5
		w = 1
	##選月 8月m=7 9月m=8
	browser.click_link_by_id("date-month-"+str(m))
	d += 1
	time.sleep(1)

	##7天就到下個禮拜
	if w_count > 7:
		w += 1
		w_count = 1
	
	##去程
	day = browser.find_by_xpath('//*[@id="datepickers-container"]/div[1]/div[2]/table/tbody/tr['+str(w)+']/td['+str(w_count)+']')
	print(str(w)+str(d)+str(w_count))
	day.click()

	##回程
	backday = browser.find_by_xpath('//*[@id="datepickers-container"]/div[1]/div[2]/table/tbody/tr['+str(w)+']/td['+str(w_count)+']')
	backday.click()
	
	w_count += 1	##一個禮拜的第幾天
	
	ok = browser.find_by_text("完成")	##完成時間選擇
	ok.click()
	
	browser.click_link_by_id("lit_ok")	##開始搜尋
	time.sleep(10)
	# Taipei_KIX = browser.find_by_xpath('//*[@id="tpl4_bound0-bound-table"]')

	# for T_K in Taipei_KIX:
	#     print(T_K.text)

	# KIX_Taipei = browser.find_by_xpath('//*[@id="availability-bound-1"]')

	# for K_T in KIX_Taipei:
	#     print(K_T.text)
	
	print("[INFO] crawling "+str(data_time))
	with open('D:/test/{}.html'.format(str(data_time)),'w',encoding="utf-8") as f:
		f.write(browser.html)

	if data_time == 1060831:
		data_time = 1060900
	data_time += 1
	
	##8/31跳出
	if m == 8 and d == 35:
			break


