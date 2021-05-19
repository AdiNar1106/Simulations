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

    def simulate(self, runs=10000):
        '''
        Running 10,000 simulations (default) and plotting the resultsOnly highlighting here the parameters not mentioned in the model function

        :param runs: number of times the model will run

        '''

        results = []
        num_simulations = 0

        while num_simulations < runs:
            model = self.insomnia_model(self.WORKING_HOURS, self.COFFEE_THRESHOLD, self.P_COUCH, self.P_PJS, self.P_TIRED)
            results.append(model)
            num_simulations += 1

        results = list(map(lambda x: 'insomnia' if x else 'sleep', results))
        results_df = pd.DataFrame(results)
        results_df.columns = ['type']

        p_insomnia = round(
            (results_df[results_df['type'] == 'insomnia'].count().values[0])/float(runs), 2)
        p_sleep = round(
            (results_df[results_df['type'] == 'sleep'].count().values[0]) / float(runs), 2)
        print('Probability of having insomnia = ' + str(p_insomnia) +
              ' || Probability of a good night\'s sleep = ' + str(p_sleep))
        print(type(results_df['type'][0]))

        # plotting the output of all model runs
        fig, ax = plt.subplots(figsize=(12, 7), constrained_layout=True)
        # removing to and right border
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)  # setting the color palette
        sns.set_palette("Set2")
        results_df['type'].value_counts().plot(kind='bar', color = ['orange', 'blue'])
        ax.xaxis.label.set_visible(False)
        plt.show()

insomnia_sim = Insomnia()
insomnia_sim.simulate()
