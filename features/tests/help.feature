Feature: Tests for Help Pages

  Scenario: User can select Help topic
    Given Open Help page for Returns
    Then  Verify Returns page opened
    When  Select Help topic Promotions & Coupons
    Then  Verify Current promotions page opened