# Unconcealment

Tool to detect secrets (AWS, GCP or AZURE keys, NPM tokens etc...)

## Badges

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![PyPI version](https://badge.fury.io/py/unconcealment.svg)](https://badge.fury.io/py/unconcealment)
[![ci](https://github.com/adioss/unconcealment/actions/workflows/ci.yml/badge.svg)](https://github.com/adioss/unconcealment/actions/workflows/ci.yml)
[![cd](https://github.com/adioss/unconcealment/actions/workflows/cd.yml/badge.svg)](https://github.com/adioss/unconcealment/actions/workflows/cd.yml)
[![security](https://github.com/adioss/unconcealment/actions/workflows/security.yml/badge.svg)](https://github.com/adioss/unconcealment/actions/workflows/security.yml)

## Usage/Examples

```bash
# help 
docker run -ti --rm adioss/unconcealment:latest -h                                             
usage: main.py [-h] [-f FILE] [-d DIRECTORY] [-l LOG_LEVEL] ...

Detect secrets (AWS, GCP or AZURE keys, NPM tokens etc...)

positional arguments:
  remainder                             input from stdin

optional arguments:
  -h, --help                            show this help message and exit
  -f FILE, --file FILE                  input file
  -d DIRECTORY, --directory DIRECTORY   input directory
  -l LOG_LEVEL, --log-level LOG_LEVEL   configure the logging level.
```

### Samples

```bash
# using input from stdin
docker run -ti --rm adioss/unconcealment:latest here some text that contains secrets like "ENV AWS_SECRET_ACCESS_KEY=4FcmDrL8tJ7jx8poyV0L5GOVqabM/abdefHQREOH"
# using file as input
docker run -ti --rm -v ${PWD}:/mnt adioss/unconcealment:latest -f /mnt/anyfile.txt
# using files as input from directory (recursive)
docker run -ti --rm -v ${PWD}:/mnt adioss/unconcealment:latest -f /mnt
```

## Running Tests

To run tests, run the following command

```bash
   poetry run python -m unittest discover -p "test_*.py"
```

## Run Locally

Clone the project

```bash
  git clone git@github.com:adioss/unconcealment.git
```

Go to the project directory

```bash
  cd unconcealment
```

Install poetry and install dependencies

```bash
  poetry self update
  poetry install
```

Start

```bash
  poetry run python unconcealment/main.py 
```

## Documentation

[TODO](https://linktodocumentation)

## Contributing

Contributions are always welcome!

See [CONTRIBUTING.md](CONTRIBUTING.md) for ways to get started.

Please adhere to this project's [`code of conduct`](CODE_OF_CONDUCT.md).

## Authors

- [@adioss](https://www.github.com/adioss)

## Acknowledgements

- TODO

## Support

For support, create a ticket [https://www.github.com/adioss](https://www.github.com/adioss)