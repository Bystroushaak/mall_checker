#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
import gzip

import hashlib
import argparse
import csv


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

def checkEmail(email, email_hashes):
    return gen_hash(email) in email_hashes

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
        print "\033[31mWarning: List of leaked emails\033[0m"
        for email in read_csv(args.csvFile):
            if checkEmail(email[0], email_hashes):
                print "\033[31m{}\033[0m".format(email[0])
    else:
        if checkEmail(args.email, email_hashes):
            print "\033[31mWarning: Your email {}, password, name and phone leaked!\033[0m".format(args.email)
        else:
            print "\033[32mYour email {} was not found in the leaked data.\033[0m".format(args.email)
