#! /usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
import gzip

import hashlib
import argparse


def gen_hash(email):
    return hashlib.sha256(email.lower()).hexdigest()


def read_hashes(fn):
    with gzip.open(fn) as f:
        hashes = f.read().splitlines()

    return set(hashes)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Test your imail against data from mall.cz."
    )
    parser.add_argument(
        "EMAIL",
        help="Your email."
    )

    args = parser.parse_args()

    email_hashes = read_hashes("email_hash_db.txt.gz")

    if gen_hash(args.EMAIL) in email_hashes:
        print "\033[31mWarning: Your email, password, name and phone leaked!\033[0m"
    else:
        print "\033[32mYour email was not found in the leaked data.\033[0m"
