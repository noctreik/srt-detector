#### Requirements
* Python3

### Setup
Activate virtual environment
```
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
```
Install requirements
```
pip install -r requirements.txt
```
### Usage
1. Store `.srt` files in subtitles folder. All files ending with .srt will be searched.
2. Store keywords in `keywords.txt`. Keyword is a single word or multiple words. New keyword is placed in new line.
3. Run the project by executing:
```
python src/main.py
```

Example of keywords.txt:
```
white privilege
goyim
adolt
```

### Test
Ensure you are in virtual environment
```console
source venv/bin/activate
```
Position yourself to the root this project and enter the following command:
```console
pytest test
```
