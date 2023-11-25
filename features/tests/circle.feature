Feature: Test Scenarios for Target Circle Page

  Scenario: Verify user can click through Circle tabs
    Given Open Circle Page
    Then  Verify that clicking through Circle tabs works

  Scenario: User is able to navigate to Google Play Target Page
    Given Open Circle Page
    And   Store original window
    When  Click Google Play button
    And   Switch to new window
    Then  Verify Google Play Target page opened
    And   Close current page
    And   Return to original window