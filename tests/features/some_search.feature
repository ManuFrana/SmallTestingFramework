Feature: Search something in DuckDuckGo

  Scenario Outline: Search something world in DuckDuckGo
    Given i launch chrome browser
    When open duckduckgo main page
    Then verify that main logo is loaded
    Then search for "<input>")
    And close browser

    Examples:
    | input |
    | this is clearly your first time using gherkin for tests |