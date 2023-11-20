from behave import then


@then('Verify Sign In url is opened')
def verify_sign_in_form_url(context):
    context.app.sign_in_page.verify_sign_in_url()


@then('Verify Sign in header {expected_text} is present')
def verify_sign_in_header(context, expected_text):
    context.app.sign_in_page.verify_sign_in_header(expected_text)


@then('Verify {expected_text} button is present')
def verify_sign_in_button(context,  expected_text):
    context.app.sign_in_page.verify_sign_in_button(expected_text)