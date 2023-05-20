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
        self.SESSION: str = os.environ.get("SESSION", "AQA74U_N4BHd9cnHhJY7ROoJMR4HL_JHDBwuVoKaChd-_I4QrnH0VGN_YOoYNKwrYXDlY35H6tntRWZYtmHRXXbNdkTGzmUEZ_PlLwSFxsx1x8We8Kdw8IBMMRib3xOnwS2BB90Giif6HGgtO2qPpMFIXYeSHe_fbDua1ceW1PktISzYf-jYVaCkiK827-iuHhZJ4DC3ZRCVybgZawbHD-NTEHnIC9smYiBdjNXEDrcfEV3ZQ8UpeOsudNp-y02YuWVbhUMefhOvvWXoO44EBN0ZjmVNLDL18N4UNDaTZFRfqm9-aKvboxuE_Gdpyu9DVO7GyULKhC39LynJ9lE17veSAAAAAT2xSecA")
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
