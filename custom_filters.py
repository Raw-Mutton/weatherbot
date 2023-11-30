from typing import Optional, Union
from telegram import Message
from telegram.ext._utils.types import FilterDataDict
from telegram.ext.filters import MessageFilter

class Current_temp(MessageFilter):
    def filter(self, message: Message) -> bool | FilterDataDict | None:
        if message.text == "temperature":
            return True