# Strings and Variables

## Multiple Variable Assignment

When assigning variable in python, you can assign multiple variable in a one liner.
eg. `name, date, temp = 'Julie', 'Saturday', '75'` or `a, b, c = c, b, a`
This is commonly done to swap values. However, how does it work?


The right side of the assignment `'Julie', 'Saturday', '75'` is evaluated first and stored in temp memory allocation.
This in turn will return the right side as a tuple first (which is immutable) and then it evaluate the left side.
Then since the left side is mutable it will then replace the current value with the new temp value.

So something like this:
```Python
temp = a
a = b
b = temp
```
Can be turn into something like this:
```Python
a, b = b, a
```



---
## Methods (String Methods)

| Method Name  | Description  |
|---|---|
| `string.upper()`  | turn string into upper case  |
| `string.lower()`  | turn string into lower cas  |
| `string.islower()`  | boolean if a string is lower case  |
| `string.isupper()`  | boolean if a string is lower case  |
| `string.isalpha()`  | boolean if string is letters only  |
| `string.isalnum()`  | boolean if letters and numbers only  |
| `string.isdecimal()`  | boolean if numbers only  |
| `strings.isspace()`  | boolean if white space only  |
| `strings.istitle()`  | boolean if titlecase only (begin with uppercase and follow with all lowercase)  |
| `strings.startswith()` | boolean if a string begin with target string |
| `strings.endswith()` | boolean if a string ends with target string |
| `''.join()` | join together a list of string with whatever string between them that the method is call on |
| `string.split()` | Call on a string value and return a list of string, split on whitespace char as default (can be change by passing in value eg. `string.split(',')`) |
| `string.ljust()` | return a padded version of a string that they're call on with space to the left justify of text |
| `string.rjust()` | return a padded version of a string that they're call on with space to the right justify of text |
| `string.center()` | return a padded version of string with text in center eg. `'hi'.center(10, '=')` >>> '====hi===='|
| `string.strip()` | return a string that have whatever is passed into the method striped off (whitespace as default) |
| `string.rstrip()` | return a string that have white space remove from right |
| `string.lstrip()` | return a string that have white space remove from left |
| `string.replace('abc', 'xyz')` | return a string that have whatever target string to replace with another target string `replace('toReplace', 'replaceWith')` |

---

## String Formatting
* Python let us put a `%s` inside of a string to mark where we want to have other string inserted into it. It is just for readability.

eg.
---
`name, date, temp = 'Julie', 'Saturday', '75'`

`'Hello! %s, today is %s and it is %s degree in the forecast.' % (name, date, temp)`
