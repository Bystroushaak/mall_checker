#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
from __future__ import print_function

import csv
import gzip
import hashlib
import argparse


def gen_hash(email):
    return hashlib.sha256(email.lower()).hexdigest()


def read_csv(csvFile):
    with open(csvFile, 'rb') as f:
        reader = csv.reader(f)
        return list(reader)


def read_hashes(fn):
    with gzip.open(fn) as f:
        hashes = f.read().splitlines()

    return set(hashes)


def check_email(email, email_hashes):
    return gen_hash(email) in email_hashes


def print_red(msg, *args, **kwargs):
    print("\033[31m%s\033[0m" % msg, *args)


def print_green(msg, *args, **kwargs):
    print("\033[32m%s\033[0m" % msg, *args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Test your email or CSV file with emails against data from mall.cz."
    )
    parser.add_argument(
        "--email",
        help="Your email."
    )
    parser.add_argument(
        "--csvFile",
        help="A CSV file with emails to be checked (email must appear at the first column)"
    )

    args = parser.parse_args()

    email_hashes = read_hashes("email_hash_db.txt.gz")

    if args.csvFile:
        print_red("Warning: List of leaked emails;")
        for email in read_csv(args.csvFile):
            if check_email(email[0], email_hashes):
                print_red(email[0])
    else:
        if check_email(args.email, email_hashes):
            print_red("Warning: Your email (%s), password, name and phone leaked!" % args.email)
        else:
            print_green("Your email (%s) was not found in the leaked data." % args.email)
