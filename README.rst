MALL.cz leak checker
````````````````````

Check your email address(es) against leaked MALL.cz database and print result to standard output.

Usage:
::
  -h, --help         show this help message and exit
  --email EMAIL      Your email.
  --csvFile CSVFILE  A CSV file with emails to be checked (email must appear
                     at the first column)
::

Examples:

Check single email

::

    ./check_email.py --email john.doe@example.com


Check multiple emails

::

    ./check_email.py --csvFile emails.csv

Manual check
````````````
You can also check the database manually, if you don't want to use provided script::

  $ echo -n email@seznam.cz | sha256sum
  24cc40d8994889305521a1c1662a6ce1c51ea7086ea771992ba470453c798eac  -
  $ zgrep 24cc40d8994889305521a1c1662a6ce1c51ea7086ea771992ba470453c798eac email_hash_db.txt.gz 
  24cc40d8994889305521a1c1662a6ce1c51ea7086ea771992ba470453c798eac

Why
```

There is a lot of people, who don't trust MALL.cz and their verification form, because they suspect the company from damage controll activities. I have access to the leaked data and I decided to make this script, which checks your email against the leaked dataset.

This repository doesn't contain any leaked sensitive information, just a list of leaked email addresses hashed by sha256, against which is your email checked.

You may use this script (and the DB) under the MIT licence.
