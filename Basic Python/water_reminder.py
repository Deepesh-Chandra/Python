from plyer import notification
import time


def water_reminder():
    while True:
        notification.notify(
            title="Water Reminder For DC",
            message="Kindly sip water!",
            timeout=10
        )

        # time.sleep(60 * 60)
        time.sleep(5)


water_reminder()