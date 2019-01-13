class Race():
    def __init__(self):
        self.state = ['cool','warm','overheated']
        # initial the three states, cool, warm and overheated.
    def getStates(self):
        
        return self.state
        #return the list in __init__


    def TransitionStates(self, action, state):
        if state =='cool' and action == 'slow':
            return [('cool', 1.0)]
        if state =='cool' and action =='fast':
            return [('cool',0.5),('warm',0.5)]
        if state =='warm' and action =='slow':
            return [('cool',0.5),('warm',0.5)]
        else:
            return [('overheated',1.0)]

    def getPossibleActions(self, state):
        if state == 'cool':
            return ['slow','fast']
        #if cool, the possible action may be slow or fast.
        if state == 'warm':
            return ['slow','fast']
        #if warm, the possible action may be slow or fast.
        if state == 'overheated':
            #if cool, the possible action may only be slow.
            return ['slow']
        
    def Reward(self,state,action,sPrime):
        if state == 'cool' and action == 'slow' and sPrime == 'cool':
            return 1.0
        #get reward 1.0 when change from cool to cool choose action slow.
        if state == 'cool' and action == 'fast' and sPrime == 'cool':
            return 2.0
        #get reward 2.0 when change from cool to cool choose action fast.
        if state == 'cool' and action == 'fast' and sPrime == 'warm':
            return 2.0
        #get reward 2.0 when change from cool to cool choose action fast.
        if state == 'warm' and action == 'slow' and sPrime == 'cool':
            return 1.0
        #get reward 1.0 when change from warm to cool choose action slow.
        if state == 'warm' and action == 'slow' and sPrime == 'warm':
            return 1.0
        #get reward 1.0 when change from warm to warm choose action slow.
        if state == 'warm' and action == 'fast' and sPrime == 'overheated':
            return -10.0
        #get reward -10.0 when change from watn to overheated choose action fast
        else:
            return -10.0
        #go overheated, get reward -10.0

def computeUntilNineteen(state,statePrime):
        racing = Race()
        #call class
        value = 0.0
        #initial reward, change later
        for i in range(0,19):
            reward = []
            statelist = racing.getStates()
            #get the list of states.
            print 'V at ' + str(i) + ' cool '+str(state['cool'])+' warm'+str(state['warm'])
            for current in statelist:
                #Check for each state
                for action in racing.getPossibleActions(current):
                    #Check for each action in the current state
                    for t in racing.TransitionStates(action,current):
                        #Check for each next possible states in current state
                        value = value\
                                +(t[1]*(racing.Reward(current,action,t[0])\
                                             +statePrime[t[0]]))
                        #Apply formular
                    reward.append(value)
                    #add the result to list
                    value = 0.0
                    #initial the value ready for the next loop.
                statePrime = state.copy()
                state[current] = max(reward)
                reward = []
                #clear the list.
def main():
    state = {'cool':0.0,'warm':0.0,'overheated':0.0}
    #initial start state, change later.
    statePrime = {'cool':0.0,'warm':0.0,'overheated':0.0}
    #initial start state, change later.
    computeUntilNineteen(state,statePrime)
        
if __name__ == "__main__":
    main()           
            
