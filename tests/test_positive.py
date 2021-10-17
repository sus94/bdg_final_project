import pytest
from pages.contact_us import ContactUs
from time import sleep
from pages.base_page import Base
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.usefixtures('set_up')
class TestPositive(Base):
    def test_submit(self):
        driver = self.driver
        contact = ContactUs(driver)
        contact.enter_name('Susan')
        contact.enter_email('susan@test.com')
        contact.enter_telephone(4564646)
        contact.submit_button()
        success_message = contact.show_success_message()
        sleep(3)
        try:
            assert success_message.text == "Feedback has been sent to the administrator"
        except NoSuchElementException:
            print('Field error')


@pytest.mark.parametrize('get_func1, output', [(ContactUs.get_name, ''), (ContactUs.get_email, ''),
                                               (ContactUs.get_telephone, ''), (ContactUs.get_country, ''),
                                               (ContactUs.get_company, ''), (ContactUs.get_message, '')])
def test_clear_button(self, get_func1, output):
    driver = self.driver
    contact = ContactUs(driver)
    contact.enter_name('Susan')
    contact.enter_email('ada@test.com')
    contact.enter_telephone(78787)
    contact.enter_country('8648')
    contact.enter_company('Company name')
    contact.enter_message('Some message here')
    contact.clear_fields()
    sleep(3)
    assert get_func1(contact) == output
