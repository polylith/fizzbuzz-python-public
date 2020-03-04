# FizzBuzz Python
This repository is for demonstration how a python task on the EntwicklerHeld.de platform works.

## Files
### fizzbuzz package
In this package are the main Python files for the challenge. It mainly consists of: `tests.py` which contains all tests for the platform and a `task.py` which is the file where the user writes the code.

### flowfile.xml
The `flowfile.xml` is the description of the task. It consists of two parts: the `<feature>` part where the scenarios are described and the `<mappings>` where the Features from above are mapped to code. 

### requirements.txt
In the requirements.txt all needed libraries are listet. 

### Other Files
The other files descibe the enviroment of the challenges and handle the test excecution. The `Dockerfile.*` describe the environment of the user on the platform. The `Makefile` and the `platform_test.sh` run the tests and gather the results. 


## Code style
We try to write good and readable Python-Code and fulfill common best-practices in all our challenges. This includes descriptive variable and function naming (e.g. `number` instead of `n`). Please report if you find a Challenge when you think this is not the case. 

### Type Annotations
In Python we always use type-annotations (`def fizzbuzz(int: number):` instead of `def fizzbuzz(number):` see <a href ="https://www.python.org/dev/peps/pep-0484/">PEP-0484</a>) for better readability and better code completion on the platform. Please always use type-annotations for arguments in EntwicklerHeld Challenges.
