Simple Tool Manager

This Python project provides a graphical interface for managing tools such as ngspice. The application allows users to install, uninstall, and check for updates for tools based on the operating system. The implementation includes support for Linux and Windows.

Features

Install tools (e.g., ngspice)

Uninstall tools

Check for tool updates

Platform-specific command support

Easy-to-use GUI built with Tkinter

Prerequisites

Before running the project, ensure you have the following installed on your system:

General Requirements

Python 3.6 or higher

Download and install Python from python.org.

pip (Python package manager)

Comes pre-installed with Python. If not, install it using:

python -m ensurepip --upgrade

Platform-Specific Tools

For Linux

Ensure sudo is available for package management.

ngspice installation requires apt package manager.

For Windows

Install Chocolatey for package management. Refer to the official Chocolatey installation guide.

Required Python Libraries

This project uses the following Python libraries:

tkinter (Built-in with Python)

subprocess

platform

os

Installation

Follow the steps below to set up and run the project:

1. Clone the Repository

Clone this repository to your local machine using:

git clone <repository_url>

Navigate to the project directory:

cd <project_directory>

2. Install Required Python Packages

Install the required Python libraries:

pip install tk

(Note: tkinter is built-in for most Python installations.)

3. Run the Application

Execute the script using:

python simple_tool_manager.py

4. Use the Application

Launch the GUI.

Click the buttons to install, uninstall, or check for updates for ngspice.

How It Works

Installation:

Uses platform-specific commands to install the selected tool.

Checks if the tool is already installed before proceeding.

Uninstallation:

Uses platform-specific commands to uninstall the selected tool.

Update Check:

Checks for updates using platform-specific commands and displays the result.

Supported Commands

Installation Commands

OS

Command

Linux

sudo apt update && sudo apt install -y ngspice

Windows

choco install -y ngspice

Uninstallation Commands

OS

Command

Linux

sudo apt remove -y ngspice

Windows

choco uninstall -y ngspice

Update Commands

OS

Command

Linux

`sudo apt update && apt list --upgradable

grep ngspice`

Windows

choco outdated

Note

The GUI may require elevated privileges (administrator or root access) for installing or uninstalling tools.

Ensure network connectivity for installation and update checks.

Troubleshooting

If the tool fails to install or uninstall, check the logs printed to the terminal for detailed error messages.

For ngspice commands to work on Windows, ensure Chocolatey is properly installed and configured.

If tkinter is missing, install it via your system’s package manager (e.g., sudo apt install python3-tk on Linux).

License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

Acknowledgments

Special thanks to the open-source community for providing the tools and resources used in this project.
