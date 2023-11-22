from behave import when, then


@when('Input email {email} and password {password} on SignIn page')
def input_email_and_password(context, email, password):
    context.app.login_page.input_user_email_password(email, password)


@when('Click on Sign In button')
def click_sign_in_button(context):
    context.app.login_page.click_sign_in_button()


@then('Verify user is logged in and sign in form is disappeared')
def verify_user_logged_in(context):
    context.app.login_page.verify_user_successfully_logged_in()
