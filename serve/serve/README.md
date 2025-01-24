<div align="center" markdown>

<img src="https://github.com/supervisely-ecosystem/MixFormer/assets/12828725/6a8e0b07-9a2a-4fd8-a34b-58e589b3a10a"/>  

🔥🔥🔥 Check out our [youtube tutorial](https://youtu.be/nyMilMvF3FM) and the [complete guide to Object Tracking in our blog ](https://supervisely.com/blog/complete-guide-to-object-tracking-best-ai-models-tools-and-methods-in-2023/)

<a href="https://youtu.be/nyMilMvF3FM" target="_blank"><img src="https://github.com/supervisely/blog-raw-media-content/assets/106374579/1c397223-0793-4130-bbcd-a0e7ea076fe2"/></a>

# MixFormer object tracking (CVPR2022)

state-of-the-art interactive object tracking (CVPR2022) integrated into Supervisely Videos Labeling tool

<p align="center">
  <a href="#Original-work">Original work</a> •
  <a href="#How-To-Run">How To Run</a> •
  <a href="#How-To-Use">How To Use</a> •
    <a href="#Demo">Demo</a>
</p>

[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervisely.com/apps/supervisely-ecosystem/mixformer)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervisely.com/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/mixformer)
[![views](https://app.supervisely.com/img/badges/views/supervisely-ecosystem/mixformer/serve/serve.png)](https://supervisely.com)
[![runs](https://app.supervisely.com/img/badges/runs/supervisely-ecosystem/mixformer/serve/serve.png)](https://supervisely.com)

</div>

# Original work

Original work is available here: [**paper (CVPR2022)**](https://arxiv.org/abs/2203.11082) and [**code**](https://github.com/MCG-NJU/MixFormer).

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

0. This object tracking app is started by default in most cases by an instance administrator. If it isn't available in the video labeling tool, you can contact your Supervisely instance admin or run this app by yourself following the steps below.

2. Add [MixFormer object tracking (CVPR2022)](https://ecosystem.supervisely.com/apps/supervisely-ecosystem/mix-former/serve/serve) from Ecosystem.  

<img data-key="sly-module-link" data-module-slug="supervisely-ecosystem/mixformer/serve/serve" src="https://github.com/supervisely-ecosystem/MixFormer/assets/119248312/e74e2bd9-f915-48b1-bb97-ee808326dff5" width="500px" style='padding-bottom: 20px'/> 

2. Run the app from **Neural Networks** page from category **detection & tracking videos**.

<img src="https://github.com/supervisely-ecosystem/MixFormer/assets/119248312/81f8a297-f4fc-48f3-854e-81674f252c36"/>  

3. Select the model [MixViT-L](#strong-performance).

4. Run app on an agent with `GPU`.

<img src="https://github.com/supervisely-ecosystem/MixFormer/assets/119248312/7b684bdb-2cbc-4d9f-8cc9-d5e9212c6b17"/>

5. Use in `Videos Annotator`.

<img src="https://github.com/supervisely-ecosystem/MixFormer/assets/119248312/fa438859-b46f-423f-b8a9-78e52396613e"/>
   
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

We have prepared videos and demonstrated how MixFormer works:

https://user-images.githubusercontent.com/119248312/247612713-78b67bfc-d947-4c29-b886-d64445c54944.webm

https://user-images.githubusercontent.com/119248312/247613164-eab83a4b-527e-4b2a-b3e0-f9a0bfef5c4e.webm

https://user-images.githubusercontent.com/119248312/247613202-177c7e67-8657-4a8d-b920-3ebfe1126547.webm
