import sys, os


# Without this line, pytest won't be able to import modules from outside tests/.
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
