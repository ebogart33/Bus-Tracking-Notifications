from double.double_map import Double_Map # Check if doublemap is working this way if it is remove other doublemap folder
import time,json
from sms.send import Email_MESSAGE
from Slack.message import Slack_MESSAGE

def main():
    tracker = Double_Map('txstate')
    Email_Message = Email_MESSAGE
    Slack_Message = Slack_MESSAGE

    with open("sms/credentials.json") as json_file:
        credentials = json.load(json_file)

    message = "Test"
    subject = "Tracker"

    ethan_number = credentials["ethan"]["number"]
    ethan_provider = credentials["ethan"]["provider"]
    icloud_email = credentials["icloud"]["email"]
    icloud_password = credentials["icloud"]["password"]
 
    brielle_provider = credentials["brielle"]["provider"]
    brielle_number = credentials["brielle"]["number"]

    message_sent = False  # Flag to track if the message has been sent in the current cycle

    while True:
     eta_1403 = tracker.eta(36,1417)
     if eta_1403 != -1:
         print(eta_1403)
         if not message_sent and eta_1403 <= 4: #Aquarena route_id-1403/1434 stops{36-UAC,90-Aquarena,26-Riverside}  When bus is 4 minutes away thats when push should be sent
             message_sent = Slack_Message.Send_message(message)
             if not message_sent:
                Email_Message.send_sms_via_icloud(ethan_number, message, ethan_provider, (icloud_email,icloud_password))
                Email_Message.send_sms_via_icloud(brielle_number, message, brielle_provider, (icloud_email,icloud_password))
                message_sent = True  # Update the flag to indicate that the message has been sent
         elif eta_1403 > 6:
             message_sent = False  # Reset the flag if the ETA is greater than 4 minutes
         time.sleep(30)
     else:
         print("Route is inactive. Waiting for it to become active again...")
         time.sleep(60)  # Wait for 60 seconds before checking again

if __name__ == '__main__':
    main()