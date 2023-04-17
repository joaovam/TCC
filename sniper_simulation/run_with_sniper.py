import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m","--mode",help="Mode to run = [Tiny, Small, Default, large, Huge]")
parser.add_argument("-d","--directory",help="Target Directory")
parser.add_argument("-t","--thread",help="Number of threads")

args = parser.parse_args()
# Specify the path to the Sniper simulator binary
SNIPER_FOLDER = "/home/joaovam/Documents/snipersim"

# Specify the path to the Sniper configuration file
SNIPER_CONFIG = "./test.cfg"


os.environ["BENCHMARKS_ROOT"]  = args.directory
# Get the list of executable files to run from the command-line arguments

files = os.listdir(args.directory)


# Loop over the executable files and run each one using the Sniper simulator
for app in files:
    folder = "%s/cap_output/%s_%s_%s" % (SNIPER_FOLDER, args.mode.lower(),args.thread , app)

    if not os.path.exists(folder):
        os.makedirs(folder)

    # Construct the command-line arguments to run the executable with the Sniper simulator
    cmd = "{}/run-sniper -v -c {} -d {} -- {} --nthreads {} --class {}".format(SNIPER_FOLDER,
                                                                          SNIPER_CONFIG,
                                                                          folder,
                                                                          args.directory + app,
                                                                          args.thread, args.mode.lower())

#    ../../run-sniper -v -n 1 -c gainestown --roi -- ./fft -p 1

    # Print the command being executed
    print("Running command: {}".format(cmd))

    # Run the command using the os.system() function
    os.system(cmd)
