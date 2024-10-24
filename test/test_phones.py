import re
import random
from fixture.contact import merge_phones_like_on_home_page, merge_emails_like_on_home_page


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone


def test_contacts_on_main_and_edit_page(app):
    contacts_from_home_page = app.contact.get_contact_list()
    random_number = random.randrange(len(contacts_from_home_page))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(random_number)
    assert contacts_from_home_page[random_number].first_name == contact_from_edit_page.first_name
    assert contacts_from_home_page[random_number].last_name == contact_from_edit_page.last_name
    assert contacts_from_home_page[random_number].address == contact_from_edit_page.address
    assert contacts_from_home_page[random_number].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contacts_from_home_page[random_number].all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)