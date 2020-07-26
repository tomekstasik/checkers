# Checkers

Strategy board game for two players.
Both players make diagonal moves of uniform game pieces and mandatory captured by jumping over opponent pieces.

## Development
```sh
$ git clone https://github.com/tomekstasik/checkers
$ cd checkers
$ virtualenv venv
$ venv\Scripts\activate
$ python setup.py develop
```

## Run server
```sh
$ cd checkers
$ docker-compose up --build
```

## Run client
```sh
$ cd checkers/client
$ python run.py
```

## Tests
```sh
$ py.test test
```

