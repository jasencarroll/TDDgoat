# TDDgoat

![Test-Driven Development with Python](https://learning.oreilly.com/covers/urn:orm:book:9781491958698/400w.jpg) 

**Test-Driven Development with Python** has not been updated since 2017 though I've always regretted not finishing it entirely. The idea of writing tests to fail before writing passing criteria really resonates with me on so many levels. Simply from an applied scientist perspective, one shall hypthosize before testing to determine if their hypothesis was correct - that's more of like a business approach and comes down to luck. 

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

Oh yes, we will learn a lot this time. Actually the author had us install Django < 4 so it was me being willy nilly and typing pip install django that got things to start but giving me a new error. I need to uninstall Django from my system now.

Checking my path of django-admin using `where` and also what `--version` was pulled down it looks like somehow I grabbed >4. when the author's requirements were <1.12. Looking up [Django's documentation on release cycles](https://www.djangoproject.com/download/) it looks like the oldest thing still supported is 3.2.18 so we'll use that. Quickly referencing [Selenium versions](https://rubygems.org/gems/selenium-webdriver/versions) (note: that was for ruby releases but shouldn't matter too much) it looks like 4.0.0 came out around the same time as the Django release we're using so let's see if that leads to success. While we're at it there is no reason to play with Python 3.9 and 3.10. The oldest version still supported is 3.7 and you can use your favorite way of obtaining that. I will say the Microsoft Store seems to work well, though the search query never pulls the right version you're asking for - as if they're promoting 3.10...

![LIFT OFF!](https://github.com/jasencarroll/TDDgoat/blob/main/images/Screenshot%202023-03-25%20071444.png)

Now that we have the development server running let's figure out what's up with the `functional_tests.py`.

I'm having a hard time getting Selenium to connect. From versions 3.2 through 4.8.

It wasn't actually that Selenium was having a hard time connecting. First I troubleshoot with Chrome and when that didn't work I eventually just tried to get Selenium to connect to Google. It worked. Then I started undoing my code to go back to Firefox and get as close to the author's intent. Now I have to figure out what is wrong with the geckodriver or something. I tried chromedriver too and that didn't work. I turned off Microsoft Defender Firewall and nothing.

Firefox will crash land at localhost. Chrome will pop up and dissapear. 