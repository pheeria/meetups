# Meetups

<img height="200" alt="Meetups" style="display: block; margin: auto;" src="https://user-images.githubusercontent.com/15848876/68985173-e73b1b00-0814-11ea-9801-fc34f14d2622.png">

[![made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![winter-is-coming](https://ForTheBadge.com/images/badges/winter-is-coming.svg)](https://ForTheBadge.com)

Meetups is a simple events calendar app. Given a `no_later_than` date and a `meetups` list it will generate a markdown file with a list of upcoming events. You can see an example [here](example.md).

<img width="466" alt="Example" style="display: block; margin: auto;" src="https://user-images.githubusercontent.com/15848876/68985165-d8ecff00-0814-11ea-8fbe-c2c776c54078.png">


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
