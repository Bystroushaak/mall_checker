MALL.cz leak checker
````````````````````

Check your email address against leaked MALL.cz database.

Usage:

::

  ./check_email.py CENSORED@seznam.cz
  Warning: Your email, password, name and phone leaked!

Or:

::

  ./check_email.py bleh@bleh.bleh
  Your email was not found in the leaked data.

Why
```

There is a lot of people, who don't trust MALL.cz and their verification form, because they already lied a few times about the leak. I have access to the leaked data and I decided to make this script, which checks your email against the leaked dataset.

This repository doesn't contain any sensitive leaked information, just a list of leaked email addresses hashed by sha256, against which is your email checked.

You may use this script under the MIT licence.
