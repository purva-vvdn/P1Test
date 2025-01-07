import time

import pytest
from time import sleep

from locators.create_account_locators import email_address
from pages.account_settings import account_settings
from pages.account_settings import Edit



@pytest.mark.usefixtures("setup")
class TestEdit:
    def test_to_verify_the_change_in_password(self):
        edit_driver = Edit(self.driver)
        edit_driver.open_login_page()
        edit_driver.enter_username('unique56@yopmail.com')
        edit_driver.enter_password('Sak@1406')
        edit_driver.clicking_on_sign_in()
        edit_driver.click_on_edit_profile_settings()
        edit_driver.clicking_on_update_profile()
        edit_driver.clicking_on_login_settings_button()
        edit_driver.clicking_on_change_password_button()
        edit_driver.entering_old_password('Sak@1406')
        edit_driver.entering_new_password('Sak@1421')
        edit_driver.entering_confirm_new_password('Sak@1421')
        edit_driver.clicking_on_submit_locator()
        time.sleep(10)