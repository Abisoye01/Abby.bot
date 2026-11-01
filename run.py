from flask import Flask
from threading import Thread
from highrise.__main__ import *
import os
import time
from dotenv import load_dotenv

load_dotenv()

ROOM_ID = os.getenv("ROOM_ID")
BOT_TOKEN = os.getenv("HIGHRISE_BOT_TOKEN")

if not ROOM_ID or not BOT_TOKEN:
    raise RuntimeError(
        "Missing HIGHRISE_BOT_TOKEN or ROOM_ID in your .env file. "
        "Example:\nHIGHRISE_BOT_TOKEN=your_token\nROOM_ID=your_room_id"
    )


class WebServer():

  def __init__(self):
    self.app = Flask(__name__)

    @self.app.route('/')
    def index() -> str:
      return "Funcionando"

  def run(self) -> None:
    self.app.run(host='0.0.0.0', port=8080)

  def keep_alive(self):
    t = Thread(target=self.run)
    t.start()


class RunBot():
  room_id = ROOM_ID
  bot_token = BOT_TOKEN
  bot_file = "main"
  bot_class = "Bot"

  def __init__(self) -> None:
    self.definitions = [
        BotDefinition(
            getattr(import_module(self.bot_file), self.bot_class)(),
            self.room_id, self.bot_token)
    ]

  def run_loop(self) -> None:
    while True:
      try:
        arun(main(self.definitions))

      except Exception as e:
        print("Error: ", e)
        time.sleep(5)

if __name__ == "__main__":
  WebServer().keep_alive()
  RunBot().run_loop()
