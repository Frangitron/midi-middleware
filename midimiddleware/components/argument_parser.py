import argparse
import logging

from midimiddleware.core.components import Components

_logger = logging.getLogger(__name__)


def parse_args() -> None:
    parser = argparse.ArgumentParser()

    # parser.add_argument(
    #     "-v", "--verbose", action="store_true",
    #     help="Show more log messages"
    # )
    # arguments = parser.parse_args()
    #
    # Components().configuration.is_verbose = arguments.verbose
