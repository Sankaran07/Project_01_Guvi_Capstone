from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver = webdriver.Chrome()

driver.get(url)

driver.maximize_window()

sleep(2)

webelement_of_email_input = driver.find_element(By.XPATH, '//input[@name="username"]')
webelement_of_email_input.send_keys("Admin")



webelement_of_password_input = driver.find_element(By.XPATH, '//input[@type="password"]')
webelement_of_password_input.send_keys("admin123")

sleep(3)

webelement_of_login_button = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--main orangehrm-login-button"]')
webelement_of_login_button.click()

sleep(3)
print("The user is logged in successfully.")

pim_lable = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span')
pim_lable.click()
# print("PIM_clicked")
sleep(3)

pim_edit_employee = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]')
pim_edit_employee.click()
# print("pim_edit_employee")
sleep(3)

emplyee_other_id = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input')
emplyee_other_id.send_keys("659")
# print('emplyee_other_id')
sleep(2)

emplyee_driver_number = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')
emplyee_driver_number.send_keys("8798")
# print('emplyee_driver_number')
sleep(2)


save_a_employee = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button')
save_a_employee.click()
print('The user should be able to edit an existing employee information in the PIM and should see a message for successful employee details addition.')
sleep(5)