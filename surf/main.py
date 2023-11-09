#!/usr/bin/env python3
"""
Surf Boto, with style.
"""

__author__ = "Sam Holden"
__version__ = "0.1.0"
__license__ = "MIT"

from logzero import logger
import surf
import boto3
import inspect


def main():
    """ """
    logger.info("init session...")
    session = boto3.session.Session()
    logger.info("init surfer...")
    surfer = surf.Surf(session)

    surfer.service = 's3'
    # surfer.service = surfer.all_services[2]
    # print(surfer.all_methods)

    method = surfer.all_methods[5]

    method_to_inspect = getattr(surfer.client, method)

    print(f'service: {surfer.service}, method: {method}')

    argspec = inspect.getfullargspec(method_to_inspect)
    args = argspec.args
    print(args)

    # for parameter_name, parameter in parameters.items():
    #     print(parameter_name)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()