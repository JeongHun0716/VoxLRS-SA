# VoxLRS-SA
To validate speaker adaptive lip reading methods in real-world scenarios, we introduce a new dataset named VoxLRS-SA, derived from VoxCeleb2 and LRS3 datasets.
This repository contains the speaker ID information of VoxCeleb2 and LRS3 audio-visual datasets, which is the outcome of the following paper:
> **Personalized Lip Reading: Adapting to Your Unique Lip Movements with Vision and Language**<be>
><br>
> Jeong Hun Yeo, Chae Won Kim, Hyunjun Kim, Hyeongseop Rha, Seunghee Han, Wen-Huang Cheng, Yong Man Ro<br>
> \[[Paper](https://arxiv.org/abs/2409.00986)\]
<div align="center"><img width="100%" src="img/img1.png?raw=true" /></div>

## Dataset preparation
For Training and Inference the model, VoxCeleb2, and LRS3 Datasets are needed. 
  1. Download the VoxCeleb2 dataset from the [VoxCeleb2 link](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox2.html) of the official website.
  2. Download the LRS3 dataset from the [LRS3 link](https://mmai.io/datasets/lip_reading/) of the official website.

## Dataset Preprocessing
After downloading the datasets, you should detect the facial landmarks of all videos and crop the mouth region using these facial landmarks. We recommend you preprocess the videos following [Visual Speech Recognition for Multiple Languages](https://github.com/mpc001/Visual_Speech_Recognition_for_Multiple_Languages).  

### Dataset layout
    Path to Datasets(e.g., /home/Dataset/...)
    ├── lrs3
    │     ├── lrs3_video_seg24s               # Preprocessed video data
    ├── vox2                                  # VoxCeleb2
    │     └── en
    │          └── video                     # Preprocessed video data


### Data structure
The Speaker ID information is included in the *.tsv files.
```bash
# Example in line 2 of baseline/test.tsv
voxlrs-00001	/Path_to_Datasets/vox2/en/video/dev/mp4/id05998/nfWYhJyGsPU/00370_00.mp4	/Path_to_Datasets/vox2/en/video/dev/mp4/id05998/nfWYhJyGsPU/00370_00.mp4	241	241
(Speaker ID)    (Path to Video)    (Path to Video)    (Number of frames in video)    (Number of frames in video) 
```
If you want to design personalized audio-visual speech recognition, you replace the 3rd item (Path to Video) and 5th item (Number of frames in video) with audio information.  

### Path Modification
All manifest files are provided in this repo. You need to replace the video path in the manifest file with your preprocessed video path using the following command:
```bash
python path_modification.py --dataset_pth /path/to/datasets
```

### VoxLRS-SA data splits
In order to build unseen-speaker scenario (train and test speakers are not overlapped), 20 speakers are selected for test and validation (adaptation).


<div align="center"><img width="100%" src="img/img2.png?raw=true" /></div>

For more information, please refer to our paper.


### Contributing
For more accurate speaker information, we welcome your participation in improving label information.

## Citation
If you find this work useful in your research, please cite the paper:
```bibtex
@article{yeo2024personalized,
  title={Personalized Lip Reading: Adapting to Your Unique Lip Movements with Vision and Language},
  author={Yeo, Jeong Hun and Kim, Chae Won, Kim, Hyunjun, Rha, HyeongSeop, Han, Seunghee, Wen-Huang Cheng, Ro, Yong Man},
  journal={arXiv preprint arXiv:2409.00986},
  year={2024}
}
```
