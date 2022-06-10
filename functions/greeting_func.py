# Importing standard libraries.
from typing import List
# Importing third-party libraries.
# Importing this repository libraries.

class ParameterName():
    """ParameterName
    
    Class for defining the names of parameters to be used in the command.
    """
    # Define parameter names to be used.
    MESSAGE = "-MESSAGE"
    FIRST_NAME = "-FIRST_NAME"
    LAST_NAME = "-LAST_NAME"
    OPTION = "-OPTION"

class GreetingFunc(ParameterName):
    """GreetingFunc
    
    'Greeting' command function class.
    
    Attributes:
        COMMAND_NAME (str): This function command name
    """
    COMMAND_NAME = "greeting"
    
    def __init__(self) -> None:
        self.message = "Hello"
        self.first_name = "Tanaka"
        self.last_name = "Takashi"
        self.option = False
    
    def parameter_parsing(self, py_command:str, src_param:List[str], param_number:int) -> bool:
        """Parse parameters
        
        Args:
            py_command (str): Python execution commands
            src_param (List[str]): Parameter List
            param_number (int): Parameter number to parse
        
        Returns:
            bool: boolean value
        """
        # Parameter names are handled in uppercase.
        name = src_param[param_number].upper()
        
        # Get a set value for each parameter name.
        ret = True
        if (name == ParameterName.MESSAGE):
            if (param_number+1 >= len(src_param)):
                # Help is displayed due to missing set values.
                GreetingFunc.show_help(py_command, name)
                ret = False
            else:
                self.message = src_param[param_number + 1]
        elif (name == ParameterName.FIRST_NAME):
            if (param_number+1 >= len(src_param)):
                GreetingFunc.show_help(py_command, name)
                ret = False
            else:
                self.first_name = src_param[param_number + 1]
        elif (name == ParameterName.LAST_NAME):
            if (param_number+1 >= len(src_param)):
                GreetingFunc.show_help(py_command, name)
                ret = False
            else:
                self.last_name = src_param[param_number + 1]
        elif (name == ParameterName.OPTION):
            self.option = True
        return ret
    
    @staticmethod
    def show_help(py_command:str, parameter_name:str="", parameter_value:str="", all_display:bool=False, err:bool=True) -> None:
        """Show help messages
        
        Args:
            py_command (str): Python execution commands
            parameter_name (str): Parameter name. Defaults to "".
            parameter_value (str, optional): Set value for parameter. Defaults to "".
            all_display (bool, optional): All display mode. Defaults to False.
            err (bool, optional): Error flag. Defaults to True.
        
        """
        # Display error due to invalid parameter.
        if err:
            print(f"Parameter error!")
            print(f"\tParameterName -> {parameter_name}")
            print(f"\tParameterValue -> {parameter_value}")
        
        if all_display:
            # Show command broad category.
            print(f"#"*5 + " Greeting " + "#"*5)
        print("- Greeting Message:")
        print(f"\t{py_command} {GreetingFunc.COMMAND_NAME}" +
              f" {GreetingFunc.MESSAGE} message_value" +
              f" {GreetingFunc.FIRST_NAME} str_value" +
              f" {GreetingFunc.LAST_NAME} str_value" +
              f"[{GreetingFunc.OPTION}]")
    
    def run_function(self) -> bool:
        """Running fuction
        
        Returns:
            bool: boolean value
        """
        print(f"Hi!{self.last_name} {self.first_name}. {self.message}")
        return True