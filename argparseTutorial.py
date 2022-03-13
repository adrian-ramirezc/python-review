import math
import argparse

# Instance the Argument Parser with a brief description
parser = argparse.ArgumentParser(description = 'Calculate volume of a Cylinder')

# Adding arguments to the Argument Parser
## positional arguments are required by default / the order is important
parser.add_argument('posArg', help = 'This is a positional argument') # positional arguments are required / the order is important
## optional arguments are NOT required by default / the order is not important
parser.add_argument('-r','--radius', type = int, metavar = '', default = 5, help = 'Radius of Cylinder')
parser.add_argument('-H','--height', type = int, metavar = '', required = True, help = 'Height of a Cylinder')
parser.add_argument('-u', '--unit', type = str, metavar = '', default = 'm3', help = 'Show volume in m3 or cm3', choices=["m3","cm3"])

# Creating a second Argument Parser
parser2 = argparse.ArgumentParser(description = 'This is a second Argument Parser')
parser2.add_argument('argumentX', help = 'This is the argumentX')
parser2.add_argument('-a1', '--arg1', type = float, help = 'This is the argument1')
parser2.add_argument('-a2', '--arg2', type = float, default = 4.12345, help = 'This is the argument2')


def cylinder_volume(radius, height):
        
        vol = (math.pi) * (radius ** 2) * height
        if args.unit == 'm3':
                return vol 
        elif args.unit == 'cm3':
                return vol*10e6 

if __name__ == '__main__':
        parser.set_defaults(radius = 1) # Set default (or overwrites) the default value of '-r' in parser 

        # What to do if you have more than 1 "Argument Parser"
        args, remaining = parser.parse_known_args() # Analizes the command line for 'parser' 
        
        args2 = parser2.parse_args(['--arg1=34.2', 'This is the argumentX value'])  # Analyzes the given list 
                                                                                    # and create an object which attributes are the 'arg's names 
        
        # args2 = parser2.parse_args() -> will analize the command line and will transform the 'args' into an object which attributes are thos 'args'
        #                                 if there was only one parser in the code, otherwise it would generate erros for the 'args' that are not recognized

        vol = cylinder_volume(args.radius,args.height)
        print(f'Volume = {vol}')
        
        print(f'args = {args}\nremaining = {remaining}') # remaining contains all the 'args' that are not recognized as 'args' of 'parser' ('args' of 'parser2')
        
        print(f'args2 = {args2}')


# User may run the program like: 

# Example: 
# python argparseTutorial.py anystr -H 10 -u m3 dsqfds -a1 43.556 -a2 -12.654332
# Volume = 31.41592653589793
# args = Namespace(posArg='anystr', radius=1, height=10, unit='m3')
# remaining = ['dsqfds', '-a1', '43.556', '-a2', '-12.654332']
# args2 = Namespace(argumentX='argumentX=SDFQDs', arg1=34.2, arg2=None)