#run as ./start_app.ps1

rm -r output
mkdir output
./venv/Scripts/activate.ps1 ; pip install -r requirements.txt ; python .\app.py