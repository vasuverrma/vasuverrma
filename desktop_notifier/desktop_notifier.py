import time
from plyer import notification
if __name__ == "__main__":
    # this is used to execute some code only if the file was run directly, and not imported.
    while True:
        #only gives notification on your desktop
        notification.notify(
            title = "Hello Vasu!!!",
            message = "Time for a Workout..!!",
            timeout = 5
        )
        #Python time sleep(v) Method
        #v is the number of seconds execution to be suspended.
        time.sleep(3600)
