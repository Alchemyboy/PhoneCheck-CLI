import sys
import phonenumbers
from phonenumbers import geocoder, carrier, timezone, phonenumberutil
from datetime import datetime, timezone as dt_timezone

numbers = [
    "+91xxxxxxxxx",
    "+91xxxxxxxxx",
    "+91xxxxxxxxx",
]

def enum_name(value):
    # Convert enum int to readable name safely
    for name, val in vars(phonenumberutil.PhoneNumberType).items():
        if not name.startswith("_") and isinstance(val, int) and val == value:
            return name
    return f"Unknown({value})"

def describe(number):
    try:
        num = phonenumbers.parse(number)
    except Exception as e:
        print(f"\n{number} → Parse error: {e}\n")
        return

    print("\n--------------------------------------")
    print("Input:", number)
    print("Valid:", phonenumbers.is_valid_number(num))
    print("E164:", phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.E164))
    print("National:", phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.NATIONAL))

    num_type = phonenumbers.number_type(num)
    print("Type:", enum_name(num_type))

    print("Carrier:", carrier.name_for_number(num, "en") or "Unknown")

    tz = timezone.time_zones_for_number(num)
    print("Timezones:", ", ".join(tz) if tz else "Unknown")

    desc = geocoder.description_for_number(num, "en") or "Unknown"
    print("Location:", desc)

    # Try light city/state guessing
    parts = [p.strip() for p in desc.split(",") if p.strip()]
    if len(parts) == 1:
        print("City (guess):", parts[0])
        print("State (guess): None")
    elif len(parts) > 1:
        print("City (guess):", ", ".join(parts[:-1]))
        print("State (guess):", parts[-1])
    else:
        print("City (guess): None")
        print("State (guess): None")

    print("--------------------------------------\n")

print("\n=== Phone Number Lookup ===")
print("Run at:", datetime.now(dt_timezone.utc).isoformat(), "UTC")

for n in numbers:
    describe(n)

try:
    input("Finished. Press Enter to exit...")
except:
    pass
