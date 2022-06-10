# Importing standard libraries.
import sys
from typing import List
# Importing third-party libraries.
# Importing this repository libraries.
from functional_managers import FunctionalManagers

def main(argv:List[str]) -> bool:
    
    # Parse parameters specified on command line.
    func_manager = FunctionalManagers()
    if not (func_manager.parameter_parsing(argv)):
        return False
    
    # Execute command.
    return func_manager.execute_command()

if __name__ == "__main__":
    if (main(sys.argv[1:])):
        exit(0)
    else:
        exit(1)