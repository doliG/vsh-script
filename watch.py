#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##########
# IMPORT #
##########
import os
import time


############
#  SET UP  #
############

# About watching
# --------------

# Path to watch : this is where the script looks for new file/folder
PATH_TO_WATCH = "./watch_folder"

# Refresh every X seconds
REFRESH = 1

# Time between comparaison of PATH_TO_WATCH
TIME_BETWEEN = 1

# folder corresponding to the photo's dimension
PHOTO_DIMENSION = "152x102"

# folder corresponding to the photo's paper's type
PAPER_TYPE = "glossy"

# REGEX ID client ? Todo #

print("--- WATCHER (in python) ---\nYour parameters :")

print("PATH_TO_WATCH   = {}".format(PATH_TO_WATCH))
print("REFRESH         = {}".format(REFRESH))
print("TIME_BETWEEN    = {}".format(TIME_BETWEEN))
print("PHOTO_DIMENSION = {}".format(PHOTO_DIMENSION))
print("PAPER_TYPE      = {}".format(PAPER_TYPE))
print("""----------------------------""")



#############
# FUNCTIONS #
#############

# Watch path and compare os.dir(path) with itself 10s later.
# Return new file(s) and folder(s).
def watcher(PATH_TO_WATCH):
    before = os.listdir(PATH_TO_WATCH)
    while 1:
        time.sleep(REFRESH)
        after = os.listdir(PATH_TO_WATCH)
        if before != after:
            print("Il y a du nouveau :")
            time.sleep(TIME_BETWEEN)
            new_files = []
            for afile in after:
                exist = 0
                for bfile in before:
                    if bfile == afile:
                        exist = 1
                if exist == 0:
                    new_files.append(afile)
            return new_files
        before = after

# Check if new_files contain an unique folder name composed by 6 digits.
# return 0 or 1
def is_it_id(new_files):
    if len(new_files) != 1:
        return 0
    if len(new_files[0]) != 6:
        return 0
    return 1

# SEARCHED NAME DEDICASSSSSE
# Search searched_name in path
# return 0 or 1
def search_in_folder(searched_name, path):
    for file in os.listdir(path):
        if file == searched_name:
            return 1
    return 0


def error_exit(action, *args):
    if action == "INVALID_CID":
        print("Error: new folder is not a valid client ID.")
    elif action == "FOLDER_!EXISTS":
        print("Error: folder '{}/' does not exist in '{}'/".format(*args))
    print("Exiting...")
    exit()


############
#   MAIN   #
############
new_files = watcher(PATH_TO_WATCH)


# Test if new_files ok.
if not is_it_id(new_files):
    error_exit("INVALID_CID")

# Getting cliend_id
cliend_id = new_files[0]

# New path to scan
path_to_scan = PATH_TO_WATCH + "/" + cliend_id

# print path_to_scan # debug

# Searching for PHOTO_DIMENSION in path_to_scan
if not search_in_folder(PHOTO_DIMENSION, path_to_scan):
    error_exit("FOLDER_!EXISTS", PHOTO_DIMENSION, path_to_scan)

# New path to scan
path_to_scan = path_to_scan + "/" + PHOTO_DIMENSION

# Searching for PAPER_TYPE in path_to_scan
if not search_in_folder(PAPER_TYPE, path_to_scan):
    error_exit("FOLDER_!EXISTS", PAPER_TYPE, path_to_scan)

# New path to scan
path_to_scan = path_to_scan + "/" + PAPER_TYPE
print("Chemin définitif : {}".format(path_to_scan))
