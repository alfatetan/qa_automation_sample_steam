# Example QA framework for Steam (Video Games Store)

#### :bangbang: Note: This framework in the process of creating

## Installation

#### Requirements:

- Any Unix/Linux OS (MacOS, Ubuntu, Debian, CentOS, RedHat, Archlinux, etc.)
- Google Chrome last version
- Installed Python interpreter version 3.9 or higher
- Opened Terminal and your fingers :stuck_out_tongue_winking_eye:
- That's it!

#### Steps (in the terminal window):

- Clone this repository:

```bash
$ git clone https://github.com/alfatetan/qa_automation_sample_steam.git && cd qa_automation_sample_steam
```

- Install Python virtual environment and activate it

```bash
$ python -m venv ./.venv
$ source ./.venv/bin/activate

# Try to check if the Python interpreter has been activated correctly
$ which python

# It should show the path to the current pythons interpreter in ".../qa_automation_sample_steam/.venv/bin/python"
```

- Install necessary libraries

```bash
$ pip install -r requirements.txt

# Check the list of libraries
$ pip list

# The list should looks like this:
Package               Version
--------------------- -----------
allure-behave         2.13.2
allure-python-commons 2.13.2
attrs                 23.2.0
behave                1.2.6
certifi               2023.11.17
charset-normalizer    3.3.2
exceptiongroup        1.2.0
h11                   0.14.0
idna                  3.6
iniconfig             2.0.0
outcome               1.3.0.post0
packaging             23.2
parse                 1.20.0
parse-type            0.6.2
pip                   22.0.4
pluggy                1.4.0
PySocks               1.7.1
pytest                8.0.0
python-dotenv         1.0.0
requests              2.31.0
selenium              4.16.0
setuptools            58.1.0
six                   1.16.0
sniffio               1.3.0
sortedcontainers      2.4.0
tomli                 2.0.1
trio                  0.24.0
trio-websocket        0.11.1
urllib3               2.1.0
webdriver-manager     4.0.1
wsproto               1.2.0
```

## Running tests

<!-- TODO: *** Here I'll write how the tests should be run -->
