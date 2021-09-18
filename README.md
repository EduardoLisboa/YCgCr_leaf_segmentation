# YCgCr Leaf Segmentation
This is part of the project for the 2020.2 Deep Learning class at Universidade Federal de Alagoas.

The objective is to try to replicate and possibly improve the original paper by using Deep Learning techniques learned throughout the semester.

Student: Eduardo Antônio de Lucena Lisboa

---
## Original paper
Original paper was obtained on [Papers With Code][pwc] and can be found [here][original_paper].

The original repository can be found [here][original_repository].

---
## Dataset
The dataset used was the BRACOL dataset, a public domain Brazilian Arabica Coffee leaves dataset, which can be found [here][BRACOL_dataset].

To simplify, the version ready to be used with the training of the model can be found [here][drive_dataset].

---
## Folder structure
In order for the project to work properly, the folder structure must be as follows:

```
project
│   README.md
|   dataset.csv
│   k_means.py   
│   main.py
|
└── Dataset
│   └── testing
│   |   │   1.jpg
│   |   │   2.jpg
│   |   │   ...
|   |
│   └── training
|       └── diseased
|       |   |   68.jpg
|       |   |   100.jpg
|       |   |   ...
|       |
|       └── healthy
|           |   170.jpg
|           |   174.jpg
|           |   ...
|
└── Models
└── Plots
```
Obs.: _Models_ and _Plots_ folders start empty. They **must** be created of the code might give some errors.

---

## Accomplished Tasks
- [X] Commit the original code
- [X] Refactor original code
- [X] Make first CNN model
- [X] Upload dataset
- [ ] Improve CNN model


[pwc]: https://paperswithcode.com
[original_paper]: https://paperswithcode.com/paper/a-smartphone-application-to-detection-and
[original_repository]: https://github.com/FrexG/ycgcr_leaf_segmentation
[BRACOL_dataset]: https://data.mendeley.com/datasets/yy2k5y8mxg/1
[drive_dataset]: https://drive.google.com/file/d/1-L_L6BWnu-1szQvsKBoMz18K64-_iAGV/view?usp=sharing
