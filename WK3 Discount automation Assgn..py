def calculate_discount(price, discount_percent):

    if discount_percent>=10:
        # Calculate the final price after applying the discount
        final_price = price - (price - discount_percent / 100)
        return final_price
    else:
        return price
    
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if discount_percent >= 10:
    print(f"The final price after a {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")