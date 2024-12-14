# darwinprint
3d rendering project with AMS regarding evolution with Rhino3d and Grasshopper


# How to Use

In the src/interface folder, there is a flask python program that can be launched in two different ways.


## Windows

### First time setup
Start Windows PowerShell with the "Run as Administrator" option. Only members of the Administrators group on the computer can change the execution policy.

Enable running unsigned scripts by entering:

```powershell
set-executionpolicy remotesigned
```
This will allow running unsigned scripts that you write on your local computer and signed scripts from Internet.
This is needed to run the venv activate script.

### Launching the app

1. create venv and launch app manually.

```powershell
cd src\interface
python -m venv venv ; .\venv\Scripts\activate ; pip install -r requirements.txt
.\app.py
```

2. launch start_app.ps1

```powershell
.\start_app.ps1
```
