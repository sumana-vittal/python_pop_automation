from behave import given, then


@given('Open Circle Page')
def open_circle_page(context):
    context.app.circle_page.open_circle()


@then('Verify that clicking through Circle tabs works')
def verify_click_circle_tabs(context):
    context.app.circle_page.verify_circle_tabs()
