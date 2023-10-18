import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestFlaskWebsite:

    @pytest.mark.parametrize('homeUrl,username,password',[('http://localhost:5003','username1','password1')])
    def test_site_login_success(self,homeUrl,username,password):
        driver = webdriver.Chrome()
        driver.get(homeUrl)
        WebDriverWait(driver,10).until(lambda p : p.find_element(By.LINK_TEXT, '登录').is_display())

        driver.find_element(By.LINK_TEXT,'登陆').click()

        driver.find_element(By.NAME, 'username').send_keys(username)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='登录']").click()

        assert driver.find_element(By.ID,'user').text==username
        assert len(driver.find_element(By.LINK_TEXT, '登出'))==1

        driver.quit()

    @pytest.mark.parametrize('homeUrl,errUsername,errPassword',[("http://localhost:5003","errorUser1","errorPassword1")])
    def test_site_login_fail(self,homeUrl,errUsername,errPassword):
        driver=webdriver.Chrome()
        driver.get(homeUrl)
        WebDriverWait(driver,10).until(lambda p :p.find_element(By.LINK_TEXT,'登录').is_display())

        driver.find_element(By.LINK_TEXT,'登陆').click()

        driver.find_element(By.NAME, 'username').send_keys(errUsername)
        driver.find_element(By.NAME, 'password').send_keys(errPassword)
        driver.find_element(By.XPATH, "//button[text()='登录']").click()

        assert driver.find_element(By.TAG_NAME,'h4').text=='用户名或密码错误！'

        driver.quit()


