import yaml
import pprint
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials

with open("config.yml", "r") as yaml_file:
  input_hyper_parameters = yaml.load(yaml_file)

 
print(input_hyper_parameters)

space = {}

def boolify(input_string):
# edited from https://github.com/cgreer/cgAutoCast/blob/master/cgAutoCast.py
  if input_string == 'True' or input_string == 'true':
    return True

  if input_string == 'False' or input_string == 'false':
    return False

  raise ValueError('Not Boolean Value!')

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

    
def variable_esimtator(input_var,hyperparemeters,hyperparameter):

  if type(input_var) == type(hyperparemeters[hyperparameter]):
     hyperparemeters[hyperparameter] = input_var
     return(True)

  else:
     print ('')
     print ('[Error] Input Type not correct: {} expected but {} detected'.format(type(hyperparameter_value),type(input_var)))
     print ('')
     return(False)



def inputedVals(hyper):
    print(' Would you like a random choice')
    print(' Or would you like a uniform choice')
    choice = input(' Enter r or u: ')

    if choice == 'r':
        print(' you picked random')
        print(' Do you want a list ?')
        wants_list = input(' Yes or no ? ')
        vals = []
        if wants_list == 'y':
            num = int(input(' How many items ? '))
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
    if choice == 'u':
        print(' you picked uniform')

#generate empty dict
for hyperparemeters in input_hyper_parameters.items():   
	print(hyperparemeters)
	#assigning instance variables 
	hyperparameter_value = hyperparemeters[0] 
	label = str(hyperparemeters[0])
	Current = str(hyperparemeters[1])

	#creating empty dictionary entry
	space[hyperparemeters[0]]= None
	print (' Current value of - ' + label + ' is : ' + Current)
	print (' Please enter a value for {} and ensure that it is of type {}'.format(label,type(hyperparameter_value)))
	print()
	vals = inputedVals(label)
	print(type(hyperparemeters[0]))
	space[label] = hp.choice(label, vals)

#space['activation'] = hp.choice('activation', ['tanh', 'relu'])
space['dropout'] = hp.uniform('dropout', low=0.001, high=1)


print(space)

