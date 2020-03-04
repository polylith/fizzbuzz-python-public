# FizzBuzz Python
This repository is for demonstration how a python task on the EntwicklerHeld.de platform works.

## File
### fizzbuzz package
In this package are the main Python files for the challenge. It mainly consists of: `tests.py` which contains all tests for the platform and a `task.py` which is the file where the user writes the code.

### flowfile.xml
The `flowfile.xml` is the description of the task. It consists of two parts: the `<feature>` part where the scenarios are described and the `<mappings>` where the Features from above are mapped to code. 

### Other Files
The other files descibe the enviroment of the challenges and handle the test excecution. The `Dockerfile.*` describe the environment of the user on the platform. The `Makefile` and the `platform_test.sh` run the tests and gather the results. 
