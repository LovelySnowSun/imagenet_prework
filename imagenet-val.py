# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 13:53:07 2021

@author: 78505
"""
import scipy.io
import os,glob,shutil

def move_valimg(val_dir='D:/imagenet/val', devkit_dir='X:/imagenet/ILSVRC2012数据集/ILSVRC2012_devkit_t12'):
    """
    move valimg to correspongding folders.
    val_id(start from 1) -> ILSVRC_ID(start from 1) -> WIND
    organize like:
    /val
       /n01440764
           images
       /n01443537
           images
        .....
    """
    # load synset, val ground truth and val images list
    synset = scipy.io.loadmat(os.path.join(devkit_dir, 'data', 'meta.mat'))
    
    ground_truth = open(os.path.join(devkit_dir, 'data', 'ILSVRC2012_validation_ground_truth.txt'))
    lines = ground_truth.readlines()
    labels = [int(line[:-1]) for line in lines]
    
    path_list = glob.glob(os.path.join(val_dir,'*'))
    print(path_list)
    for filename in path_list:
        # val image name -> ILSVRC ID -> WIND
        val_id = int(filename.split('.')[0].split('_')[-1])
        ILSVRC_ID = labels[val_id-1]
        WIND = synset['synsets'][ILSVRC_ID-1][0][1][0]
        print("val_id:%d, ILSVRC_ID:%d, WIND:%s" % (val_id, ILSVRC_ID, WIND))
 
        # move val images
        output_dir = os.path.join(val_dir, WIND)
        if os.path.isdir(output_dir):
            pass
        else:
            os.mkdir(output_dir)
        shutil.move(filename, os.path.join(output_dir, filename.split('\\')[1]))
    
                    
if __name__ == '__main__':
    move_valimg()