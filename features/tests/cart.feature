Feature: Test Scenarios for Cart

  Scenario: “Your cart is empty” message is shown for empty cart
    Given Open target home page
    When Click on Cart icon
    Then Verify Your cart is empty message is shown

  Scenario: User check for the single item added to the cart
    Given Open target home page
    When  Search for mug
    And   Select the product by clicking on Add to cart
    And   Store product name
    And   From right side navigation menu, click "View cart & check out"
    Then  Verify cart has individual cart item
    And   Verify cart has correct product
