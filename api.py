import requests

from flask import Flask
from flask import request


app = Flask(__name__)


base_url = "https://semaphore.co/api/v4/messages"
api_key = "d976ae4a30b895246d9fc1bc1dabacdb"


@app.route("/")
def index():
    return "Hello World!"


@app.route("/send_sms", methods=["POST"])
def send_sms():
    address = get_client_location()
    return address
    sender_name = "SEMAPHORE"
    message = "Test Message"  # Replace Message Template
    number = "09511808537,09915236234"  # Get from firebase
    params = (
        ("apikey", api_key),
        ("sendername", sender_name),
        ("message", message),
        ("number", number),
    )

    response = requests.post(
        base_url,
        params=params,
    )
    return response.text


def get_client_location():
    client_ip = request.environ.get("HTTP_X_REAL_IP", request.remote_addr)
    print(request.environ.get("HTTP_X_REAL_IP"))
    print(request.remote_addr)
    ip_api_url = f"http://ip-api.com/json/{client_ip}"
    response = requests.get(ip_api_url)
    if response.status_code == 200:
        return {"response": response.text}
        data = response.json()
        return {
            "country": data["country"],
            "region": data["regionName"],
            "city": data["city"],
            "lat": data["lat"],
            "lon": data["lon"],
        }
    else:
        return None


if __name__ == "__main__":
    app.run(debug=True)
