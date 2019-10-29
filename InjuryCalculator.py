import numpy as np
import json



    # Parameters
############################################################
############################################################
JSON_FILENAME = "bodyparts.json"

JSON_NAME_COLUMN = "Name"
JSON_LIMB_COLUMN = "Limb"
JSON_ORDER_COLUMN = "Order"
JSON_REM_COLUMN = "Removable"
JSON_PROB_COLUMN = "Probability"


############################################################
############################################################
class Severity:

    def __init__(self, value):
        if value < 0:
            self.severity = "dead"
        elif value >= 0 and value < 3:
            self.severity = "debilitating"
        elif value >= 3 and value < 6:
            self.severity = "major"
        elif value >=6 and value < 11:
            self.severity = "minor"
        else:
            self.severity = "on death's door"


class Injury:

    def __init__(self, level=None, con=None, spill=None):

        self.level = level
        self.con = con
        self.spill = spill

        self.level = int(self.level)
        self.con = int(self.con)
        self.spill = int(self.spill)

        self.d10 = np.random.randint(1, 11)
        self.location = RandomBodyPart()
        self.injury_value = (self.d10 - (lambda x, y: x/y)(int(self.spill), int(self.level)) + int(self.con))
        self.severity = Severity(self.injury_value).severity






class RandomBodyPart:

    def __init__(self):
        with open(JSON_FILENAME) as json_file:
            body_parts = json.load(json_file)
            probabilities = [part['Probability'] for part in body_parts]
            part = np.random.choice(body_parts, replace=True, p=probabilities)

            for field in part.keys():
                setattr(self, field.lower(), part[field])















############################################################
############################################################
