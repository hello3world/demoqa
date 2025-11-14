import allure
from pages.widgets.slider_page import SliderPage

pytestmark = allure.suite('Widgets')

@allure.feature('Slider Page')
class TestSliderPage:
    @allure.title('Check moved slider')
    def test_slider(self, page):
        slider = SliderPage(page)
        slider.open()
        before, after = slider.change_slider_value()
        assert before != after
