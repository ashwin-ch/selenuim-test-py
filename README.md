# Selenium based VGT

## Introduction
In this project we will be testing a website using Selenium framework, which helps us to
automate the test cases automatically. Selenium provides a webdriver, which has the capability
to access different parts of the webpages using id, tags, names, etc,.
In this project, we have used http://the-internet.herokuapp.com as our System under test(SUT).
We will test the static contents like heading and title and then test some functionality of the
website using Selenium-webdriver.

## Instructions

To activate a virtual environment(optional),
```python3 -m venv .virtual```

To install dependencies,
```pip3 install -r requirements.txt -I```

 Run test cases using the below command
```pytest --browser <chrome/firefox> --env <qa/dev/prod>```

_Optional argument_
``` -k <test-case-id>```


## Report
Test verification reports are generated using `pytest-html` module.
