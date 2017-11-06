import yaml
import pprint
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials

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

def stringInput(hyper):
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

def decimaValue():
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


def intVal(hyper):
    print(' Do you want a list ?')
    wants_list = input(' Yes or no ? ')
    vals = []
    if wants_list == 'y':
        num = int(input(' How many items ? '))
        for i in range(num):
            item = int(input(' What are the {} values you want to add '.format(hyper)))
            vals.append(item)
        print(vals)
        return vals

    else:
        item = int(input(' What is the {} value you want to add '.format(hyper)))
        vals.append(item)
        print(vals)
        return vals

def ranValue(hyperparameter):
	minVal = int(input(" {}  -- Minimum Value : ".format(hyperparameter)))
	print()
	maxVal = int(input(" {}  -- Maximum Value : ".format(hyperparameter)))
	print()
	stepSize = int(input(" {}  --  Step Size : ".format(hyperparameter)))
	print()
	vals = list(range(minVal, (maxVal + 1), stepSize))
	return vals

def uniValue(hyperparameter):
	minVal = int(input(" {}  -- Minimum Value : ".format(hyperparameter)))
	print()
	maxVal = int(input(" {}  -- Maximum Value : ".format(hyperparameter)))
	print()
	vals = [minVal, maxVal]
	return vals

def boolValue(hyperparameter):
    print(' Do you want to use True and False randomly for {}'.format(hyperparameter))
    res = input(' Yes or no ? ')
    if res == 'y':
        vals = [True, False]
        return vals

    elif res == 'n':
        print(' Enter which option you want to use')
        boolInput = input(' Enter True or False ')
        vals = boolify(boolInput)
        return vals

#loading YAML file
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
		space[label] = (label, vals)
		print()

	if type(hyperparameter_value) == type(float()):
		print()
		print(' Would you like a random choice')
		print(' Or would you like a uniform choice')
		choice = input(' Enter r or u: ')

		if choice == 'r':
			print(' you picked random')
			print()
			vals = ranValue(label)
			space[label] = (label, vals)
			print()

		if choice == 'u':
			print(' you picked uniform')
			print()
			vals = uniValue(label)
			space[label] = (label, vals)
			print()

	if type(hyperparameter_value) == type(bool()):
		print()
		vals = boolValue(label)
		space[label] = (label, vals)
		print()


	if type(hyperparameter_value) == type(str()):
		print()
		print(' im an string')
		vals = stringInput(label)
		space[label] = (label, vals)
		print()
	
	print(space)
	#space[label] = hp.choice(label, vals)

#space['activation'] = hp.choice('activation', ['tanh', 'relu'])
#space['dropout'] = hp.uniform('dropout', low=0.001, high=1)


print(space)

