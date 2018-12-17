#!/usr/bin/env python3
import argparse
import os
import glob

def main(args=None):
    parser = argparse.ArgumentParser(description='FreeSurfer aparcstats2table')
    parser.add_argument('--output_directories',
       		        help='List of directories that one can use that contains the subject data',
                        nargs='+')
    parser.add_argument('--subjects_file',
                        help='The output subject file')
    opts = parser.parse_args() if args is None else parser.parse_args(args)

    
    subject_dirs = []
    for x in opts.output_directories:
        sub_dir = glob.glob("{0}/sub-*".format(x))
        if len(sub_dir) > 0:
            subject_dirs.append(sub_dir[0])
    if len(subject_dirs) > 0:
        with open("{0}".format(opts.subjects_file),"w") as f:
            for x in subject_dirs[:-1]:
                f.write("{0}\n".format(x))
            f.write("{0}".format(subject_dirs[-1]))
     
if __name__ == "__main__":
    main()

