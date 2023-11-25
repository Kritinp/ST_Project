Commands
To run tests:
$ python3 -m unittest tests\test_*

To run mutation testing:
$ mut.py --target chess --unit-test tests/ --operator AOR

To get coverage information:
$ coverage run -m unittest tests/test_*
$ coverage report