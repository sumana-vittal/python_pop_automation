from behave import when, then


@when('Input email {email} and password {password} on SignIn page')
def input_email_and_password(context, email, password):
    context.app.login_page.input_user_email_password(email, password)


@when('Click on Sign In button')
def click_sign_in_button(context):
    context.app.login_page.click_sign_in_button()


@when('Store original windows')
def store_current_window(context):
    context.original_window = context.app.page.get_current_window()


@when('Click on Target terms and conditions link')
def click_terms_and_conditions(context):
    context.app.login_page.click_terms_and_conditions()


@when('Switch to the newly opened window')
def switch_new_window(context):
    context.app.page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_opened(context):
    context.app.partner_page.verify_terms_and_conditions_opened()


@then('Verify user is logged in and sign in form is disappeared')
def verify_user_logged_in(context):
    context.app.login_page.verify_user_successfully_logged_in()


@then('User can close new window and switch back to original')
def close_terms_and_conditions_page(context):
    context.app.page.close_page()
    context.app.page.switch_to_window(context.original_window)