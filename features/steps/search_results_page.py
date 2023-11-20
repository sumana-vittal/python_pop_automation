from behave import when, then


@when('Select the product by clicking on Add to cart')
def click_add_to_cart(context):
    context.app.search_results_page.click_add_to_cart()


@when('From right side navigation menu, click "View cart & check out"')
def click_right_navigation_cart_check_out_menu(context):
    context.app.search_results_page.click_right_navigation_view_cart()


@then('Verify the search result page for {product} header')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_result_header(product)


@then('Verify {product} in search result url')
def verify_search_url(context, product):
    context.app.search_results_page.verify_search_result_url(product)


