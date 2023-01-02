import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import chromedriver_binary  # Adds chromedriver binary to path
from bs4 import BeautifulSoup
def get_result_table(result_html):
    soup = BeautifulSoup(result_html,'lxml')#
    x=str(soup.find('table','ntable'))#
    result_table = pd.read_html(x)[0]#
    ##
    company_name=result_table[result_table[2]=='企业名称'][3].values[0]
    company_size=result_table[result_table[0]=='人员规模'][1].values[0]
    book_value=result_table[result_table[0]=='注册资本'][1].values[0]
    company_type=result_table[result_table[0]=='企业类型'][1].values[0]
    company_field=result_table[result_table[0]=='所属行业'][1].values[0]
    company_area=result_table[result_table[0]=='经营范围'][1].values[0]
    open_data=result_table[result_table[0]=='成立日期'][5].values[0]
    columns=['企业名称','人员规模','注册资本','企业类型','所属行业','经营范围','成立日期']
    result=pd.DataFrame([[company_name,company_size,book_value,company_type,company_field,company_area,open_data]],columns)
    return result


option = webdriver.ChromeOptions()
option.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36')
driver = webdriver.Chrome(options=option)
driver.implicitly_wait(5)
driver.get('https://www.qcc.com/')
driver.maximize_window()

text_lable = driver.find_element(By.ID, 'searchKey')
text_lable.clear()
text_lable.send_keys('宝山钢铁')
time.sleep(1)
button = driver.find_element(By.CLASS_NAME, 'input-group-btn')  # 搜索按钮
button.click()

try:
    results = driver.find_element(By.XPATH, '//*[@class="maininfo"]/div[1]/span[1]')
    results.click()
    driver.switch_to.window(driver.window_handles[-1])  # 切换页面
    # print(driver.page_source)#页面html
    result_table = get_result_table(driver.page_source)
    # final_result=final_result.append(result_table)
    # driver.close()
except:
    print('Error')


get_result_table(driver.page_source)