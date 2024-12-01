import os
import subprocess
import platform
import tkinter as tk
from tkinter import messagebox

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
            messagebox.showinfo("Installation", f"{tool_name} is already installed.")
            return

        if self.os_type not in commands:
            messagebox.showerror("Error", f"No installation commands for {tool_name} on {self.os_type}.")
            return

        command = commands[self.os_type]
        try:
            result = subprocess.run(command, shell=True)
            if result.returncode == 0:
                messagebox.showinfo("Installation", f"{tool_name} installed successfully.")
            else:
                messagebox.showerror("Error", f"Failed to install {tool_name}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while installing {tool_name}: {e}")

    def uninstall_tool(self, tool_name, uninstall_commands):
        """Uninstall a tool using the given commands."""
        if self.os_type not in uninstall_commands:
            messagebox.showerror("Error", f"No uninstallation commands for {tool_name} on {self.os_type}.")
            return

        command = uninstall_commands[self.os_type]
        try:
            result = subprocess.run(command, shell=True)
            if result.returncode == 0:
                messagebox.showinfo("Uninstallation", f"{tool_name} uninstalled successfully.")
            else:
                messagebox.showerror("Error", f"Failed to uninstall {tool_name}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while uninstalling {tool_name}: {e}")

    def check_for_updates(self, tool_name, update_command):
        """Check if updates are available for a tool."""
        if self.os_type not in update_command:
            messagebox.showerror("Error", f"No update check command for {tool_name} on {self.os_type}.")
            return

        command = update_command[self.os_type]
        try:
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode().strip()
            if result.returncode == 0 and tool_name.lower() in output.lower():
                messagebox.showinfo("Update Check", f"Update available for {tool_name}: {output}")
            elif result.returncode == 0:
                messagebox.showinfo("Update Check", f"No updates available for {tool_name}.")
            else:
                messagebox.showerror("Error", f"Failed to check updates for {tool_name}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while checking updates for {tool_name}: {e}")

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

    def install():
        manager.install_tool(tool, tool_commands[tool], check_commands[tool][manager.os_type])

    def uninstall():
        manager.uninstall_tool(tool, uninstall_commands[tool])

    def check_updates():
        manager.check_for_updates(tool, update_commands[tool])

    # Create GUI
    root = tk.Tk()
    root.title("Simple Tool Manager")

    install_button = tk.Button(root, text="Install ngspice", command=install)
    install_button.pack(pady=10)

    uninstall_button = tk.Button(root, text="Uninstall ngspice", command=uninstall)
    uninstall_button.pack(pady=10)

    update_button = tk.Button(root, text="Check for Updates", command=check_updates)
    update_button.pack(pady=10)

    root.mainloop()
