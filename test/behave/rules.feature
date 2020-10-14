Feature: Get Rule of Acquisition
  Scenario Outline: Get Rule v1
    Given an English speaking user
    When the user says "what is the <type> rule of acquisition"
    Then mycroft reply should contain "<rule>"

    Examples: Ordinal and rule example
      | type | rule |
      | first | Once you have their money, you never give it back |

  Scenario Outline: Get Rule v2
    Given an English speaking user
    When the user says "what is rule of acquisition number <number>"
    Then mycroft reply should contain "<rule>"

    Examples: Rule example
      | number |
      | Once you have their money, you never give it back |