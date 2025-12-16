#!/usr/bin/env python3
"""
Phone Call Script
-----------------
This script facilitates making phone calls using the `termux-telephony-call` command,
which comes with the Termux:API package on Android.

Usage:
    python phone_call.py [phone_number]

Requirements:
    - Android Device
    - Termux App
    - Termux:API App and Package (`pkg install termux-api`)
"""

import os
import sys
import shutil
import argparse
import subprocess

def check_requirements():
    """
    Checks if the necessary tools are installed.
    """
    # Check if termux-telephony-call is available in PATH
    if not shutil.which("termux-telephony-call"):
        print("WARNING: `termux-telephony-call` not found in PATH.")
        print("This script is intended to run on Android within Termux with Termux:API installed.")
        print("If you are running this on Windows/Linux for testing, the actual call will be skipped.")
        return False
    return True

def make_call(phone_number):
    """
    Executes the command to dial the specified phone number.

    Args:
        phone_number (str): The phone number to call.
    """
    print(f"[*] Attempting to call: {phone_number}")

    command = ["termux-telephony-call", phone_number]
    
    try:
        # verify requirements again just in case, though usually checked at start
        if shutil.which("termux-telephony-call"):
            subprocess.run(command, check=True)
            print(f"[+] Call initiated to {phone_number}")
        else:
            print(f"[!] Simulation: `termux-telephony-call {phone_number}` would run here.")
            
    except subprocess.CalledProcessError as e:
        print(f"[-] Error occurred while trying to call: {e}")
    except Exception as e:
        print(f"[-] Unexpected error: {e}")

def main():
    """
    Main entry point of the script.
    """
    # Initialize argument parser
    parser = argparse.ArgumentParser(
        description="Make a phone call using Termux API."
    )
    
    # Add optional argument for phone number
    parser.add_argument(
        "phone_number", 
        nargs="?", 
        help="The phone number to dial."
    )
    
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Force launch the GUI."
    )

    parser.add_argument(
        "--no-gui",
        action="store_true",
        help="Force run in CLI mode (don't launch GUI if no args)."
    )
    
    args = parser.parse_args()
    
    # Check environment
    check_requirements()

    if args.gui or (not args.phone_number and not args.no_gui):
        try:
            launch_gui()
        except ImportError:
            print("[-] tkinter not found. Falling back to CLI.")
            interactive_cli()
        except Exception as e:
             print(f"[-] Failed to launch GUI: {e}")
             interactive_cli()
    elif args.phone_number:
         make_call(args.phone_number)
    else:
        interactive_cli()

def interactive_cli():
    """
    Runs the interactive command line interface.
    """
    print("\n--- Phone Call Script ---")
    try:
        number_to_call = input("Enter the phone number to call: ").strip()
        if number_to_call:
            make_call(number_to_call)
        else:
             print("[-] No phone number provided. Exiting.")
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        sys.exit(0)

def launch_gui():
    """
    Launches a basic tkinter GUI.
    """
    import tkinter as tk
    from tkinter import messagebox

    def on_call():
        phone_number = entry_number.get().strip()
        if not phone_number:
             messagebox.showwarning("Input Error", "Please enter a phone number.")
             return
        
        # logic from make_call but adapted for GUI feedback
        # checks if we are on a supported platform for actual calling
        if shutil.which("termux-telephony-call"):
             try:
                subprocess.run(["termux-telephony-call", phone_number], check=True)
                lbl_status.config(text=f"Calling {phone_number}...", fg="green")
                messagebox.showinfo("Success", f"Call initiated to {phone_number}")
             except Exception as e:
                lbl_status.config(text=f"Error: {e}", fg="red")
                messagebox.showerror("Error", f"Failed to call: {e}")
        else:
             # Simulation mode
             lbl_status.config(text=f"Simulating call to {phone_number}...", fg="blue")
             messagebox.showinfo("Simulation", f"Call command would run for: {phone_number}\n(termux-telephony-call not found)")

    root = tk.Tk()
    root.title("Phone Caller")
    root.geometry("300x200")

    tk.Label(root, text="Enter Phone Number:", font=("Arial", 12)).pack(pady=10)
    
    entry_number = tk.Entry(root, font=("Arial", 14), width=20)
    entry_number.pack(pady=5)
    
    btn_call = tk.Button(root, text="Call", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=on_call)
    btn_call.pack(pady=20)

    lbl_status = tk.Label(root, text="Ready", fg="gray")
    lbl_status.pack(side=tk.BOTTOM, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
