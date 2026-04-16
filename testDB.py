from database import contributions

contributions.insert_one({
    "name": "Test User",
    "email": "lakshyashukla108@gmail.com"
})

print("Inserted Successfully ✅")