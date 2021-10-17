from pages.base_page import Base
from pages.contact_us import ContactUs
import pytest
from time import sleep
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.usefixtures('set_up')
class TestNegative(Base):
    @pytest.mark.parametrize('name', ['8ada', '@adsfa', ' '])
    def test_name(self, name):
        driver = self.driver
        contact = ContactUs(driver)
        contact.enter_name(name)
        contact.enter_email('adfa@test.com')
        contact.enter_telephone(456466)
        contact.submit_button()
        try:
            contact.show_name_error()
        except NoSuchElementException:
            print("Field error")

    @pytest.mark.parametrize('email, output', [('asdfas', '* Invalid email address'),
                                               ('adfa@', '* Invalid email address'),
                                               ('daf@fasd@test.com', '* Invalid email address'),
                                               ('adfg@test.', '* Invalid email address'),
                                               ('asdf.test.com', '* Invalid email address'),
                                               ('', '* This field is required\n* Invalid email address')
                                               ]
                             )
    def test_email(self, email, output):
        driver = self.driver
        contact = ContactUs(driver)
        contact.enter_name('susan')
        contact.enter_email(email)
        contact.enter_telephone(465464)
        contact.submit_button()
        sleep(3)
        assert contact.find_email_error().text == output

    @pytest.mark.parametrize('phone, output', [('asd', '* Invalid phone number'),
                                               ('5225', '* Invalid phone number'),
                                               ('5asdf', '* Invalid phone number'),
                                               (' ', '* This field is required\n* Invalid phone number'),
                                               ('', '* This field is required\n* Invalid phone number')

                                               ])
    def test_phone(self, phone, output):
        driver = self.driver
        contact = ContactUs(driver)
        contact.enter_name('Susan')
        contact.enter_email('ada@test.com')
        contact.enter_telephone(phone)
        contact.submit_button()
        sleep(3)
        try:
            assert contact.find_phone_error().text == output
        except NoSuchElementException:
            print('Field error')

    @pytest.mark.parametrize('message',
                             [("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
                               Ipsum has been the industry's standard Ipsum has been the Ipsum has """),
                              ("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
                               as been the industry's standard dummy text ever since the 1500s, when an unknown """),
                              ("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
                               has been the industry's standard dummy text ever since the 1500s, when an unknown
                               prinnly fivafggfhfgh"""),
                              ""
                              ])
    def test_message(self, message):
        driver = self.driver
        contact = ContactUs(driver)
        contact.enter_message(message)
        contact.submit_button()

        try:
            assert len(message) <= 180

        except:
            print("Field error - Message cannot have more than 180 characters")
