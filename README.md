# News Collector

This project get articles from `newsapi` and store the result in a MondoDB collection.

## Prerequisites

- Python 3.x
- MongoDB
- `pip` (Python package installer)

## Setup

### Install Dependencies
1. Navigate to application folder
```bash
$ cd data_collector_app
```

2. create a virtual environment and activate it:

```bash
$ python -m venv venv
```

```bash
$ source ./venv/bin/activate
```

3. Install requirements

```bash
$ pip install -r requirements.txt
```
4. Up MongoDB

```bash
$ cd infra && docker-compose up
```

5. Run main

```bash
$ python src/collector.py
```

```bash
$ pip install ../DbModel
```
