import os
import subprocess

# Activate the virtual environment
activate_env = ".venv/bin/activate"  # or .venv\Scripts\activate.bat on Windows

# Update requirements.txt
subprocess.run(f"pip freeze > requirements.txt", shell=True)

print("requirements.txt has been updated.")