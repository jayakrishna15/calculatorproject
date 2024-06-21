from datetime import datetime
import phonenumbers
import pytz
from phonenumbers import timezone, geocoder, carrier
from zoneinfo import ZoneInfo

number = input("Enter your number with country code (e.g., +91): ")

# Parse the phone number with default region 'IN' (for India)
phone = phonenumbers.parse(number, "IN")

# Get time zone for the phone number
time_zones = timezone.time_zones_for_number(phone)

# Get carrier name for the phone number
car = carrier.name_for_number(phone, "en")

# Get region description for the phone number
reg = geocoder.description_for_number(phone, "en")

print(f"Phone number: {phone}")
print(f"Time zones: {time_zones}")
print(f"Carrier: {car}")
print(f"Region: {reg}")

# Example of getting the current time in the phone number's primary time zone
if time_zones:
    tz = pytz.timezone(time_zones[0])
    current_time = datetime.now(tz)
    print(f"Current time in primary time zone ({time_zones[0]}): {current_time}")
