Feature: Test Scenarios for Cart

  Scenario: “Your cart is empty” message is shown for empty cart
    Given Open target home page
    When Click on Cart icon
    Then Verify Your cart is empty message is shown
