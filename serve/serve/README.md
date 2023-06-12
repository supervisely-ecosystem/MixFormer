# MixFormer object tracking

state-of-the art interactive object tracking (CVPR2022) integrated into Supervisely Videos Labeling tool


# Original work

Original work available by hyperlinks: [**paper (CVPR2022)**](https://arxiv.org/abs/2203.11082) and [**code**](https://github.com/MCG-NJU/MixFormer).

![Architecture](https://raw.githubusercontent.com/MCG-NJU/MixFormer/main/tracking/mixformer_merge_framework.png)


## Highlights
### New transformer tracking framework
MixFormer is composed of a **target-search mixed attention (MAM) based backbone** and a simple corner head, 
yielding a compact tracking pipeline without an explicit integration module.


### End-to-end, post-processing-free

Mixformer is an end-to-end tracking framework without post-processing. 

### Strong performance
| Tracker                | VOT2020 (EAO) | LaSOT (NP) | GOT-10K (AO) | TrackingNet (NP) |
| ---------------------- | ------------- | ---------- | ------------ | ---------------- |
| **MixViT-L (ConvMAE)** | 0.567         | **82.8**   | -            | **90.3**         |
| **MixViT-L**           | **0.584**     | 82.2       | **75.7**     | 90.2             |
| **MixCvT**             | 0.555         | 79.9       | 70.7         | 88.9             |
| ToMP101* (CVPR2022)    | -             | 79.2       | -            | 86.4             |
| SBT-large* (CVPR2022)  | 0.529         | -          | 70.4         | -                |
| SwinTrack* (Arxiv2021) | -             | 78.6       | 69.4         | 88.2             |
| Sim-L/14* (Arxiv2022)  | -             | 79.7       | 69.8         | 87.4             |
| STARK (ICCV2021)       | 0.505         | 77.0       | 68.8         | 86.9             |
| KeepTrack (ICCV2021)   | -             | 77.2       | -            | -                |
| TransT (CVPR2021)      | 0.495         | 73.8       | 67.1         | 86.7             |
| TrDiMP (CVPR2021)      | -             | -          | 67.1         | 83.3             |
| Siam R-CNN (CVPR2020)  | -             | 72.2       | 64.9         | 85.4             |
| TREG (Arxiv2021)       | -             | 74.1       | 66.8         | 83.8             |


# How to run


1. Add *add link* from Ecosystem


2. Run the app from **Plugins & Apps** page:

3. Select the model name. [MixViT-L](#strong-performance) is the default 

4. Run app on an agent with `GPU`

4. The model has been successfully deployed

5. Use in `Videos Annotator` 



# How to use

### :sparkles: TODO :sparkles:


# Controls

| Key                                                           | Description                               |
| ------------------------------------------------------------- | ------------------------------------------|
| <kbd>5</kbd>                                       | Rectangle Tool                |
| <kbd>Ctrl + Space</kbd>                                       | Complete Annotating Object                |
| <kbd>Space</kbd>                                              | Complete Annotating Figure                |
| <kbd>Shift + T</kbd>                                          | Track Selected     |
| <kbd>Shift + Enter</kbd>                                      | Play Segment     |




# Demo

### :sparkles: TODO :sparkles: