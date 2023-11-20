from behave import then


@then('Verify the search result page for {product} header')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_result_header(product)


@then('Verify {product} in search result url')
def verify_search_url(context, product):
    context.app.search_results_page.verify_search_result_url(product)