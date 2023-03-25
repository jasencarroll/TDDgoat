# TDDgoat

[Test-Driven Development with Python](https://learning.oreilly.com/covers/urn:orm:book:9781491958698/400w/) has not been updated since 2017 though I've always regretted not finishing it entirely. The idea of writing tests to fail before writing passing criteria really resonates with me on so many levels. Simply from an applied scientist perspective, one shall hypthosize before testing to determine if their hypothesis was correct - that's more of like a business approach and comes down to luck. 

## Installation

Getting this going might not be that simple. The book was written using python3.6 and I am on 3.9 and 3.10. I know some especially funky stuff breaks on 3.10.

For starters, while you're inside the project folder, install `pipenv` with the following:
```bash
$ python3 -m pip install pipenv
$ pipenv shell
```

This will build you a pipenv and activate it after installing.

I immediately had a hard time with Firefox. Initially it couldn't find the binary. The first code that began to fail as expected was as follows.

```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options=Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/Firefox.exe"

browser = webdriver.Firefox(options=options)
browser.get('http://127.0.0.1:8000')

assert 'Django' in browser.title
```

In fact, the older `localhost:8000` was also failing but I'm proceeding with so much caution here that I started to troubleshoot before recognizing the book had intended a failure there with Firefox intentionally not connecting to the server.

Now that we have a failing test, we can get started building out our application. Trying to run a development server I had issues with Django not being on PYTHONPATH however I think that was resoved by running `django-admin help`.

[`django.conf.urls.url()` was deprecated in Django 3.0, and is removed in Django 4.0+.](https://stackoverflow.com/questions/70319606/importerror-cannot-import-name-url-from-django-conf-urls-after-upgrading-to)

Oh yes, we will learn a lot this time.