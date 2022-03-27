class JsonOutput:
     def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[key] = value

     def __repr__(self, reccursion_number=0):
         output = ""
         for key, value in self.__dict__.items():
             if type(value) == dict:
                output += key + " :\n" + JsonOutput(**value).__repr__(reccursion_number + 1)
             elif type(value) == list:
                for x in value:
                    output += key + ' :\n' + JsonOutput(**x).__repr__(reccursion_number + 1)
             else:
                output += '\t' * reccursion_number + key + " : " + str(value) + '\n'
         return output
