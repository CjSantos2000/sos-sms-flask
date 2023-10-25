# send_sms.py
import sys, requests

base_url = "https://semaphore.co/api/v4/messages"
api_key = "d976ae4a30b895246d9fc1bc1dabacdb"


def send_message():
    print("Sending Message...")
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
    print(response)
    print("Message Sent!")


if __name__ == "__main__":
    # message = sys.argv[1]
    # number = sys.argv[2]
    # send_message(message, number)
    send_message()
