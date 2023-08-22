---
layout: single
title: Modern VSLAM
categories: Autonomous_Driving_course
use_math: true
---

## Modern SLAM
1. Fusion of several sensors
2. Various strategies to sontrust factor graph
3. Joint optimization of motion & observation model

## Types of computation
1. Frame-to-Frame tracking
2. Sliding-window local map optimization
3. Global map optimization / Loop closure

## Frame-to-Frame tracking
* Computes camera pose every frame(i.i. 30FPS)
* Does not construct map
* Steps
    1. Color conversion(RGB -> Gray)
    2. Resize image
    3. Detect features
    4. Match features with..
        * Previous frame
            * 2d - 2d correspondence - E/F matrix
        * Keyframe
            * 2d - 3d correspondence - PnP
    5. Estimate motion

## Sliding-window local map optimization
* Bundle adjustment on previous N Keyframes
* Performs every new keyframe / every N new keyframes (50-500ms)
* Steps
    1. Check if current image is a keyframe
        * if keyframe, triangulate features to make new 3D points - Triangulation
    2. Jointly optimize camera poses and landmarks
        * Bundle adjustment - BA, Non-linear optimization

## Global map optimization
* Only performs map optimization when...
    * Loop closure is found
    * SLAM is finished
* Processing time depends on size of graph
* Steps
    1. Detect loop
        * Bag-of-visual-words
    2. Estimate pose
        * PnP
    3. Optimize loop
        * Bundle adjustment