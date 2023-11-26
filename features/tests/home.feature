Feature: Target Home page UI tests

  Scenario: User can see signin arrow
    Given Open target home page
    When  Hover over signin
    Then  Verify signin arrow shown