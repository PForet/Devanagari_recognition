#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 12:23:01 2017

@author: pierreforet
"""

import os
from PIL import Image
def test_data():
    
    # Test if the directory from kaggle is attached to the project
    if not 'devanagari-character-dataset' in os.listdir(os.getcwd()):
        raise ValueError("The character dataset was not found in the main folder")
        
    # Test if all elements are in this directory
    available_files = os.listdir('devanagari-character-dataset')
    missings = [afile not in available_files for afile in ['consonants', 'labels.csv', 'numerals', 'vowels']]
    if any(missings):
        raise ValueError("'consonants', 'labels.csv', 'numerals', 'vowels' \
             should be in the 'devanagari-character-dataset' directory")
        
# Run test function on import
test_data()


def PIL_list_data(characters_type):
    
    # Check if the input is valid
    assert characters_type in ['consonants', 'vowels', 'numerals']
    
    img_path = os.path.join('devanagari-character-dataset',characters_type)
    img_list, img_labels = [], []
    
    # We remove files starting with a dot to exclude hidden files (like .DS_Store)
    hidden_files_removed = [fl for fl in os.listdir(img_path) if fl[0] != '.' ]
    
    # Loop over classes then images in the classes. Append the results to the lists
    for class_id in hidden_files_removed:
        for one_img in os.listdir(os.path.join(img_path, class_id)):
            
            # Open images with PIL if the file is not a hidden one
            if one_img[0] != '.':
                
                # Workaround to counter the 'too many open files' error in PIL
                temp_img = Image.open(os.path.join(img_path, class_id, one_img))
                img_list.append(temp_img.copy())
                temp_img.close()
                
                img_labels.append(class_id)
            
    # Report and return
    print("Raw {} loaded, {} obs of {} classes".format(characters_type,
              len(img_list), len(set(img_labels))))
    return img_list, img_labels

