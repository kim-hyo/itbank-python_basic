from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import time

file_path = "D:\\Coding\\itbank-python_basic\\py1530\\"
file_name = "aladin_bestseller" + "-" + str(datetime.today().year) + "-" + str(datetime.today().month) + "-" + str(datetime.today().day)

driver = webdriver.Chrome(file_path+"chromedriver.exe")
driver.get("https://www.aladin.co.kr")
rank = 1

def aladin_crawling(best_seller_div):
    global rank  # using global variable

    for i in best_seller_div:
        # 증정품이 있는 책과 없는 책의 구분자 "["
        if i.find_all("li")[0].text[0] == "[":
            book_title = i.find_all("li")[1].text
            book_origin = str(i.find_all("li")[2].text).split(' | ')            
            book_author = book_origin[0].strip()
            book_publisher = book_origin[1].strip()
            published_date = book_origin[2].strip()
            book_price = str(i.find_all("li")[3].text).split(",  ")[0]            
        else:        
            book_title = i.find_all("li")[0].text
            book_origin = str(i.find_all("li")[1].text).split(' | ')            
            book_author = book_origin[0].strip()
            book_publisher = book_origin[1].strip()
            published_date = book_origin[2].strip()    
            book_price = str(i.find_all("li")[2].text).split(",  ")[0]     

        f.write(f"Rank: {rank}\n")
        f.write(f"Book Title: {book_title}\n")
        f.write(f"Book Author: {book_author}\n")
        f.write(f"Book Publisher: {book_publisher}\n")
        f.write(f"Published date of Book: {published_date}\n")
        f.write(f"Book Price: {book_price}\n")
        f.write("-" * 70 + "\n")
        rank += 1       


try:
    f = open(file_path+file_name, "a", encoding="UTF-8")
    for i in range(1, 9):
        driver.get(f"https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=0&page={i}&cnt=1000&SortOrder=1")
        time.sleep(1)

        # selenium으로 현재 페이지의 html 소스 코드 가져오기
        source = driver.page_source
        bs = BeautifulSoup(source, "html.parser")
        best_seller_div = bs.find_all("div", class_="ss_book_box")        

        aladin_crawling(best_seller_div)

except:
    print("can't open file or error is occured")

finally:
    f.close()




