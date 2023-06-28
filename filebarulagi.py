
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_sign_up(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.demoblaze.com/") # buka situs
        driver.find_element(By.ID,"signin2").click() # klik tombol Sign Up
        driver.find_element(By.ID,"sign-username").send_keys("mawar") # isi username
        driver.find_element(By.ID,"sign-password").send_keys("inipassword") # isi password
        driver.find_element(By.CLASS_NAME, "btn btn-primary").click()

        # validasi
        #response_data = driver.find_element(By.CLASS_NAME,"title").text
        #self.assertIn('PRODUCTS', response_data)
 
    def test_a_success_log_in(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.demoblaze.com/") # buka situs
        driver.find_element(By.ID,"login2").click() # klik tombol Log In
        driver.find_element(By.ID,"loginusername").send_keys("mawar") # isi username
        driver.find_element(By.ID,"loginpassword").send_keys("inipassword") # isi password
        driver.find_element(By.CLASS_NAME, "btn btn-primary").click()

        # validasi
        #response_data = driver.find_element(By.CLASS_NAME,"title").text
        #self.assertIn('PRODUCTS', response_data)

    def test_place_order_from_cart(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.demoblaze.com") # buka situs
        driver.find_element(By.CLASS_NAME, "hrefch").click() # klik produk
        driver.find_element(By.CLASS_NAME,"btn btn-success btn-lg").click() # masukin ke cart
        driver.find_element(By.ID, "cartur").click() # cek isi cart
        driver.find_element(By.CLASS_NAME, "btn btn-success").click() #pesan barang di cart

    def test_a_success_log_out(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.demoblaze.com/") # buka situs
        driver.find_element(By.ID,"logout2").click() # klik tombol Log Out
        
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()
