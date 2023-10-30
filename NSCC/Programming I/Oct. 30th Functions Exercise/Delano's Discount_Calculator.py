def main():
    print("\nDiscount Calculator\n")

    # variables initialization
    original_price = float(input("Enter total price: $"))
    total_price = 0
    discount_percentage = 0
    discount_amount = 0
    tax = 15/100 # tax set at 15%
    tax_amount = 0

    # verify and set discount percetage
    if original_price < 100: # 0 to 99 - 10% discount
        discount_percentage = 10
    elif original_price < 200: # from 100 to 199 - 15% discount
        discount_percentage = 15
    elif original_price < 300: # from 200 to 299 - 25% discount
        discount_percentage = 25
    elif original_price < 600: # from 300 to 599 - 35% discount
        discount_percentage = 35
    else: #over 599 - 50% discount
        discount_percentage = 50

    discount_amount = discount_percentage/100 * original_price
    tax_amount = tax/100 * (original_price - discount_amount)
    total_price = original_price - discount_amount + tax_amount

    print(f"Total (before taxes): ${original_price:,.2f} \
\nDiscount Percentage: {discount_percentage}%\
\nDiscount Amount: ${discount_amount:,.2f}\
\nTax ({tax}%): ${tax_amount}\
\n------------------\
\nTotal Price: ${total_price:,.2f}\n")

if __name__ == "__main__":
    main()