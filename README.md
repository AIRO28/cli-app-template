# Module name
cli app template

# Overview
This module serves as a template for creating CLI applications.  
It enables processing to be executed in response to arbitrary commands.  

# Dependency libraries and packages
```
None
```

# How to use
Using `template_func.py` as a template, add the necessary processing according to the TODOs in each file.  
By adding the command processing to be executed and the accompanying parameter parsing process to the file to be written, a CLI application can be easily implemented.  

`greeting_func.py` and `calculation_func.py` are samples.  

## ・Python

```python
# Execute help commands.
$ python main.py help
##### Greeting #####
- Greeting Message:
        python3.9 main.py greeting -MESSAGE message_value -FIRST_NAME str_value -LAST_NAME str_value[-OPTION]
##### Caluculation #####
- Calculation Value:
        python3.9 main.py calculation -CALC_MODE (['ADD', 'SUB']) -OPERAND_1 int_value -OPERAND_2 int_value

# Execute the greeting message command.
$ python main.py greeting -Message "Nice to meet you." -First_Name "Tanaka" -Last_name "Takashi"
Hi!Takashi Tanaka. Nice to meet you.

# Execute calculation command.
$ python main.py calculation -calc_mode add -OPERAND_1 1 -OPERAND_2 2
Calculation Result: 3

```