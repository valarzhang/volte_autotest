from selenium import webdriver

# 创建浏览器对象
driver = webdriver.Chrome()

# 访问地址
web_url = 'http://www.baidu.com'

# 打开浏览器
driver.get(web_url)


'''
八大元素定位法则：
1、id，基于元素属性中id的值来进行定位
    id类似于人们身份证号码，一般不会重复
2、name，基于元素属性中name的值来进行定位
    类似于身份证上的名字，可能会有重复
3、link text，主要用于超链接进行定位
4、partial link text，link text的模糊查询，类似于数据库中的like %
5、classname，基于元素样式定位，非常容易重复，不支持多个classname同时定位
6、tagname，标签名定位，重复度高，一般在二次定位的时候使用
7、cssselector，应用相对较多，最初IE不支持xpath，完全基于class属性定位
8、xpath，目前应用最多，基于页面结构进行定位
    绝对路径：
    相对路径：
        //*[@id="kw"]     //input[contains(@id,'kw'] contains表示模糊查找   //input[contains(text(),'搜索')]
        
        //表示从根路径
        * 任意标签
        [] 表示筛选条件
        @ 表示基于属性，@id="kw"表示id属性为kw的
        //a[text()="登录"]
        基于文本内容进行查找
        无法直接定位元素时，可以通过定位子集来获取父级
        //a[text()="登录"]/..
'''

# 基于id定位
driver.find_element_by_id('id')

# 基于name定位
driver.find_element_by_class_name('name')

# 基于link text定位
driver.find_element_by_link_text('').click()

# 基于partial link text定位
driver.find_element_by_partial_link_text('').click()
driver.find_elements_by_partial_link_text('')[1].click()
drs = driver.find_elements_by_partial_link_text('')
for dr in drs:
    print(dr.text)
# 基于classname属性定位
driver.find_element_by_class_name('').send_keys('百度')

# 基于cssselector定位
driver.find_element_by_css_selector('')

# 基于xpath定位
driver.find_element_by_xpath('')



# driver.quit()
