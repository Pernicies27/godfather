# godfather
Mafia moderator bot for Telegram

## Setup
Clone this repository.

It's strongly recommended to create a virtual environment for this project.
If you are using virtualenvwrapper, create a new environment using `$ mkvirtualenv godfather`.
Otherwise, run `$ virtualenv .virtualenv` in the project root folder and add `.virtualenv/` to your `.git/info/exclude`.

You can activate your new environment with `$ workon godfather` (virtualenvwrapper) or `$ source .virtualenv/bin/activate` (if you don't use virtualenvwrapper).

After that, do the following to install the necessary dependencies:

`
$ pip3 install -r requirements.txt
`

## Running godfather
To start the bot, run the following command in your project root folder:

`
$ python3 godfather
`

## Running the tests
Run `$ pytest tests` .
