import argparse
import os
from dotenv import load_dotenv, find_dotenv
import webbot

load_dotenv(find_dotenv())


def startBot():
    web = webbot.Browser(showWindow=False, driverPath=os.environ.get("CHROMEDRIVER_PATH"),
                         binaryLocation=os.environ.get("GOOGLE_CHROME_BIN"))
    web.go_to('www.google.com')
    print(web.get_page_source())


parser = argparse.ArgumentParser(description="Bot for Comedy Cellar NYC")
required = parser.add_argument_group('required arguments')
required.add_argument(
    "-u",
    "--url",
    help="Url to the course page that contains the index number",
    required=False,
)
args = parser.parse_args()

startBot()
