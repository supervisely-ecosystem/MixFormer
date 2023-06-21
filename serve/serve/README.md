<div align="center" markdown>

<img src="https://github.com/supervisely-ecosystem/MixFormer/assets/12828725/6a8e0b07-9a2a-4fd8-a34b-58e589b3a10a"/>  

# MixFormer object tracking (CVPR2022)

state-of-the-art interactive object tracking (CVPR2022) integrated into Supervisely Videos Labeling tool

<p align="center">
  <a href="#Original-work">Original work</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#How-To-Use">How To Use</a> •
    <a href="#Demo">Demo</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/mixformer)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/mixformer)
[![views](https://app.supervise.ly/img/badges/views/supervisely-ecosystem/mixformer.png)](https://supervise.ly)
[![runs](https://app.supervise.ly/img/badges/runs/supervisely-ecosystem/mixformer.png)](https://supervise.ly)

</div>

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

1. Add [MixFormer object tracking (CVPR2022)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/mix-former/serve/serve) from Ecosystem.  

<img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/mixformer/serve/serve" src="XXX" width="600px" style='padding-bottom: 20px'/> 

2. Run the app from **Neural Networks** page:

3. Select the model name [MixViT-L](#strong-performance) is the default.

4. Run app on an agent with `GPU`.

4. The model has been successfully deployed.

5. Use in `Videos Annotator`.



# How to use

<table>
  <tr style="width: 100%">
    <td>
      <a data-key="sly-embeded-video-link" href="https://youtu.be/EMvqTFu1ILE" data-video-code="EMvqTFu1ILE">     <img src="https://imgur.com/a19csV9.jpg" alt="SLY_EMBEDED_VIDEO_LINK"  style="width:100%;"> </a>
    </td>
    <td>
      <a data-key="sly-embeded-video-link" href="https://youtu.be/Xa6WeIgw_mI" data-video-code="Xa6WeIgw_mI">     <img src="https://imgur.com/n2P5qSL.jpg" alt="SLY_EMBEDED_VIDEO_LINK"  style="max-width:100%;"> </a> 
    </td>
  </tr>
</table>


# Controls

| Key                                                           | Description                               |
| ------------------------------------------------------------- | ------------------------------------------|
| <kbd>5</kbd>                                       | Rectangle Tool                |
| <kbd>Ctrl + Space</kbd>                                       | Complete Annotating Object                |
| <kbd>Space</kbd>                                              | Complete Annotating Figure                |
| <kbd>Shift + T</kbd>                                          | Track Selected     |
| <kbd>Shift + Enter</kbd>                                      | Play Segment     |




# Demo

We have prepared a videos and demonstrated how TransT works:

https://github.com/supervisely-ecosystem/MixFormer/assets/119248312/6bd93aa7-d9c3-4a5b-8dd3-758d179bf88f

https://github.com/supervisely-ecosystem/MixFormer/assets/119248312/877dc5f4-275f-4e06-b2df-ad2509a0e3ca

https://github.com/supervisely-ecosystem/MixFormer/assets/119248312/c32a46eb-b202-4618-9f3e-91d4391d4ec8

https://github.com/supervisely-ecosystem/MixFormer/assets/119248312/893bce9c-c700-4947-ac3c-4e51b7c8c72f

