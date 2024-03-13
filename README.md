# Bus Tracking Notification System

Sends a message to users based on bus route ETA through messages to a channel using Slack's app API or directly to users' phones via email to SMS services.

## Usage

1. Ensure you have access to the DoubleMap GPS bus services.
2. Configure Slack channel and app for Slack notifications (if using Slack).
3. Create the `config.json` file in the `Slack` directory with your Slack API token.
```
    {
        "slack_api_token": "your_slack_api_token"
    }
```
4. Ensure you have a valid Gmail or iCloud account and set up app passwords for email to SMS notifications.
5. Create the `credentials.json` file in the `sms` directory with your email and SMS service provider credentials.
```
    {
        "name": {
            "number": "name_phone_number",
            "provider": "name_sms_provider"
        },
        "icloud": {
            "email": "your_icloud_email",
            "password": "your_icloud_app_password"
        }
    }
```
6. Run the `tracker.py` script to start the bus tracking and notification system.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or feedback, contact [Ethan Bogart](mailto:bogart_ethan@icloud.com)
