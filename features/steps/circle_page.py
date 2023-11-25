from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@given('Open Circle Page')
def open_circle_page(context):
    context.app.circle_page.open_circle()


@given('Store original window')
def store_windows(context):
    #context.windows = context.driver.window_handles
    context.windows = context.app.page.get_all_windows()
    #context.original_window = context.driver.current_window_handle
    context.original_window = context.app.page.get_current_window()


@when('Click Google Play button')
def click_google_play(context):
   # context.driver.find_element(*GOOGLE_PLAY_BTN).click()
    context.app.circle_page.click_google_play()


@when('Switch to new window')
def switch_window(context):
    # context.driver.wait.until(EC.new_window_is_opened)
    # new_window = context.driver.window_handles[1]
    # context.driver.switch_to.window(new_window)
    context.app.page.switch_to_new_window()


@then('Verify that clicking through Circle tabs works')
def verify_click_circle_tabs(context):
    context.app.circle_page.verify_circle_tabs()


@then('Verify Google Play Target page opened')
def verify_google_play_opened(context):
    #assert 'https://play.google.com/' in context.driver.current_url
    context.app.partner_page.verify_google_play_opened()


@then('Close current page')
def close(context):
    #context.driver.close()
    context.app.page.close_page()


@then('Return to original window')
def switch_original_window(context):
    #context.driver.switch_to.window(context.original_window)
    context.app.page.switch_to_window(context.original_window)