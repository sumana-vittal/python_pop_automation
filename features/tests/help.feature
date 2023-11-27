Feature: Tests for Help Pages

  Scenario: User can select Help topic
    Given Open Help page for Returns
    Then  Verify Returns page opened
    When  Select Help topic Promotions & Coupons
    Then  Verify Current promotions page opened

  Scenario Outline: User can select Help topic
    Given Open Help page for Returns
    Then  Verify Returns page opened
    When  Select Help topic <topic>
    Then  Verify <topic_header> page opened
  Examples:
    |topic               |topic_header            |
    |Gift Cards          | Target GiftCard balance|
    |Holiday Help        | Holiday Help           |
    |Orders & Purchases  | Print a receipt        |
    |Target Circle™      | About Target Circle    |


