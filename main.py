from enum import Enum

import numpy as np
import pandas as pd
from fastapi import FastAPI
from tensorflow import keras


def rule(player, ia):
    if player == ia:  # 'Tie'
        return 'Tie'

    elif player == 0 and ia == 1:  # "IA Won"
        return "IA Won"

    elif player == 1 and ia == 2:  # "IA Won"
        return "IA Won"

    elif player == 2 and ia == 0:  # "IA Won"
        return "IA Won"

    else:  # "Player Won"
        return "Player Won"


def int_to_str(choice):
    if choice == 0:
        return 'Rock'
    elif choice == 1:
        return 'Paper'
    else:
        return 'Scissor'


def str_to_int(choice):
    if choice is Decision.rock:
        return 0
    elif choice is Decision.paper:
        return 1
    else:
        return 2


class Decision(str, Enum):
    rock = "Rock"
    paper = "Paper"
    scissor = "Scissor"


app = FastAPI()


@app.post("/predict")
async def predict_game(decision: Decision):
    player_choice = str_to_int(decision)
    saved_model = keras.models.load_model('model/model2.h5')
    df_save = pd.read_csv('model/df_save.csv')

    mean_x = np.array([df_save['mean_x0'][0], df_save['mean_x1'][0]])
    std_x = np.array([df_save['std_x0'][0], df_save['std_x1'][0]])

    my_data = ([player_choice, 1] - mean_x) / std_x

    my_data = np.array(my_data).reshape(1, 2)

    predictions = saved_model(my_data)

    if predictions <= 0.66666666:
        choixIA = 0
    elif (predictions > 0.66666666) and (predictions <= 1.33333332):
        choixIA = 1
    else:
        choixIA = 2

    output = rule(player_choice, choixIA)

    return {"Prediction : ", int_to_str(choixIA), "Result : ", output}
