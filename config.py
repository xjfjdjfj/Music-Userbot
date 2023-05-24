"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021  Asad Ali <https://github.com/jankarikiduniya>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "11360899")
        self.API_HASH: str = os.environ.get("API_HASH", "b3a49413dfcaf0a16bd6d15e49772d70")
        self.SESSION: str = os.environ.get("SESSION", "AQByy4i7lLklJsKwZfrNJho-CzuX-HF7jlzB0VQBvrS-Vz2wyCV48eLUQ6NFGt0JVRStIVPZfOg53_VzOmXNKQ8OhUKimHWcC6VPH08H8W9I-YO1ZLU5j7gku9TUMgawI9nsq4qjbXFSiMJHNRjAq4q02ZvVfK4bRmE24YxdmvAbgZd78mtLc3uIVRvcy4f-xxMsv919W7IoXRpkLv_ilTD3eptOwKmlcy-1zXfPHk2f7awvfZ-OPmxMhu0qwfe_neK33tJoboC4zoIkNybIPaE32ycMxQ2xJTggaR3og980MhFVZG7zpbWkwmTXhbOvGiwzseKS03nd2ucMD7kgTuAAAAAUpVis4A")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "5329996263").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("Error: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.CUSTOM_QUALITY: str = os.environ.get("CUSTOM_QUALITY", "high").lower()


config = Config()
