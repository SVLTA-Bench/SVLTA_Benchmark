import json
import os
import re
import random
import numpy as np
from pymouse import PyMouse

def get_verb_object(action):
    v, object_1, object_2 = " ", " ", " "
    if re.match("open", action) or re.match("close", action) or re.match("sit", action) \
        or re.match("run", action) or re.match("walk", action) or re.match("drink", action) or re.match("grab", action):
        v = action.split(" ")[0]
        object_1 = action.split(" ")[-1]
    elif re.match("stand up", action):
        v = "stand up"
    elif re.match("switch on", action) or re.match("switch off", action):
        v = action.split(" ")[0] + action.split(" ")[1]
        object_1= action.split(" ")[-1]
    elif re.match(r"put(\s*)(.*)in(\s*)(.*)", action) and action != "put fryingpan back":
        v = action.split(" ")[0] + action.split(" ")[2]
        object_1 = action.split(" ")[1]
        object_2 = action.split(" ")[-1]
    elif re.match(r"put(\s*)(.*)back", action):
        v = action.split(" ")[0] + action.split(" ")[2]
        object_1 = action.split(" ")[1]
        object_2 = action.split(" ")[-1]
    
    return v, object_1, object_2


def load_json(file_):
    with open(file_, 'r') as f:
        all_ = json.load(f)
    return all_

def write_json(file_, data):
    if not os.path.exists(file_):
        with open(file_, 'a') as f:
            json.dump(data, f)
    else:
        all_ = load_json(file_)
        all_.extend(data)
        with open(file_, 'w') as f:
            json.dump(all_, f)

def load_txt(file_):
    all_ = []
    for line in open(file_, 'r'):
        v = line.split('\n')[0]
        all_.append(v)
    return all_

def get_actions_list(all_):
    actions = []
    for v, a in all_.items():
        for action in a["actions"]:
            actions.append(action)

    return actions

def softmax(x):

    f_x = np.exp(x) / np.sum(np.exp(x))
    return f_x

def auto_click(x, y):
    mouse = PyMouse()
    mouse.move(x, y)
    mouse.click(x, y)

def random_select(list_, N):
    result = random.sample(list_, N)
    return result