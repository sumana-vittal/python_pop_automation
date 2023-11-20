from behave import then


@then('Verify {expected_message} message is shown')
def verify_cart_message(context, expected_message):
    context.app.cart_page.verify_cart_empty_message(expected_message)