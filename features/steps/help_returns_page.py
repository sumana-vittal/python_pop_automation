from behave import given, when, then


@given('Open Help page for Returns')
def open_target_help_returns(context):
    context.app.help_page.open_help_returns_page()


@when('Select Help topic Promotions & Coupons')
def select_promotions(context):
    context.app.help_page.select_topic()


@then('Verify Returns page opened')
def verify_return_opened(context):
    context.app.help_page.verify_returns_page_opened()


@then('Verify Current promotions page opened')
def verify_promotions_opened(context):
    context.app.help_page.verify_promotions_page_opened()
