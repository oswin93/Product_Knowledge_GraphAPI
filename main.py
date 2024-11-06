import requests

API_BASE_URL = "https://dev.shopalyst.com/shopalyst-service/v1/products"

def get_product_sku(product_id):

    # Creating the API endpoint
    api_url = f"{API_BASE_URL}/{product_id}"

    try:
        # Making a GET request to the Shopalyst API
        response = requests.get(api_url)
        response.raise_for_status()

        # Parse the JSON response
        product_data = response.json()

        # Checking if SKUs are available
        skus = product_data.get("skuSet", [])
        if not skus:
            print("No SKUs found for this product.")
            return

        # Print each SKU's details in the required format
        print(f"Product ID: {product_id}")
        for i, sku in enumerate(skus, start=1):
            sku_id = sku.get("skuId", "N/A")
            shade = next(iter(sku["attributes"].values()), "N/A")
            offer_price = sku.get("offerPrice", "N/A")
            title="N/A"
            if "attributeValues" in product_data and product_data["attributeValues"]:
                for attribute in product_data["attributeValues"]:
                    if attribute.get("id") == shade:  # Matching on a unique attribute with shade
                        title = attribute.get("title", "N/A")
                        break  # Stop searching once the title is found


            print("-" * 30)
            print(f"Product {i}")
            print(f"skuId : {sku_id}")
            print(f"shade : {shade}")
            print(f"offerPrice : {offer_price}")
            print(f"title : {title}")
            print()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# Accepting the product ID input from User
if __name__ == "__main__":
    product_id = input("Enter the product ID: ")
    get_product_sku(product_id)