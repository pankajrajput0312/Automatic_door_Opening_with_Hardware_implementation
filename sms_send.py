# send sms using fastsms API
import datetime


def get_date_time():
    x = datetime.datetime.now()
    x = str(x)
    date = x.split(" ")[0]
    time = x.split(" ")[1].split(".")[0]
    return (date, time)


def send_sms(number, Id):
    import requests
    import json
    import pandas as pd
    from get_details import details
    from add_details_incsv import update_incoming_list
    url = "https://www.fast2sms.com/dev/bulk"
    number = 9810904773
    person_details = list(details(Id))
    date, time = get_date_time()
    message_admin = "Person Name "+str(person_details[1])+" unique_id "+str(
        person_details[0])+" Email_id: "+str(person_details[2])+" Entered in your House at " + date + " "+time
    user_number = str(person_details[3])
    update_incoming_list(
        person_details[1], person_details[0], person_details[2], user_number)
    message_violeter = "Welcome for coming in our House. We are Waiting for you. Directly come to 2nd Floor"

    print(message_admin)

    prams_voileter = {
        "authorization": "Q7BKRrYei2pxU0z8t1D4gOuJFPLNaydIqmhbTk5fVoXWAElGcvOv71o4hVmin3cfZdDIFG56rwqjYNX9",
        "sender_id": "FSTSMS",
        "route": "p",
        "language": "unicode",
        "numbers": user_number,
        "message": message_violeter
    }

    prams_admin = {
        "authorization": "ZiIlOWv3bzgP1wxkscar0Gyu4CTYhQeS9H87KDUdnBjMLJ2qpoLplP9A6SXMxNRWijcsv3OJtYqTrd4u",
        "sender_id": "FSTSMS",
        "route": "p",
        "language": "unicode",
        "numbers": number,
        "message": message_admin
    }
    response_voileter = requests.get(url, params=prams_voileter)
    response_admin = requests.get(url, params=prams_admin)
    dic_violeter = response_voileter.json()
    dic_admin = response_admin.json()
    print(dic_violeter)
    print(dic_admin)


if __name__ == "__main__":
    send_sms(9810904773, 312)
