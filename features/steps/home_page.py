from behave import given, when, then


@given('Open target home page')
def open_home_page(context):
    context.app.home_page.open_home_page()


@when('Search for {product}')
def search_product(context, product):
    context.app.home_page.search(product)


@then('Verify the search result page for {product} header')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_result_header(product)


@then('Verify {product} in search result url')
def verify_search_url(context, product):
    context.app.search_results_page.verify_search_result_url(product)

