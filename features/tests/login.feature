Feature: Test Scenarios for login test

  Scenario: Verify user successfully logged in
    Given Open target home page
    When  Click Sign In
    And   From right side navigation menu, click Sign In
    And   Input email jac42437@udinnews.com and password ******** on SignIn page
    And   Click on Sign In button
    Then  Verify user is logged in and sign in form is disappeared


  Scenario: User can open and close Terms and Conditions from sign in page
      Given Open target home page
      When  Click Sign In
      And   From right side navigation menu, click Sign In
      And   Store original windows
      And   Click on Target terms and conditions link
      And   Switch to the newly opened window
      Then  Verify Terms and Conditions page is opened
      And   User can close new window and switch back to original

  Scenario: User check for incorrect email and password
     Given Open target home page
     When  Click Sign In
     And   From right side navigation menu, click Sign In
     When  Input email test7@example.com and password testtest on SignIn page
     And   Click on Sign In button
     Then  Verified that “We can't find your account.” message is shown
