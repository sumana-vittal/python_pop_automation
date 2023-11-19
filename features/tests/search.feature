Feature: Test Scenarios for the Search

  Scenario: verify search product
    Given Open target home page
    When Search for coffee
    Then Verify the search result page for coffee header
    And Verify coffee in search result url