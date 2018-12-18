#!/usr/bin/env python3
import argparse
import os
import glob
import csv


def dir_exists(parser, dir_name):
    if not os.path.isdir(dir_name):
        parser.error("Directory not correct, either doesn't exist or is not a directory {0}".format(dir_name))
    return dir_name


def main(args=None):
    parser = argparse.ArgumentParser(description='FreeSurfer aparcstats2table')
    parser.add_argument('--filecol',type=lambda x: dir_exists(parser,x), 
       		        help='CBRAIN file collection with all directories that one can use that contains the subject data')
    parser.add_argument('--subjects_file',
                        help='The output subject file')
    opts = parser.parse_args() if args is None else parser.parse_args(args)

    
    subject_dirs = glob.glob("{0}/*/sub-*".format(opts.filecol))

    if len(subject_dirs) > 0:
        with open("{0}".format(opts.subjects_file),"w") as f:
            for x in subject_dirs[:-1]:
                f.write("{0}\n".format(x))
            f.write("{0}".format(subject_dirs[-1]))
     
if __name__ == "__main__":
    main()

