weather = input("Enter the weather: sunny, rainy, or cold: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater"
additional_items = "hat" if weather == "sunny" else "rainboots" if weather == "rainy" else "gloves"
accessory = "sunscreen" if clothing == "sunglasses" else "waterproof bag" if clothing == "umbrella" else "earmuffs"
print(clothing, additional_items, "and", accessory)