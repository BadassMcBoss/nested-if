attendees = int(input("Enter number of attendees: "))
meal_type = input("Would you like vegetarian food? (yes/no): ")

venue = "large hall" if attendees > 100 else "conference room"
additional_facilities = "audio system and projector" if attendees > 100 else "projector only"
meal_served = "Veggie Delight Caterers" if meal_type == "yes" else "Gourmet Meals Caterers"
print(venue, additional_facilities, meal_served)