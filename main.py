import os
from pathlib import Path
import sys
import zipfile

from utils.utils_funcs import ensure_dir_exists

# =================================================================================================================
#                                                   CONFIG.                            
# =================================================================================================================
ROOT_DIR = os.getcwd() # root folder
# print("ROOT_DIR:", ROOT_DIR)
BUILD_DIR = os.path.join(ROOT_DIR, 'build') # build folder (/buid)
# print("BUILD_DIR:", BUILD_DIR)

# =================================================================================================================
#                                                   FUNCTIONS                            
# =================================================================================================================
def display_menu():
    print("""
          ==========================================================================
          Available actions: 
          1. Create setup hook build 
          ==========================================================================
          """)
    
    while(1):
        choosen_action = input("Choose action to execute (1 or 2 or ... or 'q' to exit: ")

        if choosen_action == "q":
            print("\nYou choose to exit. Bye, see you!")
            break
        elif choosen_action == "1":
            print("\nYou choose: 1. Create setup hook build")
            create_setup_hook_build()
            break
        else:
            print(f"\nError: choice not valid (or not exists yet): '{choosen_action}'")
         


def create_setup_hook_build():
    """Create setup hook build"""

    output_zip_name = "scripts-dev-env-only.zip"
    output_zip_path = os.path.join(BUILD_DIR, output_zip_name)
    files_to_include = ["requirements.txt", "README.md"]
    folders_to_include = ["src", ]
    exclude_patterns = (
        "__pycache__",
        ".git",
        ".env",
    )

    print("\nCreating setup hook build ...\n")     

    # === Check if build dir exists and create it if not
    ensure_dir_exists(BUILD_DIR)

    # === Define path and build zip name 

    with zipfile.ZipFile(output_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Add individual files
        for file in files_to_include:
            zipf.write(file)

        # Add folders recursively
        for folder in folders_to_include:
            for path in Path(folder).rglob("*"):
                if path.is_file() and not any(x in str(path) for x in exclude_patterns):
                    zipf.write(path)

    print(f"\nCreated build '{output_zip_name}' in build directory '{BUILD_DIR}'")
    


# =================================================================================================================
#                                                   MAIN                            
# =================================================================================================================
def main():
    display_menu()




if __name__ == "__main__":
    main()