# README

## Running

1. First install requirements: run
      make setup   (or)
      pip install -r requirements

2. Run proj1.py
      make run     (or)
      python -B proj1.py

3. For help on input arguments
      make help    (or)
      python -B proj1.py -h

4. For each task run `make task<task-number>`. For Ex:
      make task1
      make task2
      ...
      make task3



## The folder structure:

Proj1
├── Makefile
├── requirements.txt
├── proj1.py
├── tasks
│   ├── task1.py
│   ├── task2.py
│   ├── task3.py
│   ├── task4.py
│   └── task5.py
├── test_cases.py
└── Utils
    ├── __init__.py
    ├── CalcUtils.py
    ├── MisclUtils.py
    ├── PlotsUtils.py
    ├── RandomUtil.py
    └── ServerUtil.py
