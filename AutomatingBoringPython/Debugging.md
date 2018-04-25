# [Raise and Assert Errors](https://automatetheboringstuff.com/chapter10/)

## Raising Errors & Raise Statement

* You can raise your own error using the `raise Exception('Error Message')` or `raise ValueError('Error Message')`
  when you run into an edge case that you know will pop up either when the program cant process the data or from bad user input.

  * Program will crash and stop
  * This will help you trace back bad code or bugs inside your program early.

* You can also use the `traceback` module to write error call stack message from the Traceback as a string value to your own error_log.txt  

  * This help you have a record of all bugs and not lose any of them.

## Assertions & assert Statement

* Assertions are sanity checks where you're making sure your code is not doing something obviously wrong.

  * They are performed by the assert Statement
  * If assert return False then it will raise an error
  * To put it simply, an assert statement's condition need to always hold true, else there is a bug.
  * Assert statement are usually for programmer's way to check bugs

## Logging

* Use to understand what is going on in your code (Similar to **print statement** and is meant for development stage, not production)

* You can use the `logging` module for python.
  * Set up code
  ```python
  import logging
  logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
  ```

* One advantage this have over print function is that there is a way to disable all the logging messages with `logging.disable(logging.CRITICAL)`

* There are 5 Log Levels. (Debug, info, warning, error, critical)

* You can also write the logs into a txt files by adding `filename = 'logFilename.txt'` as an argument in the basic basicConfig code


## Debugger

* Using the debugger can help you go through line by line, variable by variable to see each values and codes of your program.

* This will help you identify deeply rooted bug that may not be picked up by exception/Assert errors. (Common bugs are type errors etc.)
