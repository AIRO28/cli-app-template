# Importing standard libraries.
import platform
import sys
from typing import List, Callable, Optional
# Importing third-party libraries.
# Importing this repository libraries.
from functions.greeting_func import GreetingFunc
from functions.calculation_func import CalculationFunc

class FunctionalManagers(object):
    """FunctionalManagers
    
    Class that manages commands to be executed.
    
    Attributes:
        PY_FILENAME (str): Name of Python file to run
        HELP_COMMAND_NAME (str): Help command name
    """
    PY_FILENAME = "main.py" # Replace with the name of the Python file to be executed.
    HELP_COMMAND_NAME = "help"
    
    def __init__(self) -> None:
        self.command_name = ""
        self.target_command:Optional[Callable[[], bool]] = None
        self.greeting_func = GreetingFunc()
        self.calculation_func = CalculationFunc()
        # TODO:Please append here any instances for functions you wish to add.
        # self.hoge_func = HogeFunc()
    
    @classmethod
    def __get_py_command(cls) -> str:
        """Get Python execution command
        
        Returns:
            str: Python execution commands
        """
        # Get the Python version (x.x) you are running.
        py_version = str(sys.version_info[0]) +  "." + str(sys.version_info[1])
        
        # Get OS information.
        pf = platform.system()
        if pf == "Windows":
            return f"py -{py_version} {cls.PY_FILENAME}"
        elif pf == "Darwin":
            return f"python{py_version} {cls.PY_FILENAME}"
        else:
            return f"python{py_version} {cls.PY_FILENAME}"
    
    def parameter_parsing(self, params:List[str]=[]) -> bool:
        """Parse parameters
        
        Args:
            params (List[str], optional): parameter. Defaults to [].
        
        Returns:
            bool: boolean value
        
        Note:
            Add the argument analysis for the commands you have added yourself.
        """
        py_command = self.__get_py_command()
        ret = True
        
        if (len(params) > 0):
            for param_number in range(len(params)):
                if (param_number == 0):
                    # Get Execution Command.
                    self.command_name = params[param_number].lower()
                else:
                    # Perform argument analysis according to each execution command.
                    if (self.command_name == GreetingFunc.COMMAND_NAME):
                        ret = self.greeting_func.parameter_parsing(py_command, params, param_number)
                    elif (self.command_name == CalculationFunc.COMMAND_NAME):
                        ret = self.calculation_func.parameter_parsing(py_command, params, param_number)
                    # TODO:Argument analysis for functions you wish to add should be appended.
                    # elif (self.command_name == HogeFunc.COMMAND_NAME):
                        # ret = self.hoge_func.parameter_parsing(py_command, params, param_number)
                    else:
                        # A nonexistent execution command is specified.
                        print("A nonexistent command is specified!")
                        self.show_help_command()
                        return False
        else:
            # Parameters not set.
            print("Required arguments for command line execution are not set!")
            self.show_help_command()
            return False
        
        # Based on the analysis results, commands to be executed are extracted.
        if not self.__command_selecter():
            # No corresponding command exists.
            print("No corresponding command exists.")
            self.show_help_command()
            return False
        
        return ret
    
    def show_help_command(self) -> bool:
        """All help display commands
        
        Returns:
            bool: boolean value
        
        Note:
            Add help functions for the commands you have added.
        """
        py_command = self.__get_py_command()
        
        GreetingFunc.show_help(py_command, "", "", True, False)
        CalculationFunc.show_help(py_command, "", "", True, False)
        # TODO:Add help functions for the commands you have added.
        # HogeFunc.show_help(py_command, "", "", True, False)
        return True
    
    def __command_selecter(self) -> bool:
        """Selection of commands to be executed.
        
        Returns:
            bool: boolean value
        Note:
            Set the run_function method of the added command.
        """
        selecter = {
            FunctionalManagers.HELP_COMMAND_NAME: self.show_help_command, 
            GreetingFunc.COMMAND_NAME: self.greeting_func.run_function,
            CalculationFunc.COMMAND_NAME: self.calculation_func.run_function,
            # TODO:Set the run_function method of the added command.
        }
        
        self.target_command = selecter.get(self.command_name, None)
        if self.target_command is None:
            # Returns False if the corresponding command does not exist.
            return False
        return True
    
    def execute_command(self) -> bool:
        """Execute target command.
        
        Returns:
            bool: boolean value
        """
        if not self.target_command is None:
            return self.target_command()
        return False
    
if __name__ == "__main__":
    func_manager = FunctionalManagers()
    # ret = func_manager.parameter_parsing([])
    ret = func_manager.parameter_parsing(["help"])
    # ret = func_manager.parameter_parsing(["helpoo"])
    # ret = func_manager.parameter_parsing(["helpoo", "p"])
    # ret = func_manager.parameter_parsing(["greeting", "-Mesae", "Hello", "-First_Name", "Tanaka", "-Last_name", "Takashi"])
    # ret = func_manager.parameter_parsing(["greeting", "-Message", "Hello", "-First_Name", "Tanaka", "-Last_name", "Takashi"])
    # ret = func_manager.parameter_parsing(["calculation", "-calc_mode", "add", "-OPERAND_1", "1", "-OPERAND_2", "2"])
    if ret:
        func_ret = func_manager.execute_command()
    else:
        exit(1)
    
    if not func_ret:
        exit(1)
    exit(0)