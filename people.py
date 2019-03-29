from datetime import datetime
from flask import make_response, abort


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

def get_by_lname(lname):
  if lname in PEOPLE:
    person = PEOPLE.get("lname")
  else:
    abort(404, "Person  with last name {lname} not found".format(lname=lname))
  return person

def create(person):
  lname = person.get("lname", None)
  fname = person.get("fname", None)

  if lname not in PEOPLE and lname is not None:
    PEOPLE[lname] = {
      "lname": lname,
      "fname": fname,
      "timestamp": get_timestamp(),
    }
    return PEOPLE[lname], 201
  else:
    abort(406, "Person with last name {lname} already exist".format(lname=lname))

def update(lname, person):
  if lname in PEOPLE:
    PEOPLE[lname]["fname"] = person.get("fname")
    PEOPLE[lname]["timestamp"] = get_timestamp()

    return PEOPLE[lname], 200
  else:
    abort(404, "Person  with last name {lname} not found".format(lname=lname))

def delete(lname):
  if lname in PEOPLE:
    del PEOPLE[lname]
    return make_response(
      "{lname} successfully deleted".format(lname=lname), 200
    )
  else:
    abort(404, "Person  with last name {lname} not found".format(lname=lname))
