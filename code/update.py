import os

from dotenv import load_dotenv
from lookup_turns import find_todays_phone
from zoom import ZoomClient


def update_phone_number():
    load_dotenv()

    ZOOM_ACCOUNT_ID = os.environ.get("ZOOM_ACCOUNT_ID")
    ZOOM_CLIENT_ID = os.environ.get("ZOOM_CLIENT_ID")
    ZOOM_CLIENT_SECRET = os.environ.get("ZOOM_CLIENT_SECRET")

    if not ZOOM_ACCOUNT_ID or not ZOOM_CLIENT_ID or not ZOOM_CLIENT_SECRET:
        return

    zoom_client = ZoomClient(ZOOM_ACCOUNT_ID, ZOOM_CLIENT_ID, ZOOM_CLIENT_SECRET)

    todays_phone = find_todays_phone()
    if todays_phone == "not found":
        print("phone number not found")
        return

    print(zoom_client.set_phone_number("ON Call IT", f"+1{todays_phone}"))
    settings = zoom_client.get_extension_settings("ON Call IT")

    print(
        settings["business_hours"][1]["settings"]["routing"]["forward_to"][
            "phone_number"
        ]
    )

if __name__ == "__main__":
    update_phone_number()
