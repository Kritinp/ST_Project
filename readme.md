Commands
To run tests:
$ python3 -m unittest tests/test_*

To run mutation testing:
$ mut.py --target chess --unit-test tests/ --operator AOR

To get coverage information:
$ coverage run -m unittest tests/test_*
$ coverage report


Integration testing:
$ mut.py --target chess --unit-test tests/test_* --operator IOD SCI CDI SVD

Unit Testing:
mut.py --target chess --unit-test tests/test_* --operator ASR COI SDI COD