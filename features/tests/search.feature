Feature: Test Scenarios for the Search

  @smoke
  Scenario: verify search product
    Given Open target home page
    When Search for coffee
    Then Verify the search result page for coffee header
    And Verify coffebee in search result url