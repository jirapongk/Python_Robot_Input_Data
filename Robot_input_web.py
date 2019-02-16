from selenium import webdriver

# Using Chrome to access web
driver = webdriver.Chrome()
# Open the website
driver.get('https://10.9.92.91:1443/login_ipas/login.html')

# Select the login box
login_box = driver.find_element_by_id('i_user')

# Send login information
login_box.send_keys('K_JIRAPONG')

# Select the login password box
login_pass_box = driver.find_element_by_id('i_password')

# Send login password information
login_pass_box.send_keys('password')

# Find login button
login_button = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/form[1]/div[1]/input[1]")
# Click login
login_button.click()

driver.implicitly_wait(30) # seconds

# Find Merchant Service Workbench
login_button = driver.find_element_by_xpath("/html[1]/body[1]/form[1]/div[4]/div[2]/div[3]/div[5]/div[4]/div[1]/ul[1]/li[1]/ul[1]/li[2]/ul[1]/li[3]/div[1]/span[1]")
# Click Merchant Service Workbench
login_button.click()

# Find Close Tab
login_button = driver.find_element_by_class_name("rwCloseButton")

# Click Merchant Service Workbench
login_button.click()

# Find Create
login_button = driver.find_element_by_xpath("/html[1]/body[1]/form[1]/div[5]/div[2]/div[3]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]/span[1]/span[1]/span[1]/span[1]")
# Click Create
login_button.click()


driver.implicitly_wait(30) # seconds

