from email import message
import time
from turtle import title 
from plyer import notification

if __name__=="__main__":
    notification.notify (
        title = "Please drink water",
        message = " Getting enough water every day is important for your health. Drinking water can prevent dehydration. ",
        timeout=5 
    )