# import os
# import sys

# print(f"**File**: {__file__}")
# print()
# # print(f"**File**: {os.path.dirname(__file__)}")
# project_root = os.path.join(os.path.dirname(__file__), '..')
# sys.path.insert(0, project_root)
# print(sys.path)
# # print(f"Project Root: {project_root} ")

import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print("Project root:", project_root)  # Print current working directory
sys.path.insert(0, project_root)
print("Sys path:", sys.path)        # Print Python's module search paths



