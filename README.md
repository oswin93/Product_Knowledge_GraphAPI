# Product Knowledge Graph API

This Python program retrieves SKU details for a specified product using the Shopalyst Product Knowledge Graph API. By providing a product ID, the program fetches and displays details about each SKU, including SKU ID, shade, offer price, and title.


## Prerequisites

* Python 3.x
* requests library: Required to make API requests.


## Code Structure

* Input Handling: The user is prompted to enter a product ID.
* API Request: A GET request is made to the API endpoint using the provided product ID.
* Data Parsing: Extracts SKU information, including ID, shade, offer price, and title from the JSON response.
* Output Formatting: Displays SKU details for each product variant.

## API Reference

* Endpoint: https://dev.shopalyst.com/shopalyst-service/v1/products/<productId>
* Method: GET
* Parameters: productId – Unique identifier for the product in the Product Knowledge Graph.


## Sample Output:

Enter the product ID: 929323BCA2A04A74961E0043E9A55B60

###### Product ID: 929323BCA2A04A74961E0043E9A55B60
* Product 1
* skuId : 152934
* shade : MR21 Brick Blush
* offerPrice : 299.0
* title : Lakme 9 to 5 Primer + Matte Lip Color - MR21 Brick Blush
--------------------------
* Product 2
* skuId : 152935
* shade : MR22 Scarlet Surge
* offerPrice : 299.0
* title : Lakme 9 to 5 Primer + Matte Lip Color - MR22 Scarlet Surge