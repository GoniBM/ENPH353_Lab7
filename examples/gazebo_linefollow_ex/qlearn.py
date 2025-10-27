import random
import pickle
import csv



class QLearn:
    def __init__(self, actions, epsilon, alpha, gamma):
        self.q = {}
        self.epsilon = epsilon  # exploration constant
        self.alpha = alpha      # discount constant
        self.gamma = gamma      # discount factor
        self.actions = actions

    def loadQ(self, filename):
        '''
        Load the Q state-action values from a pickle file.
        '''
        
        # TODO: Implement loading Q values from pickle file.
        
#to load a pickle file we open it in read binary mode and use pickle.load
#it needs to be binary mode because pickle files are binary files
        with open(filename + ".pickle", "rb") as f: 
            self.q = pickle.load(f)
            print("Locked and Loaded file")



        print("Loaded file: {}".format(filename+".pickle"))

    def saveQ(self, filename):
        '''
        Save the Q state-action values in a pickle file.
        '''
        # TODO: Implement saving Q values to pickle and CSV files.

        with open(filename + ".pickle", "wb") as f: 
            pickle.dump(self.q,f)

# to save a csv file we open it in write mode and use csv.writer
#we oyt each key value pair in q a dictionary as a row in the csv file
# each key is a tuple (state, action) so we unpack it into state and action
# the value is the Q value
# we write this to the csv file because its eaiser to read and analyze then a pickle file I think
        with open(filename + ".csv", "w", newline = "") as f: 
            writer = csv.writer(f)
            for key, value in self.q.items():
                state, action = key 
                writer.writerow([state, action,value])
            print("File is written {}".format(filename + ".pickle"))



        print("Wrote to file: {}".format(filename+".pickle"))

    def getQ(self, state, action):
        '''
        @brief returns the state, action Q value or 0.0 if the value is 
            missing
        '''
        return self.q.get((state, action), 0.0)

    def chooseAction(self, state, return_q=False):
        '''
        @brief returns a random action epsilon % of the time or the action 
            associated with the largest Q value in (1-epsilon)% of the time
        '''
        # TODO: Implement exploration vs exploitation
        #    if we need to take a random action:
        #       * return a random action
        #    else:
        #       * determine which action has the highest Q value for the state 
        #          we are in.
        #       * address edge cases - what if 2 actions have the same max Q 
        #          value?
        #       * return the action with highest Q value
        #
        # NOTE: if return_q is set to True return (action, q) instead of
        #       just action

        # THE NEXT LINES NEED TO BE MODIFIED TO MATCH THE REQUIREMENTS ABOVE 

        # We randomly pick a number if its less then epsilon we explore
        if(random.random() < self.epsilon): 
            #This is exploration, basically we pick a random action
            action = random.choice(self.actions)
            
        #This is exploitation we pick the action with the highest Q value which means
        # we think it will lead to the best reward, based on prior learning
        else: 
            # gets all q values for all actions in current state
            q_vals = [self.getQ(state, a) for a in self.actions]
            # find the max Q value
            max_q = max(q_vals)
            # find all actions that have the max Q value
            candidates = [a for a, q in zip(self.actions, q_vals) if q == max_q ]
            #randomly pick one of the candidates if there is more than one
            action =random.choice(candidates)

        # if return_q is true we return both the action and the Q value
        if(return_q): 
            return action, self.getQ(state, action)
        return action


    def learn(self, state1, action1, reward, state2):
        '''
        @brief updates the Q(state,value) dictionary using the bellman update
            equation
        '''
        # TODO: Implement the Bellman update function:
        #     Q(s1, a1) += alpha * [reward(s1,a1) + gamma* max(Q(s2)) - Q(s1,a1)]
        # 
        # NOTE: address edge cases: i.e. 
        # 
        # Find Q for current (state1, action1)
        # Address edge cases what do we want to do if the [state, action]
        #       is not in our dictionary?
        # Find max(Q) for state2
        # Update Q for (state1, action1) (use discount factor gamma for future 
        #   rewards)

        # THE NEXT LINES NEED TO BE MODIFIED TO MATCH THE REQUIREMENTS ABOVE
        
# Get old Q value for (state1, action1)
        old_q = self.getQ(state1,action1)
        # Get max Q value for state2 by checking all possible actions
        future_q = max([self.getQ(state2, a) for a in self.actions])
        # Bellman update which is a way to update Q values based on learning rate alpha
        self.q[(state1, action1)] = old_q + self.alpha * (reward + self.gamma * future_q - old_q)

       