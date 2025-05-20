
# 🎭 Comedy Cellar Bot

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Heroku](https://img.shields.io/badge/Deployed-Heroku-7952B3?logo=heroku)](https://heroku.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Automation](https://img.shields.io/badge/Automation-Selenium-informational)](https://www.selenium.dev/)
[![Status](https://img.shields.io/badge/status-Active-brightgreen)](https://github.com/your-username/comedy-cellar-bot)

A Selenium-powered bot that monitors **Comedy Cellar NYC's** reservation site and automatically books a show when a specific time slot becomes available.

Hosted on **Heroku**, this script runs headlessly using `webbot` and can be customized for specific dates and times via command-line parameters.

---

## 📌 Features

- Automatically checks the Comedy Cellar reservation site for availability.
- Fills in your reservation details.
- Confirms booking when a show opens up.
- Logs "Sold Out" when no slots are available.
- Fully compatible with **Heroku deployment** using environment variables for Chrome driver paths.

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.6+
- `webbot`, `selenium`, `python-dotenv`, `argparse`
- Chrome and ChromeDriver (configured via Heroku environment variables)

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Usage

Run the script via command line:

```bash
python cellar.py -e your_email@example.com [-d mm/dd/yyyy] [-t hh:mm]
```

### 🔑 Required Arguments

| Argument | Description |
|----------|-------------|
| `-e`, `--email` | **(Required)** Your email address used to make the reservation |

### 🕓 Optional Arguments

| Argument | Description | Format | Default |
|----------|-------------|--------|---------|
| `-d`, `--date` | Date for the reservation | `mm/dd/yyyy` | Today’s date |
| `-t`, `--time` | Time for the show | `hh:mm` (24-hour format without "pm") | `9:30` |

> Note: Time is automatically interpreted as **PM** in the script logic.

---

## ⚙️ Heroku Deployment

Your `Procfile` for Heroku should include:

```
web: python cellar.py --help
worker: python cellar.py --help
```

Add the following **Config Vars** to Heroku:

| Variable | Description |
|----------|-------------|
| `CHROMEDRIVER_PATH` | Path to ChromeDriver on Heroku |
| `GOOGLE_CHROME_BIN` | Path to the Chrome binary on Heroku |

---

## 🧪 Example

```bash
python cellar.py -e kevin@example.com -d 09/23/2025 -t 7:00
```

This will:
- Navigate to the Comedy Cellar website.
- Check for availability on Sept 23rd at 7:00pm.
- Book the reservation if available.
- Print "Sold Out" if the slot is unavailable.

---

## 🧠 Tech Stack

- [Selenium](https://www.selenium.dev/)
- [webbot](https://pypi.org/project/webbot/)
- [Heroku](https://www.heroku.com/)
- Python 3

---

## 📬 Contact

Created by **Kevin Shah**  
Feel free to fork, modify, or submit issues!

---

## 📄 License

MIT License – see [LICENSE](LICENSE) file for details.
