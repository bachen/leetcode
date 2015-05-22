from selenium import webdriver
import threading,time

usrs = [u'cc0001@163.com',u'cc0002@163.com']
pwd = u'111111'

def login1(usr,pwd):
	dr = webdriver.Chrome()
	dr.maximize_window()
	dr.get("http://test.ximalaya.com/passport/login")
	time.sleep(2)
	dr.find_element_by_id('userAccount').send_keys(usr)
	dr.find_element_by_id('userPwd').send_keys(pwd)
	dr.find_element_by_id('login_btn').click()
	time.sleep(4)
	print "%s login successfully." % usr
	dr.quit()

def login2(usr,pwd):
	dr = webdriver.Chrome()
	dr.maximize_window()
	dr.get("http://test.ximalaya.com/passport/login")
	time.sleep(2)
	dr.find_element_by_id('userAccount').send_keys(usr)
	dr.find_element_by_id('userPwd').send_keys(pwd)
	dr.find_element_by_id('login_btn').click()
	time.sleep(4)
	print "%s login successfully." % usr
	dr.quit()

threads = []
t1 = threading.Thread(target=login1,args=(usrs[1],pwd))
threads.append(t1)
t2 = threading.Thread(target=login2,args=(usrs[0],pwd))
threads.append(t2)

if __name__ == "__main__":
	for t in threads:
		t.setDaemon(True)
		t.start()

	t.join()
	print "threads over."