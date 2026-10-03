import sys

# Collecting argument using sys module at the run time
args_number1 = sys.argv[1]
args_number2 = sys.argv[2]

# printing the arguments provided by the user
print("The  arguments provided when the file was run : ")
print("argument 1 : ", args_number1)
print("argument 2 : ", args_number2)


# using the sys module to control the flow of the program from the aeguments
print()
if not args_number1:
    print("There was argument for the argument 1")
    sys.exit(1) # exits the program without executing further statements 0 means sucess and any other value is failure

print("The arguments were provided no need to exit the program")

# checking data quality
print()
if args_number1 is int:
    print("The provided argument is not an integer so exiting the program")
    sys.exit(1)

print("The argument was an integer as expected") 

# read environment/platform information
print()
print("The platform is : ")
print(sys.platform)

if sys.platform.startswith("linux"):
    print("running in linux...............")
else:
    print("The code is not running is linux")

# identifying the python version
print()
print("The python vesrion : ", sys.version," ", sys.version_info)

# printing system path
print()
print("The location of the program is : ", sys.path)

# list all the modules in the system currently
print()
print("List of the modules present in the container : ", sys.modules)

# get the executable running of the python program
print()
print("The location of the python executable is : ", sys.executable)
