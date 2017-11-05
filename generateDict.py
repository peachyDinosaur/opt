import yaml


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

 

def is_empty(input):
    if input == "":
        print(' you entered nothing')
        min_input_var = hyperparemeters[hyperparameter]
        print('', min_input_var)
        valueNotChecked= False   

def variable_esimtator(input_var,hyperparemeters,hyperparameter):

  if type(input_var) == type(hyperparemeters[hyperparameter]):
     hyperparemeters[hyperparameter] = input_var
     return(True)

  else:
     print ('')
     print ('[Error] Input Type not correct: {} expected but {} detected'.format(type(hyperparameter_value),type(input_var)))
     print ('')
     return(False)


with open("config.yml", "r") as yaml_file:
  input_hyper_parameters = yaml.load(yaml_file)

 
print(yaml_file)
 

print ('')
print ('')
print ('----------------------------------------------------------------------------------')

print ('            please specify the ranges for the hyper parameters ')

print ('----------------------------------------------------------------------------------')
print ('')
print ('')

 

for paramter_group, hyperparemeters in input_hyper_parameters.items():    
  print ('')
  print (' For the Hyperparameter group : {}'.format(paramter_group))

  for hyperparameter in hyperparemeters:

    hyperparameter_value = hyperparemeters[hyperparameter]
    print (type(hyperparameter_value))

    print ('')
    print ('')

    print (' Current value of - ' + hyperparameter + ' is : ' + str( hyperparemeters[hyperparameter]))

    print (' Please enter a value for {} and ensure that it is of type {}'.format(hyperparameter,type(hyperparameter_value)))
    valueNotChecked = True

    if type(hyperparameter_value) == type(int()): 
      while valueNotChecked:

        string_input_var = input(" {}  -- Minimum Value : ".format(hyperparameter))
        if string_input_var == "":
          print(' you entered nothing')
          min_input_var = hyperparemeters[hyperparameter]
          print('', min_input_var)
          valueNotChecked= False
        else:
          min_input_var = estimateType(string_input_var)

        if variable_esimtator(min_input_var,hyperparemeters,hyperparameter):
           break




      while valueNotChecked:

        string_input_var = input(" {}  -- Maximum Value : ".format(hyperparameter))
        max_input_var = estimateType(string_input_var)

        if variable_esimtator(max_input_var,hyperparemeters,hyperparameter):

          if max_input_var < min_input_var:
             print ('[Error] Maximum Value ({}) cannot be smaller than Minimum Value ({}) '.format(max_input_var,min_input_var))

          else:
             break



      while valueNotChecked:

        string_input_var = input(" {}  -- Step size : ".format(hyperparameter))
        step_size_input_var = estimateType(string_input_var)

        if variable_esimtator(step_size_input_var,hyperparemeters,hyperparameter):

          if((max_input_var - min_input_var) == 0):
            step_size_input_var = 1
            break

          elif step_size_input_var > (max_input_var - min_input_var):

            print ('[Error] Step size ({}) cannot be larger than range of Minimum Value to Maximum Value ({}) '.format(step_size_input_var,(max_input_var - min_input_var)))

          else:
            break


      if valueNotChecked ==False:
        print("using default value")
      else:
        hyperparemeters[hyperparameter] = list(range(min_input_var, (max_input_var + 1), step_size_input_var))



    else:
      emptyString = True

      while emptyString:
        string_input_var = input(" {} : ".format(hyperparameter))
        if string_input_var == "":
          print(' you entered nothing')
          input_var = hyperparemeters[hyperparameter]
          print('', input_var)
          emptyString= False
        else:
          input_var = estimateType(string_input_var)

        if variable_esimtator(input_var,hyperparemeters,hyperparameter):
          break

      hyperparemeters[hyperparameter] = input_var