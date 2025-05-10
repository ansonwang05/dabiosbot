## Getting Started 

Before anything you can create a python virtual environment 

For macOS / Linux[^1]:

```bash
python3 -m venv .venv
```


For Windows[^2]:

```bash
python -m venv .venv
```

Make sure to update .gitignore

```bash
/.venv
/__pycache__
```

Running the program: 

For macOS / Linux: 

```bash
python3 filename.py
```

For Windows: 

```bash
python filename.py
```


[^1]: May need to run 'sudo apt-get install python3-venv' first on Debain-based OSs
[^2]: Can also use 'py -3 -m venv .venv'
