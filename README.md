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

## Before Running

Make sure you activate the python virtual environment
and confirm that it is activated

For macOS / Linux: 

```bash
source .venv/bin/activate
which python
```

For Windows:

```bash
.venv/Scripts/activate
where python
```

When you want to switch projects or leave: 

```bash
deactivate
```

## Running Files

For macOS / Linux: 

```bash
python3 main.py
```

For Windows: 

```bash
python main.py
```

[^1]: May need to run 'sudo apt-get install python3-venv' first on Debain-based OSs
[^2]: Can also use 'py -3 -m venv .venv'
