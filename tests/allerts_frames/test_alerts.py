import allure
from pages.alerts_frames.alerts_page import AlertsPage

pytestmark = allure.suite('Alerts/Frames')

@allure.title('Simple alert shows and can be accepted')
def test_simple_alert(page):
    alerts = AlertsPage(page)
    alerts.open()
    text = alerts.check_see_alert()
    assert text

@allure.title('Timer alert appears after delay and can be accepted')
def test_timer_alert(page):
    alerts = AlertsPage(page)
    alerts.open()
    text = alerts.check_alert_appear_after_5_sec()
    assert text

@allure.title('Confirm dialog accept path updates result text')
def test_confirm_accept(page):
    alerts = AlertsPage(page)
    alerts.open()
    result = alerts.check_action_alert('accept')
    assert 'You selected Ok' in result

@allure.title('Prompt dialog returns entered text')
def test_prompt(page):
    alerts = AlertsPage(page)
    alerts.open()
    typed, result = alerts.check_prompt_alert()
    assert typed in result
