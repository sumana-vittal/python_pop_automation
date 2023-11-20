from behave import given, when, then


@given('Open target home page')
def open_home_page(context):
    context.app.home_page.open_home_page()


@when('Search for {product}')
def search_product(context, product):
    context.app.home_page.search(product)


@when('Click on Cart icon')
def click_on_cart_icon(context):
    context.app.home_page.click_cart_icon()


@when('Click Sign In')
def click_on_sign_in(context):
    context.app.home_page.click_sign_in()


@when('From right side navigation menu, click Sign In')
def click_right_navigation_sign_in(context):
    context.app.home_page.click_right_navigation_sign_in()



