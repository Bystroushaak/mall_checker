#! /usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
import gzip

from tqdm import tqdm

from check_email import gen_hash


def parse_email(line):
    line = line.split("#")[0]

    email = line.split(":")[0]

    return email.strip()


def read_custommer_list(fn):
    with open(fn) as f:
        for line in f:
            email = parse_email(line)

            if email:
                yield email


if __name__ == '__main__':
    email_db = set()

    for email in read_custommer_list("customers.txt"):
        email_db.add(email)

    with gzip.open("email_hash_db.txt.gz", "wb") as f:
        for email in tqdm(email_db):
            email_hash = gen_hash(email)
            f.write(email_hash + "\n")
