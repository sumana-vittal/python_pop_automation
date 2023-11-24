from behave import then


@then('Verify {expected_message} message is shown')
def verify_cart_message(context, expected_message):
    context.app.cart_page.verify_cart_empty_message(expected_message)


@then('Verify cart has individual cart item')
def verify_single_cart_item_header(context):
    context.app.cart_page.verify_single_cart_item_message()


@then('Verify cart has correct product')
def verify_product_name(context):
    context.app.cart_page.verify_product_name(context.product_name)
    