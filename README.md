# scripts-dev-env-only
Useful scripts to be used only by developers in their development environment.

## Current scripts
### Python
#### 1 - git_setup_hook.py
```
Description:
This script automatically sets up a Git hook in the current repository when executed.

Usage:
    python git_setup_hook.py

Requierements:
    The structure of the project and it folder names must be:

    <Root project folder>
    |
    |    
    +---SCRIPTS-DEV-ENV-ONLY
        |
        |   
        +---python
            +---git
                |   git_setup_hook.py
                |   
                +---my_hooks
                   +---commit-msg
                   |       my_commit_msg_v1
                   |       my_commit_msg_v1_description
                   |       ...
                   |       
                   +---pre-commit
                   |       my_pre_commit_v1
                   |       my_pre_commit_v1_description
                   |       ...
                   |
                   +--- ...
    

Environments:
    - os: windows 11
    - python version: 3.14.0
    - git version: 2.51.1.windows.1
Warning: It will probably need to be adapted if the environment changes.

Note:
This script needs to be run only once per repository.
The hook will then be triggered automatically on every git command which trigger it (e.g. `git commit` command to 
trigger 'commit-msg' hook).
```

##### *1.1 - my_commit_msg_\<version number>*
This script is used to create **commit-msg** hook in the default .git/hooks filder.

###### Current versions:
*my_commit_msg_v1:*

- Description in ./python/git/my_hooks/commit-msg/my_commit_msg_v1_description


##### *1.2 - my_pre-commit_v1*
This script is used to create **commit-msg** hook in the default .git/hooks folder.

###### Current versions:
*my_pre-commit_v1:*

- Description in ./python/git/my_hooks/pre-commit/my_pre_commit_v1_description




