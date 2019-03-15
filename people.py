from datetime import datetime

def get_timestamp():
  return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
PEOPLE = {
    "001": {
        "fname": "Anibal",
        "lname": "Chacon",
        "timestamp": get_timestamp()
    },
    "002": {
        "fname": "Jack",
        "lname": "Moreno",
        "timestamp": get_timestamp()
    },
    "003": {
        "fname": "Jeferson",
        "lname": "Cieza",
        "timestamp": get_timestamp()
    }
}

def get_all():
  return [PEOPLE[key] for key in sorted(PEOPLE.keys())]