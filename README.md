# News Collector

This project get articles from `newsapi` and store the result in a MondoDB collection.

## Prerequisites

- Python 3.x
- MongoDB
- `pip` (Python package installer)

## Setup

### Install Dependencies
1. create a virtual environment and activate it:

```bash
$ python -m venv venv
```

```bash
$ source ./venv/bin/activate
```

2. Install requirements

```bash
$ pip install -r newsrecomendation/Api/requirements.txt 
$ pip install -r newsrecomendation/DataAnalyzer/requirements.txt 
$ pip install -r newsrecomendation/DataCollector/requirements.txt 
$ pip install -r newsrecomendation/DbModel
```
3. Up MongoDB and RabbitMQ

```bash
$ cd infra && docker-compose up
```

4. Run DataAnalyzer

```bash
$ python newsrecomendation/DataAnalyzer/src/analyzer.py
```

5. Run API

```bash
$ python newsrecomendation/Api/src/app.py
```

5. Run DataCollector

```bash
$ python newsrecomendation/DataCollector/src/collector.py
```

6. Run Web Aplication
```bash
$ cd Web
$ pip install
$ ng serve
```