# Task 1

attendees = int(input("enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2

need_audio_system = True if attendees >50 else False

need_projector = True if attendees >75 else False

if need_audio_system:
    print("We will need an audio system for this event.  Please send one to the", venue)

if need_projector:
    print("We will need a projector for this event. Please send one to the", venue)

# Task 3

vegetarian = input("Do you want vegetarian food at this event? (yes/no)")

if vegetarian == "yes":
    print("We should order from Veggie Delight Caterers.")
elif vegetarian == "no":
    print("We should order from Gourmet Meals Caterers.")
    

    

