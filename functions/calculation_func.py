# Importing standard libraries.
from typing import List
# Importing third-party libraries.
# Importing this repository libraries.

class ParameterName():
    """ParameterName
    
    Class for defining the names of parameters to be used in the command.
    """
    # Define parameter names to be used.
    CALC_MODE = "-CALC_MODE"
    OPERAND_1 = "-OPERAND_1"
    OPERAND_2 = "-OPERAND_2"

class CalculationFunc(ParameterName):
    """CalculationFunc
    
    'Calculation' command function class.
    
    Attributes:
        COMMAND_NAME (str): This function command name
        CALC_MODE_LIST (List[str]): Calculation type
    """
    COMMAND_NAME = "calculation"
    CALC_MODE_LIST = ["ADD", "SUB"]
    
    def __init__(self) -> None:
        self.calc_mode = "ADD"
        self.operand_1 = 0
        self.operand_2 = 0
    
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
        if (name == ParameterName.CALC_MODE):
            if (param_number+1 >= len(src_param)):
                # Help is displayed due to missing set values.
                CalculationFunc.show_help(py_command, name)
                ret = False
            else:
                calc_mode = src_param[param_number + 1].upper()
                if calc_mode in CalculationFunc.CALC_MODE_LIST:
                    self.calc_mode = calc_mode
                else:
                    CalculationFunc.show_help(py_command, name, src_param[param_number + 1])
                    ret = False
        elif (name == ParameterName.OPERAND_1):
            if (param_number+1 >= len(src_param)):
                CalculationFunc.show_help(py_command, name)
                ret = False
            else:
                try:
                    self.operand_1 = int(src_param[param_number + 1])
                except ValueError:
                    CalculationFunc.show_help(py_command, name, src_param[param_number + 1])
                    ret = False
        elif (name == ParameterName.OPERAND_2):
            if (param_number+1 >= len(src_param)):
                CalculationFunc.show_help(py_command, name)
                ret = False
            else:
                try:
                    self.operand_2 = int(src_param[param_number + 1])
                except ValueError:
                    CalculationFunc.show_help(py_command, name, src_param[param_number + 1])
                    ret = False
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
            print(f"Parameter error.")
            print(f"\tParameterName -> {parameter_name}")
            print(f"\tParameterValue -> {parameter_value}")
        
        if all_display:
            # Show command broad category.
            print(f"#"*5 + " Caluculation " + "#"*5)
        print("- Calculation Value:")
        print(f"\t{py_command} {CalculationFunc.COMMAND_NAME}" +
              f" {CalculationFunc.CALC_MODE} ({CalculationFunc.CALC_MODE_LIST})" +
              f" {CalculationFunc.OPERAND_1} int_value" +
              f" {CalculationFunc.OPERAND_2} int_value")
    
    def run_function(self) -> bool:
        """Running fuction
        
        Returns:
            bool: boolean value
        """
        if (self.calc_mode == CalculationFunc.CALC_MODE_LIST[0]):
            calc_result = self.operand_1 + self.operand_2
            print(f"Calculation Result: {calc_result}")
        elif (self.calc_mode == CalculationFunc.CALC_MODE_LIST[1]):
            calc_result = self.operand_1 - self.operand_2
            print(f"Calculation Result: {calc_result}")
        return True