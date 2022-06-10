# Importing standard libraries.
from typing import List
# Importing third-party libraries.
# Importing this repository libraries.

class ParameterName():
    """ParameterName
    
    Class for defining the names of parameters to be used in the command.
    """
    # Define parameter names to be used.
    # TODO:Add the name of the parameter to be used.
    HOGE = "-HOGE"

# Template for command functions.
class HogeFunc(ParameterName):
    """HogeFunc
    
    'Hoge' command function class that serves as a template.
    """
    COMMAND_NAME = "hoge"   # TODO:Replace command names as necessary
    # TODO:Add class variables as needed.
    
    def __init__(self) -> None:
        # TODO:Define the parameter parsed setting values as instance variables.
        self.hoge = ""
    
    def parameter_parsing(self, py_command:str, src_param:List[str], param_number:int) -> bool:
        """Parse parameters
        
        Args:
            py_command (str): Python execution commands
            src_param (List[str]): Parameter List
            param_number (int): Parameter number to parse
        
        Returns:
            bool: boolean value
        
        Note:
            Describe the necessary parameter analysis process according to the command to be added.
        """
        # Parameter names are handled in uppercase.
        name = src_param[param_number].upper()
        
        # Get a set value for each parameter name.
        ret = True
        if (name == ParameterName.HOGE):
            if (param_number+1 >= len(src_param)):
                # Help is displayed due to missing set values.
                HogeFunc.show_help(py_command, name)
                ret = False
            else:
                self.hoge = src_param[param_number + 1].upper()
        # TODO:Add a process for acquiring setting values for each added parameter.
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
        
        Note:
            Describe the necessary help messages according to the commands to be added.
        """
        # Display error due to invalid parameter.
        if err:
            print(f"Parameter error.")
            print(f"\tParameterName -> {parameter_name}")
            print(f"\tParameterValue -> {parameter_value}")
        
        # TODO:Describe the necessary help messages according to the commands to be added
        if all_display:
            # Show command broad category.
            print(f"#"*5 + " Hoge " + "#"*5)
        print("- Hoge function:")
        print(f"\t{py_command} {HogeFunc.COMMAND_NAME} {HogeFunc.HOGE} str_value")
    
    def run_function(self) -> bool:
        """Running fuction
        
        Returns:
            bool: boolean value
        
        Note:
            Describe the command process you actually want to execute.
        """
        # TODO:Describe the command process you actually want to execute
        pass
        return True