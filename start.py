import sys

# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'build\\exe.win-amd64-3.10')
with open("sending_info.py") as f:  # open file
    exec(f.read())  # starting file

# TODO: Documentation - 50/50
# TODO: APP - DONE
# TODO: LOCATION COORDINATES - DONE
# TODO: GUI - location - DONE
