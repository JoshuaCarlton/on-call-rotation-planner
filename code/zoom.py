import requests


class ZoomClient:
    def __init__(self, account_id, client_id, client_secret) -> None:
        self.account_id = account_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = self.get_access_token()

    def get_access_token(self):
        data = {
            "grant_type": "account_credentials",
            "account_id": self.account_id,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        response = requests.post("https://zoom.us/oauth/token", data=data)
        return response.json()["access_token"]

    def get_call_queues(self):
        url = "https://api.zoom.us/v2/phone/call_queues"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        return requests.get(url, headers=headers).json()

    def get_extension_settings(self, queue_name):
        call_queues = self.get_call_queues()["call_queues"]
        for call_queue in call_queues:
            if call_queue["name"] == queue_name:
                desired_queue = call_queue
                break
        extension_id = desired_queue["extension_id"]
        url = f"https://api.zoom.us/v2/phone/extension/{extension_id}/call_handling/settings"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        return requests.get(url, headers=headers).json()

    def set_phone_number(self, queue_name, new_phone):
        call_queues = self.get_call_queues()["call_queues"]

        for call_queue in call_queues:
            if call_queue["name"] == queue_name:
                extension_id = call_queue["extension_id"]
                break
        else:
            raise ValueError(f"Call queue '{queue_name}' not found")

        payload = {
            "settings": {
                "call_not_answer_action": 10,
                "phone_number": new_phone
            },
            "sub_setting_type": "call_handling"
        }
        url = (
            f"https://api.zoom.us/v2/phone/extension/{extension_id}/call_handling/settings/business_hours"
        )

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }

        response = requests.patch(
            url,
            headers=headers,
            json=payload
        )

        return response
