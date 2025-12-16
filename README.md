# 📞 Phone-Call

A robust Python script to make phone calls using **Termux:API** on Android.
Includes a **GUI** for Windows (simulation) and interactive CLI for Android.

---

## 📱 Requirements

- **Android Device**
- **[Termux](https://f-droid.org/en/packages/com.termux/)** App
- **[Termux:API](https://f-droid.org/en/packages/com.termux.api/)** App & Package
- **Python 3.x**

---

## ⚙️ Setup for Android

1. **Install Apps**: Download Termux and Termux:API from F-Droid (recommended) or Play Store.
2. **Grant Permissions**: Open Termux:API app once. in Android Settings, ensure Termux has "Phone" or "Call" permissions.
3. **Install Packages**: Open Termux and run:
   ```bash
   pkg update
   pkg install python termux-api
   ```
4. **Download Script**: Move `phone_call.py` to your Termux storage.

---

## 🚀 Usage

### Option 1: Interactive (Easiest)
Simply run the script. It will ask for the number.
```bash
python phone_call.py
```
*Note: If graphical interface (GUI) is not available, it automatically falls back to text mode.*

### Option 2: Command Line
Pass the number directly.
```bash
python phone_call.py +1234567890
```

### Option 3: Windows (Simulation)
- Double-click `run.bat` to launch the GUI.
- It will simulate the call (print the command) since Windows cannot make cellular calls directly.

---

## 🛠 Features
- **Smart Fallback**: Tries to launch a GUI; if it fails (common on pure Termux), it switches to CLI.
- **Safety**: Uses standard `subprocess` calls.
- **Cross-Platform**: Works on Android (Real Calls) and Windows (Simulation).
