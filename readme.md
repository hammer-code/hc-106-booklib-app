# book-lib-app

Sample App for Web Development w/ Python Class [HC-106]. [Demo](http://book-lib-app.hammercode.org)

The goal of this class is to make the participants know how to develop a simple web application with python, combining the knowledge of previous classes:
- HC-101 Intro to Programming
- HC-102 Web I: HTML & CSS
- HC-103 Web II: Intro to JS
- HC-104 Linux, Git and Github
- HC-105 Intro to SQL Database 

## Requirements
- python 3.6
- pipenv

## Development
- Create venv `pipenv --python 3.6` (Skip if it's there already)
- Run shell `pipenv shell`
- Install dependencies `pipenv install`
- Create mysql database, name it `book-lib-app`
- Import sql dump in `dump.sql`
- Copy `.env` file. Run `cp .env.example .env` and change the values in the file accordingly
- Run `./dev.sh` to start the server locally

## Deployment to server
TBD

## Todo
- Update to python 3.8
- Provide vps deployment steps
