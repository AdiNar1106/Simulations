import numpy as np
import pandas as pd
import random
import seaborn as sns
import matplotlib.pyplot as plt


class Insomnia:
    WORKING_HOURS = 8
    COFFEE_THRESHOLD = 6
    P_COUCH = 0.7
    P_PJS = 0.35
    P_TIRED = 0.05

    def __init__(self):
        super().__init__()

    def insomnia_model(self, working_hours, coffee_threshold, p_couch, p_pajamas, p_tired):
        '''
        The model, i.e., how the different inputs interact to generate the outputModel constants (not picked at random)
        :param working_hours: number of working hours in a day
        :param coffee_threshold: amount of coffee you need that will for sure result in insomniaModel inputs (picked at random)
        :param p_couch: probability of working from the couch on any given day
        :param p_pajamas: probability of wearing pajama pants on any given day
        :param p_tired: probability of ending the day so tired that you'll fall asleep regardless of how many cups of coffee you have
        :return: The result of the model is either insomnia or sleep.
        '''
        if bool(np.random.binomial(1, p_tired, 1)[0]):
            return False;

        start_day = True
        pjs = bool(np.random.binomial(1, p_pajamas, 1)[0])
        does_couch_work = bool(np.random.binomial(1, p_couch, 1)[0])

        while working_hours > 0 and coffee_threshold > 0:
            if pjs and start_day:
                coffee_threshold -= 2
                start_day = False

            if (does_couch_work) and (working_hours % 2 == 0):
                coffee_threshold -= 1
            working_hours -= 1

        return coffee_threshold == 0
