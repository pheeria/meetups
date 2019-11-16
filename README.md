# Meetups

[![made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![winter-is-coming](https://ForTheBadge.com/images/badges/winter-is-coming.svg)](https://ForTheBadge.com)

Meetups is a simple events calendar app. Given a `no_later_than` date and a `meetups` list it will generate a markdown file with a list of upcoming events.

## Usage

1. Clone the repo

1. Create a virtual environment

   ```sh
   python3 -m venv env
   ```

1. Activate the environment

   ```sh
   source env/bin/activate
   ```

1. Install dependencies

  ```sh
  pip install -r requirements.txt
  ```

1. Modify `config.json` according to your needs

1. Run `python meetup.py`
