Feature: Single product API

  Background:
    Given openapi ./swagger.yaml

  Scenario Outline: Getting a product that does not exist
    When GET /v1/products/(id:number)
    Then status 404
    Examples:
      | id       |
      | 10000000 |

  Scenario Outline: Successful getting product by ID
    When GET /v1/products/(id:number)
    Then status 200
    Examples:
      | id |
      | 42 |

  Scenario Outline: Deleting a product that does not exist
    When DELETE /v1/products/(id:number)
    Then status 404
    Examples:
      | id       |
      | 10000000 |

  Scenario Outline: Successful deleting product by ID
    When DELETE /v1/products/(id:number)
    Then status 204
    Examples:
      | id   |
      | 7777 |

  Scenario Outline: Successful getting list of products
    When GET /v1/products?expanded=(number)
    Then status 200
    Examples:
      | expanded |
      | 1        |
      | 0        |

  Scenario Outline: Successful getting list of products in a given category
    When GET /v1/products?category=(string)
    Then status 200
    Examples:
      | category    |
      | smartphones |
      | laptops     |
      |             |

  Scenario Outline: Successful getting list of products in a given category and expanded param
    When GET /v1/products?category=(string)&expanded=(number)
    Then status 200
    Examples:
      | category    | expanded |
      | smartphones | 1        |
      | laptops     | 0        |
      |             | 1        |
      |             | 0        |

  Scenario Outline: Successful getting list of products using search term
    When GET /v1/products?q=(string)
    Then status 200
    Examples:
      | q     |
      | phone |
      | HP    |
      |       |

  Scenario Outline: Successful getting list of products using search term and expanded param
    When GET /v1/products?q=(string)&expanded=(number)
    Then status 200
    Examples:
      | q     | expanded |
      | phone | 1        |
      | HP    | 0        |
      |       | 1        |
      |       | 0        |

  Scenario Outline: Successful getting expanded list of products in a given category and using text search
    When GET /v1/products?category=(string)&expanded=(number)&q=(string)
    Then status 200
    Examples:
      | category    | expanded | q   |
      | smartphones | 1        | foo |
      | laptops     | 0        |     |
      |             | 1        |     |
      |             | 0        |     |