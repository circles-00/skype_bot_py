from skpy import Skype
import environ

env = environ.Env()
environ.Env.read_env()

class SkypeService:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def send_message(self, message):
        sk = Skype(self.username, self.password)

        # while True:
        #     for ids in sk.chats.recent():
        #         print(ids)
        #     else:
        #         break

        ch = sk.chats[env('BISTRO_CHAT')]
        ch.sendMsg(message)
