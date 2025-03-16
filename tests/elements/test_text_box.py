import logging
from pages.elements.text_box_page import TextBoxPage
from pages.elements.home_page import HomePage
from pages.elements.elements_page import ElementsPage

def test_text_box(page):
    logging.info("Navigating to the home page")
    home_page = HomePage(page)
    home_page.open("https://demoqa.com/")
    home_page.page_verify()
    
    logging.info("Navigating to the text box page")
    home_page.click_elements_button()
    element_page = ElementsPage(page)
    element_page.page_verify()
    element_page.click_text_box()

    text_box_page = TextBoxPage(page)
    text_box_page.page_verify()
    logging.info("Filling the form")
    text_box_page.fill_form('Ivan Petrov', 'ivan_petrov@gmail.com', 'Minsk City, Main Street, 1-1', 'Minsk City, Secondary Street, 1-2')

    logging.info("Validating the results")
    assert 'Ivan Petrov' in page.locator('#name').text_content()
    assert 'ivan_petrov@gmail.com' in page.locator('#email').text_content()
    assert 'Minsk City, Main Street, 1-1' in page.locator('p#currentAddress').text_content()
    assert 'Minsk City, Secondary Street, 1-2' in page.locator('p#permanentAddress').text_content()
