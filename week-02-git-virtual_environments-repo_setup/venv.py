#Week 2 - Day 1: Virtual Environments and Packages
""""create a virtual environment and installed packages followed by the requirements.txt file"""

print("Creating a virtual environment...")

#to create a virtual environment, run the following command in your terminal:
command = "python -m venv venv"

#to activate the virtual environment, run the following command in your terminal:
to_activate = "venv\\Scripts\\activate"  # For Windows
to_activate_in_gitbash = "source venv/Scripts/activate"  #for Git Bash on Windows
to_activate_mac_linux = "source venv/bin/activate"  # For macOS/Linux

#to deactivate the virtual environment, run the following command in your terminal:
to_deactivate = "deactivate"