import os
import subprocess
import platform

class SimpleToolManager:
    def __init__(self, install_dir="tools"):
        self.os_type = platform.system().lower()
        self.install_dir = os.path.abspath(install_dir)
        os.makedirs(self.install_dir, exist_ok=True)

    def is_tool_installed(self, tool_name, check_command):
        """Check if a tool is already installed."""
        try:
            result = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.returncode == 0
        except Exception as e:
            print(f"Error while checking installation for {tool_name}: {e}")
            return False

    def install_tool(self, tool_name, commands, check_command):
        """Install a tool using the given commands."""
        if self.is_tool_installed(tool_name, check_command):
            print(f"{tool_name} is already installed.")
            return

        if self.os_type not in commands:
            print(f"No installation commands for {tool_name} on {self.os_type}.")
            return

        command = commands[self.os_type]
        print(f"Installing {tool_name}...")
        try:
            result = subprocess.run(command, shell=True)
            if result.returncode == 0:
                print(f"{tool_name} installed successfully.")
            else:
                print(f"Failed to install {tool_name}. Command: {command}")
        except Exception as e:
            print(f"An error occurred while installing {tool_name}: {e}")

    def uninstall_tool(self, tool_name, uninstall_commands):
        """Uninstall a tool using the given commands."""
        if self.os_type not in uninstall_commands:
            print(f"No uninstallation commands for {tool_name} on {self.os_type}.")
            return

        command = uninstall_commands[self.os_type]
        print(f"Uninstalling {tool_name}...")
        try:
            result = subprocess.run(command, shell=True)
            if result.returncode == 0:
                print(f"{tool_name} uninstalled successfully.")
            else:
                print(f"Failed to uninstall {tool_name}. Command: {command}")
        except Exception as e:
            print(f"An error occurred while uninstalling {tool_name}: {e}")

    def check_for_updates(self, tool_name, update_command):
        """Check if updates are available for a tool."""
        if self.os_type not in update_command:
            print(f"No update check command for {tool_name} on {self.os_type}.")
            return

        command = update_command[self.os_type]
        print(f"Checking for updates for {tool_name}...")
        try:
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode().strip()
            if result.returncode == 0:
                if tool_name.lower() in output.lower():
                    print(f"Update available for {tool_name}: {output}")
                else:
                    print(f"No updates available for {tool_name}.")
            else:
                print(f"Failed to check updates for {tool_name}. Command: {command}")
        except Exception as e:
            print(f"An error occurred while checking updates for {tool_name}: {e}")

if __name__ == "__main__":
    tool_commands = {
        "ngspice": {
            "linux": "sudo apt update && sudo apt install -y ngspice",
            "windows": "choco install -y ngspice"
        }
    }

    check_commands = {
        "ngspice": {
            "linux": "ngspice --version",
            "windows": "ngspice --version > nul 2>&1"
        }
    }

    uninstall_commands = {
        "ngspice": {
            "linux": "sudo apt remove -y ngspice",
            "windows": "choco uninstall -y ngspice"
        }
    }

    update_commands = {
        "ngspice": {
            "linux": "sudo apt update && apt list --upgradable | grep ngspice",
            "windows": "choco outdated"
        }
    }

    manager = SimpleToolManager()

    tool = "ngspice"

    # Install ngspice
    manager.install_tool(tool, tool_commands[tool], check_commands[tool][manager.os_type])

    # Check for updates
    manager.check_for_updates(tool, update_commands[tool])

    # Uncomment to uninstall ngspice
    # manager.uninstall_tool(tool, uninstall_commands[tool])
