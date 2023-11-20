Feature:Test Scenarios for the the Target Sign in

  Scenario:Verify Sign In form is opened
    Given Open target home page
    When Click Sign In
    And  From right side navigation menu, click Sign In
    Then Verify Sign In url is opened
    And  Verify Sign in header Sign is present
    And  Verify Sign in button is present