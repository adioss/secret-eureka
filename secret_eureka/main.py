import argparse
import logging


def any_method():
    """" any method """
    return "changeme"


def main():
    """ main """
    parser = argparse.ArgumentParser(description='changeme')
    parser.add_argument('--configuration-file', type=str, required=False, help='Config file')
    parser.add_argument("--log-level", default=logging.INFO, type=lambda x: getattr(logging, x),
                        help="Configure the logging level.")
    print(f"All the {any_method()} starting here.")


if __name__ == '__main__':
    main()
