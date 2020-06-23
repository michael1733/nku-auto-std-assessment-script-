from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
import numpy as np

#需要互评的同学假设有100位，便创建一个0到99的列表[0,1,2,...,99]作为学生名单的索引。
# 若你已经评价过某位同学，say,第32位(列表中的索引是31)，那么这个ind列表就应该删去元素31
std_number = input('需要互评的学生数量')
ind = np.arange(std_number)

#每位同学都是一个评价
text1 = '我和这位同学很熟悉，我们常在一起讨论学习，我认为思维敏捷，积极好学是这位同学最大的优点！'
text2 = '在我们相处的生涯中，我觉得该同学没有缺点。这话听起来可能很夸张，可是确实是我的发自肺腑之言。希望这名同学能够再接再厉，前途似锦！'



b = webdriver.Ie()#辅学网站在我电脑上有个bug,只能用ie登录vpn（easy connect），不然会提示我学号密码错错误。
b.implicitly_wait(30)

std_id = input('学号')
std_password = input('登录vpn的密码')#默认该密码也会用于辅学网页登陆

b.get("https://vpn.nankai.edu.cn/por/login_psw.csp?rnd=0.35051682764342595#https%3A%2F%2Fvpn.nankai.edu.cn%2F")

            
user = b.find_element_by_id('svpn_name')
password = b.find_element_by_id('svpn_password')
login_button = b.find_element_by_id('logButton')

user.send_keys(std_id)
password.send_keys(std_password)
login_button.click()

time.sleep(15)#ie游览器太慢，常会因为加载时间过长使得程序无法正常进行





b.get('fuxue.nankai.edu.cn')

id=b.find_element_by_name('username')
pa=b.find_element_by_id('password1')

yan_zheng = input('验证码')#验证码暂时没法自动填写，but I have a plan.
yan_zheng_ma = b.find_element_by_class_name('login_input2')



id.send_keys(std_id)
pa.send_keys(std_password)
yan_zheng_ma.send_keys(yan_zheng)

b.find_element_by_class_name('loginin').click()
b.find_element_by_partial_link_text('评估班会').click()

class_list=b.find_elements_by_partial_link_text('进入班会')
class_list[0].click()


for i in ind:
    std_list = b.find_elements_by_partial_link_text('互评')#这个表每次都会变
    std = std_list[i]
    std.click()
    bars = b.find_elements_by_class_name('clickable-dummy')#那些拖动条的全体，全部打六分
    for bar in bars:
        bar.click()
    b.find_element_by_name('goodcon').send_keys(text1)
    b.find_element_by_name('badcon').send_keys(text2)
    sub = b.find_element_by_name('submit').click()
    time.sleep(1)
    
    
    

    



