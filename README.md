# iCard Client Python Implementation
This is an example implentation of an iCard client in python.
The client class is very simple to use and has the following methods:
 - Get Brands
 - Retreive Cards
 - Purchase

## Creating an instance of iCard client
Before using any of the class methods, you first have to create an object instance of the iCard client class.
Creating an instance requires one parameter and that is the base URL.

There are two eviroments in iCard:
 - Production
 - Testing

Creating an instance of the client requires 3 parameters:
 - iCash Card Number
 - API Token
 - Enviroment Type ("production" or "testing")

### Example 1 - Production Enviroment
    iCardCleintProduction = iCard(7120114562, "d2fghj3#kleu4i$^oeddk3w4dow343kdlk+%#%DE$G^HLS123Phhr%^H+55Ssrf#4f", "production")
### Example 2 - Testing Enviroment
    iCardCleintTesting = iCard(1000114562, "f4#frsS55+H^%rhhP321SLH^G$ED%#%+kldk343wod4w3kddeo^$i4uelk#3jhgf2d", "testing")

## Get Card Brands & Categories
This method returns a detailed list of all brands and categories. It requires a single parameter which is the package number (determines the price of cards).
### Example

    iCardClient.getBrands("712")

### Response

    Insert Response

## Retrieve Cards
This method requires 2 parameters:
 - iCash Card Number
 - Payment Code to Store #10 where amount is zero.
### Example

    iCardClient.retrieveCards("7120111245", "1579864")

### Response

    Insert Response
## Purchase Cards
This method purchases cards for the iCard store. It requires the following 2 parameters:
 - Payment Code to store #10 and total amount
 - Dictionary where the keys are card IDs and values are the quatity for each card.

### Example
    iCardClient.purchaseCards({1:3, 4:5, 6:9}, "1234567")

### Response

    Insert Response

