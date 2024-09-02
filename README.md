# VoxLRS-SA
This repository contains the speaker labeled information of VoxCeleb2 and LRS3 audio-visual datasets, which is the outcome of the following paper:


### Dataset layout
    Path to Datasets(e.g., /home/Dataset/...)
    ├── lrs3
    │     ├── lrs3_video_seg24s               # Preprocessed video and audio data
    │     └── lrs3_text_seg24s                # Preprocessed text data
    ├── vox2                        # VoxCeleb2
    │     ├── train.tsv                       # List of audio and video path for training
    │     ├── train.wrd                       # List of target label for training
    │     ├── train.cluster_counts            # List of clusters to deduplicate speech units in training
    │     ├── test.tsv                        # List of audio and video path for testing
    │     ├── test.wrd                        # List of target label for testing
    │     └── test.cluster_counts             # List of clusters to deduplicate speech units in testing
    └── test_data
          ├── vsr
          │    └── en
          │        ├── test.tsv 
          │        ├── test.wrd  
          │        └── test.cluster_counts           
          └── vst
               └── en
                   ├── es
                   :   ├── test.tsv
                   :   ├── test.wrd 
                   :   └── test.cluster_counts
                   └── pt
                       ├── test.tsv
                       ├── test.wrd 
                       └── test.cluster_counts
