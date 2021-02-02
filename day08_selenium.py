# # selenium module import
# from selenium import webdriver
# import time

# # running chrome physical driver 
# driver = webdriver.Chrome("D:\\Coding\\itbank-python_basic\\py1530\\chromedriver.exe")

# # site move
# driver.get("https://naver.com")

# # using variable for selenium
# webtoon_btn = driver.find_element_by_xpath('//*[@id="NM_FAVORITE"]/div[1]/ul[2]/li[9]/a')
# time.sleep(1)
# webtoon_btn.click()
# print(type(webtoon_btn))

# # using method in directly without variable
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="snb_wrap"]/h1/a[1]').click()
# driver.find_element_by_xpath('//*[@id="query"]').send_keys('python')
# driver.find_element_by_xpath('//*[@id="search_btn"]').click()


from selenium import webdriver
import time

driver = webdriver.Chrome(r"D:\Coding\itbank-python_basic\py1530\chromedriver.exe")
driver.get("https://naver.com")

driver.find_element_by_xpath('//*[@id="NM_NEWSSTAND_HEADER"]/div[2]/a[1]').click()
time.sleep(1)

for i in range(1, 6):
    time.sleep(1)
    driver.find_element_by_xpath(f'//*[@id="_rankingList0"]/li[{i}]/div/div/div/a[1]').click()
    time.sleep(2)
    driver.back()


