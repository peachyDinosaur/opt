import yaml
import pprint
import sys
import numpy as np
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials

def boolify(input_string):
# edited from https://github.com/cgreer/cgAutoCast/blob/master/cgAutoCast.py
  if input_string == 'True' or input_string == 'true':
    return True

  if input_string == 'False' or input_string == 'false':
    return False

  raise ValueError('Not Boolean Value!')

def yesNo(input_string):
  input_string = input_string.lower()
  if input_string == 'y' or input_string == 'yes':
    return 'yes'

  if input_string == 'n' or input_string == 'no':
    return 'no'

  raise ValueError('Not Yes or no Value!')

def estimateType(input_var):

  # edited from https://github.com/cgreer/cgAutoCast/blob/master/cgAutoCast.py

  # we wanna try to guess (estimate) the variable type from the input string
  input_var = str(input_var) #important if the parameters aren't strings...

  for posible_input_types in (boolify, int, float, str ):
     try:
        return posible_input_types(input_var)
     except ValueError:
        pass
  return input_var

def validInput(input_string, inputType):
    while True:
        try:
            inp = input(input_string)
            if inp == 'exit':
                sys.exit(0)
            #maybe add default value
            vals = inputType(inp)
            print (vals)
            print(type(vals))
            return vals
        except ValueError:
            print(' Not correct type')

def frange(x, y, jump):
  while x < y:
    yield x
    x += float(decimal.Decimal(jump))

    
def variable_esimtator(input_var,hyperparemeters,hyperparameter):

  if type(input_var) == type(hyperparemeters[hyperparameter]):
     hyperparemeters[hyperparameter] = input_var
     return(True)

  else:
     print ('')
     print ('[Error] Input Type not correct: {} expected but {} detected'.format(type(hyperparameter_value),type(input_var)))
     print ('')
     return(False)

def stringInput(hyper):
    print(' Do you want a list ?')
    wants_list = validInput(' Yes or no ? ', yesNo)
    vals = []
    if wants_list == 'y':
        num = validInput(' How many items ? ', int)
        for i in range(num):
            item = input(' What are the {} functions you want to add '.format(hyper))
            vals.append(item)
        print(vals)
        return vals

    else:
        item = input(' What {} function do you want to add '.format(hyper))
        vals.append(item)
        print(vals)
        return vals


def intVal(hyperparameter):
    print(' Do you want a list ?')
    wants_list = validInput(' Yes or no ? ', yesNo)
    vals = []
    if wants_list == 'y' or wants_list == 'yes':
        minVal = validInput(" {}  -- Minimum Value : ".format(hyperparameter), int)
        print()
        maxVal = validInput(" {}  -- Maximum Value : ".format(hyperparameter), int)
        print()
        stepSize = validInput(" {}  --  Step Size : ".format(hyperparameter), int)
        print()
        vals = list(range(minVal, (maxVal), stepSize))
        print(vals)
        return vals

    elif wants_list == 'n' or wants_list == 'no':
        item = validInput(' What is the {} value you want to add '.format(hyperparameter), int)
        vals.append(item)
        print(vals)
        return vals

def ranValue(hyperparameter):
    minVal = validInput(" {}  -- Minimum Value : ".format(hyperparameter), float)
    print()
    maxVal = validInput(" {}  -- Maximum Value : ".format(hyperparameter), float)
    print()
    stepSize = validInput(" {}  --  How many distributed values : ".format(hyperparameter), int)
    print()

    #trying to define floating step size list
    vals = np.linspace(minVal, maxVal, num=(stepSize+1)).tolist()
    #vals = [maxVal, minVal]
    print(vals)
    return vals

def uniValue(hyperparameter):
    minVal = validInput(" {}  -- Minimum Value : ".format(hyperparameter), float)
    print()
    maxVal = validInput(" {}  -- Maximum Value : ".format(hyperparameter), float)
    print()
    vals = [minVal, maxVal]
    print(vals)
    return vals

def boolValue(hyperparameter):
    correctInput = True
    print(' Do you want to use True and False randomly for {}'.format(hyperparameter))
    res = validInput(' Yes or no ? ', yesNo)
    if res == 'y' or res == 'yes':
        vals = [True, False]
        print(vals)
        return vals

    # elif res == 'n' or res == 'no':
    #     while correctInput:
    #         correctInput = False
    #         try:
    #             print(' Enter which option you want to use')
    #             boolInput = input(' Enter True or False ')
    #             vals = [boolify(boolInput)]
    #         except ValueError:
    #             print(' NOT RIGHT INPUT TRY AGAIN')
    #             correctInput= True
    #     print(vals)
    #     return vals


    elif res == 'n' or res == 'no':
        print(' Enter which option you want to use')
        inp = ' Enter True or False '
        return [validInput(inp, boolify)]



#loading YAML file
#with open("training.yml", "r") as yaml_file:
with open("config2.yml", "r") as yaml_file:
  input_hyper_parameters = yaml.load(yaml_file)

#Print hyperparms
print(input_hyper_parameters)

#init empty space
space = {}


#Looping through items in YAML file
for hyperparemeters in input_hyper_parameters.items():
    #current hyper
    print(hyperparemeters)


    #assigning instance variables 
    hyperparameter_value = hyperparemeters[1] 
    label = str(hyperparemeters[0])
    Current = str(hyperparemeters[1])

    #creating empty dictionary entry
    space[hyperparemeters[0]]= None
    print()
    print (' Current value of - ' + label + ' is : ' + Current)
    print (' Please enter a value for {} and ensure that it is of type {}'.format(label,type(hyperparameter_value)))
    print()

    #Checking type of hyper
    if type(hyperparameter_value) == type(int()):
        print()
        vals = intVal(label)
        space[label] = hp.choice(label, vals)
        print()

    if type(hyperparameter_value) == type(float()):
        print()
        print(' Would you like a random choice')
        print(' Or would you like a uniform choice')
        #TODO type checking or restructure
        choice = input(' Enter r or u: ')

        if choice == 'r':
            print(' you picked random')
            print()
            vals = ranValue(label)
            space[label] = hp.choice(label, vals)
            print()

        elif choice == 'u':
            print(' you picked uniform')
            print()
            vals = uniValue(label)
            space[label] = hp.uniform(label, low=vals[0], high=vals[1])
            print()

    if type(hyperparameter_value) == type(bool()):
        print()
        vals = boolValue(label)
        space[label] = hp.choice(label, vals)
        print()


    if type(hyperparameter_value) == type(str()):
        print()
        print(' im an string')
        vals = stringInput(label)
        space[label] = hp.choice(label, vals)
        print()
    
    print(space)
    #space[label] = hp.choice(label, vals)

#space['activation'] = hp.choice('activation', ['tanh', 'relu'])
#space['dropout'] = hp.uniform('dropout', low=0.001, high=1)


print(space)

