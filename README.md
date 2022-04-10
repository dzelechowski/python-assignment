**This repository contains tests performing CRUD operations on clients**

In order to run tests, please check the e-mail with the basic auth credentials.

Tests can be run:
directly by using pytest command. 
```
BASIC_AUTH={credentials} pytest tests/test_clients.py -vv
```
or docker
```
docker build --tag clients-tests .
docker run -e BASIC_AUTH={credentials} clients-tests
```

Ideas for improving the tests:
* checking "unhappy paths"
* using Mypy
* integration with CI
* creating env.tpl
* storing credentials in a server and getting them by being authorized
