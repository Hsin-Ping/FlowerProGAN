#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:28:48 2024

@author: wangxinping
"""
import os
import cv2
import glob
import numpy as np

def create_video(root_dir, video_dim, fps, steps, epochs, videoname):
    out = cv2.VideoWriter(f'{videoname}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, video_dim)
    for step in range(steps):
        dirname = os.path.join(root_dir, f"step{step}")
        for n_epoch in range(epochs):
            filepath = os.path.join(dirname, f"Epoch_{n_epoch}.jpg")
            img = cv2.imread(filepath)
            text = f"Step{step}_Epoch{n_epoch+1}"
            frame = cv2.resize(img, video_dim)
            cv2.putText(frame, text, (10, 45), cv2.FONT_HERSHEY_PLAIN, 2.0, (0,0,0), thickness=2)
            out.write(frame)

    out.release()
    return
            
    
    




if __name__ == "__main__":
    root_dir = os.path.join(os.getcwd(), "results")
    video_dim = (1024, 1024)
    fps = 10.0 # fps has to be float and 10的倍數
    steps = 6
    epochs = 30
    videoname = "FlowerGAN"
    
    create_video(root_dir, video_dim, fps, steps, epochs, videoname=videoname)

            
        
        
        
