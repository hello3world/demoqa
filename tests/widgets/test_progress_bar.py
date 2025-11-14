import allure
from pages.widgets.progress_bar_page import ProgressBarPage

pytestmark = allure.suite('Widgets')

@allure.feature('Progress Bar Page')
class TestProgressBarPage:
    @allure.title('Check changed progress bar')
    def test_progress_bar(self, page):
        progress_bar = ProgressBarPage(page)
        progress_bar.open()
        before, after = progress_bar.change_progress_bar_value()
        assert before != after

    @allure.title('Check full progress bar')
    def test_full_progress_bar(self, page):
        progress_bar = ProgressBarPage(page)
        progress_bar.open()
        before, after = progress_bar.change_full_progress_bar()
        assert before != after
        assert int(after) == 100

    @allure.title('Check progress bar after reset')
    def test_reset_progress_bar(self, page):
        progress_bar = ProgressBarPage(page)
        progress_bar.open()
        before, after = progress_bar.change_full_progress_bar('reset')
        assert before == after
