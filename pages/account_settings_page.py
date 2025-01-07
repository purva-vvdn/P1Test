import re
import time
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from locators import account_settings
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

from locators.account_settings import confirm_email


class Edit:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 60)

    # def clicking_on_create_account_button(self):
    #     self.wait.until(EC.element_to_be_clickable(edit_email_locators.create_another_account)).click()
    #
    # def enter_the_email(self, email):
    #     self.wait.until(EC.presence_of_element_located(edit_email_locators.email_address)).send_keys(email)
    #
    # def clicking_on_verify_email(self):
    #     self.wait.until(EC.element_to_be_clickable(edit_email_locators.confirm_email_address1)).click()
    #
    # def verifying_the_email(self, gmail):
    #     self.wait.until(EC.presence_of_element_located(edit_email_locators.confirm_email_address)).send_keys(gmail)
    #
    # def enter_name(self, name):
    #     self.wait.until(EC.presence_of_element_located(edit_email_locators.enter_name)).send_keys(name)
    #
    # def enter_last_name(self, last):
    #     self.wait.until(EC.presence_of_element_located(edit_email_locators.enter_last_name)).send_keys(last)
    #
    # def enter_password(self, password):
    #     self.wait.until(EC.presence_of_element_located(edit_email_locators.enter_password)).send_keys(password)
    #
    # def confirm_password(self, confirm):
    #     self.wait.until(EC.presence_of_element_located(edit_email_locators.confirm_password)).send_keys(confirm)
    #
    # def clicking_on_country(self):
    #     self.wait.until(EC.element_to_be_clickable(edit_email_locators.selecting_country)).click()
    #
    # def clicking_on_india(self):
    #     self.wait.until(EC.element_to_be_clickable(edit_email_locators.country_India)).click()
    #
    # def clicking_on_checkbox(self):
    #     self.wait.until(EC.element_to_be_clickable(edit_email_locators.clicking_on_checkbox)).click()
    #
    # def clicking_on_next(self):
    #     self.wait.until(EC.element_to_be_clickable(edit_email_locators.clicking_on_next)).click()

    def open_login_page(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'button_premium'))).click()
        for attempt in range(3):
            try:
                self.driver.find_element(account_settings.enter_username_locator)
                print("Username field to locate.")
                break
            except Exception as e:
                print(f"Attempt {attempt + 1}: Username field not found. Retrying...")
                try:
                    self.driver.find_element(By.ID, 'button_premium').click()
                    print(f"Retrying click on 'button_premium' (Attempt {attempt + 1})...")
                    time.sleep(6)
                except Exception as retry_exception:
                    print(f"Retry click failed on attempt {attempt + 1}: {retry_exception}")



    def enter_username(self, username):
        self.wait.until(EC.presence_of_element_located(account_settings.enter_username_locator)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.presence_of_element_located(account_settings.enter_password_locator)).send_keys(password)

    def clicking_on_sign_in(self):
        self.wait.until(EC.element_to_be_clickable(account_settings.click_on_login_locator)).click()
        time.sleep(2)

    def click_on_edit_profile_settings(self):
        self.wait.until(EC.invisibility_of_element_located(
        (By.CLASS_NAME, 'overlay-class')))
        element = self.wait.until(EC.element_to_be_clickable(account_settings.click_on_edit_profile))
        element.click()
        time.sleep(2)

    def clicking_on_update_profile(self):
        self.wait.until(EC.element_to_be_clickable(account_settings.click_on_update_profile)).click()
        print("waiting on edit screen")

    def clicking_on_cancel(self):
        self.wait.until(EC.element_to_be_clickable(account_settings.click_on_cancel)).click()
        time.sleep(2)


    def clicking_on_login_settings_button(self):
        self.wait.until(EC.element_to_be_clickable(account_settings.click_on_login_settings)).click()
        time.sleep(2)


    def clicking_on_changing_mail(self):
        self.wait.until(EC.element_to_be_clickable(account_settings.clicking_on_change_email)).click()
        time.sleep(2)

    def entering_current_email(self,email):
        self.wait.until(EC.element_to_be_clickable(account_settings.enter_email)).send_keys(email)
        time.sleep(2)

    def confirm_new_email_address(self,confirm_mail):
        self.wait.until(EC.element_to_be_clickable(account_settings.confirm_email)).send_keys(confirm_mail)
        time.sleep(2)


    def enter_current_password(self,current_password):
        self.wait.until(EC.element_to_be_clickable(account_settings.enter_password)).send_keys(current_password)
        time.sleep(2)

    def clicking_on_submit(self,):
        self.wait.until(EC.element_to_be_clickable(account_settings.submit_button)).click()
        time.sleep(2)

    def clicking_on_verify_your_email_in_popup(self):
        self.wait.until(EC.element_to_be_clickable(account_settings.clicking_on_verify_your_email)).click()
        time.sleep(2)

    def switching_to_new_window(self):
        self.driver.execute_script("window.open('https://yopmail.com/');")
        print("Opened a new window with Yopmail site")
        self.driver.switch_to.window(self.driver.window_handles[1])
        print("Switched to the Yopmail window")
        print("Current URL in the new window:", self.driver.current_url)

    def entering_yopmail_mail(self,yopmail):
        self.wait.until(EC.element_to_be_clickable(account_settings.entering_mail)).send_keys(yopmail)
        time.sleep(2)

    def clicking_on_arrow(self):
        self.wait.until(EC.element_to_be_clickable(account_settings.arrow_locator)).click()
        time.sleep(2)

    def clicking_on_netgear(self):
        self.driver.switch_to.frame("ifinbox")
        checkbox = self.driver.find_element(By.XPATH, '//span[text()="NETGEAR"]/../../..//input[@class="mc"]')
        assert checkbox.is_displayed(), "Checkbox is not visible"
        assert checkbox.is_enabled(), "Checkbox is not enabled"
        checkbox.click()
        self.driver.switch_to.default_content()
        time.sleep(3)
        self.driver.switch_to.frame("ifmail")
        self.wait.until(EC.element_to_be_clickable(account_settings.here_locator)).click()
        time.sleep(5)


    # def clicking_on_back_arrow(self):
    #     self.driver.switch_to.window(self.driver.window_handles[0])
    #     time.sleep(2)
    #     self.wait.until(EC.element_to_be_clickable(edit_email_locators.back_arrow_locator)).click()
    #     time.sleep(2)

    def clicking_on_done(self):
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(account_settings.done_locator)).click()
        time.sleep(2)

    def clicking_on_double_verify(self):
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(account_settings.double_verify)).click()
        time.sleep(2)

    def clicking_on_resend_email(self):
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(account_settings.resend_email)).click()
        time.sleep(2)

    def clicking_on_refresh(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(account_settings.refresh_locator)).click()
        time.sleep(7)

    def get_otp_from_the_target_page(self, mobile_num):
        self.driver.get("https://quackr.io/temporary-numbers/france/{}".format(mobile_num))
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'INSIGHT')]")))
        time.sleep(2)
        elements = self.driver.find_elements(By.XPATH, '//span[text()="Message"]/../..//p[@style="word-break: break-all;"]')
        s = None
        otps = []
        for my_str in elements:
            if 'INSIGHT' in my_str.text:
                otpMatch = re.search(r"\b\d{6}\b", my_str.text)
                if otpMatch:
                    otps.append(otpMatch.group())

        # Return the latest OTP
        if otps:
            latest_otp = otps[0]  # The last OTP in the list
            print("All OTPs:", otps)
            print("Latest OTP:", latest_otp)
            self.driver.quit()
            return latest_otp
        else:
            print("No OTP found.")
            self.driver.quit()
            return None

    def clicking_on_cancel_button_landing(self):
        self.wait.until(EC.element_to_be_clickable(account_settings.clicking_on_cancel_button)).click()
        time.sleep(2)


    def clicking_on_change_password_button(self):
        self.wait.until(EC.element_to_be_clickable(account_settings.change_password_button)).click()
        time.sleep(2)

    def entering_old_password(self,oldpassword):
        self.wait.until(EC.element_to_be_clickable(account_settings.input_old_password)).send_keys(oldpassword)
        time.sleep(2)

    def entering_new_password(self,newpassword):
        self.wait.until(EC.element_to_be_clickable(account_settings.input_new_password)).send_keys(newpassword)
        time.sleep(2)

    def entering_confirm_new_password(self,cnpassword):
        self.wait.until(EC.element_to_be_clickable(account_settings.input_confirm_new_password)).send_keys(cnpassword)
        time.sleep(2)

    def clicking_on_submit_locator(self):
        self.wait.until(EC.element_to_be_clickable(account_settings.submit_locator)).click()
        time.sleep(2)








