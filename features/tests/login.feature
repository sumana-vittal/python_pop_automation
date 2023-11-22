Feature: Test Scenarios for login test

  Scenario: Verify user successfully logged in
    Given Open target home page
    When  Click Sign In
    And   From right side navigation menu, click Sign In
    And   Input email jac42437@udinnews.com and password ******** on SignIn page
    And   Click on Sign In button
    Then  Verify user is logged in and sign in form is disappeared