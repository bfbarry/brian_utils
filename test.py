import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', dest='manual', nargs=2)

args = parser.parse_args()

print(args.manual)