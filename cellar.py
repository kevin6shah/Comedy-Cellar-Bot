import argparse
import os
from dotenv import load_dotenv, find_dotenv
import webbot
import datetime
from datetime import date
from selenium.webdriver.common.by import By
from localStoragePy import localStoragePy

load_dotenv(find_dotenv())

DATE_FORMAT = '%m/%d/%Y'


def dateCheck(s):
    try:
        date = datetime.datetime.strptime(s, DATE_FORMAT)
        return date
    except:
        raise argparse.ArgumentTypeError('Input date is not a valid date')


def timeCheck(s):
    timeSplit = s.split(':')
    if (all(time.isdigit() for time in timeSplit)):
        return f"{s}pm"
    else:
        raise argparse.ArgumentTypeError('Input time is not a valid time')


def reserveShow(web):
    web.type('George', xpath='//*[@id="panel-4"]/div[2]/form/div[1]/input')
    web.type('Patrick', xpath='//*[@id="panel-4"]/div[2]/form/div[2]/input')
    web.driver.find_element(
        by=By.XPATH, value='//*[@id="panel-4"]/div[2]/form/div[3]/select/option[5]').click()
    web.type('5059338493',
             xpath='//*[@id="panel-4"]/div[2]/form/div[4]/input[1]')
    web.click(xpath='//*[@id="panel-4"]/div[3]/input[2]')
    web.click('Make Reservation')

    while not web.exists('Confirmation', xpath='//*[@id="panel-6"]/h2'):
        pass

    print('RESERVED SHOW!!')
    localStorage.setItem(args.email, 'RESERVED')
    web.quit()


def startBot():
    web = webbot.Browser(showWindow=False, driverPath=os.environ.get("CHROMEDRIVER_PATH"),
                         binaryLocation=os.environ.get("GOOGLE_CHROME_BIN"))
    web.go_to('https://www.comedycellar.com/v3/reservation/')
    web.click('Make Reservation')
    web.click(str(args.date.day))
    web.click(args.time)
    web.click(xpath='//*[@id="panel-2"]/div[2]/input[2]')
    web.type(args.email, xpath='//*[@id="panel-3"]/div[2]/form/div[1]/input')
    web.type(args.email, xpath='//*[@id="panel-3"]/div[2]/form/div[2]/input')
    web.click(xpath='//*[@id="panel-3"]/div[3]/input')

    if (web.exists('Sold Out', xpath='//*[@id="panel-32"]/h2')):
        print('Sold Out')
    else:
        print('Available')
        reserveShow(web)


parser = argparse.ArgumentParser(description="Bot for Comedy Cellar NYC")
required = parser.add_argument_group('required arguments')
required.add_argument(
    "-e",
    "--email",
    help="Email address to use for Comedy Cellar",
    required=True,
)
parser.add_argument("-d", "--date", help="Date for the reservation",
                    default=date.today().strftime(DATE_FORMAT), type=dateCheck)
parser.add_argument("-t", "--time", help="Time for the reservation. NOTE: Time should be formatted like '9:30' for a 9:30pm show",
                    default="9:30", type=timeCheck)

args = parser.parse_args()

localStorage = localStoragePy('cellar')

if (localStorage.getItem(args.email) == None):
    startBot()
else:
    print('Already Reserved!')
