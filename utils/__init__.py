"""
Prevent import this module indside a forbidden folder
"""

import os
import sys

# Folder from which importing is forbidden
forbidden_folder_name = "src"
mypackage = "utils" # module name

main = sys.modules.get("__main__")
caller_file = getattr(main, "__file__", None)

if caller_file is not None:
    caller_file = os.path.abspath(caller_file)

    # Check all parent folders of the caller
    parts = caller_file.split(os.sep)

    if forbidden_folder_name in parts:
        raise ImportError(
            f"'{mypackage}' cannot be imported from inside '{forbidden_folder_name}/'"
        )
