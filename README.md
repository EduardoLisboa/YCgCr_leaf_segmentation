# YCgCr Leaf Segmentation
This is part of the project for the 2020.2 Deep Learning class at Universidade Federal de Alagoas.

The objective is to try to replicate and possibly improve the original paper by using Deep Learning techniques learned throughout the semester.

Student: Eduardo Antônio de Lucena Lisboa

---
## Original paper
Original paper was obtained on [Papers With Code][pwc] and can be found [here][original_paper].

The original repository can be found [here][original_repository].

---
## Dataset and Model
The dataset used was the BRACOL dataset, a public domain Brazilian Arabica Coffee leaves dataset, which can be found [here][BRACOL_dataset].

This dataset contains Brazilian Arabica Coffee leaves images which are 2048 x 1024 pixels is size and labeled with four diseases (these being _Rust_, _Miner_, _Cercospora_ and _Phoma_) and their severity. For this project, only was considered if the leaf has a disease or not.

To simplify, the version ready to be used with the training and testing of the model can be found [here][drive_dataset].

And the model to use with the main code can be found [here][drive_best_model].

---
## Folder structure
In order for the project to work properly, the folder structure must be as follows:

```
project
│   README.md
|   Accuracy Tests.ipynb
|   CNN_Model.ipynb
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
|   └── best_model.h5
|
└── images
|   |   1.jpg
|   |   2.jpg
|   |   ...
|
└── Plots
```
Obs.: _Plots_ folder starts empty. It **must** be created or the code will not work.

---

## Accomplished Tasks
- [X] Commit the original code
- [X] Refactor original code
- [X] Make first CNN model
- [X] Upload dataset
- [X] Implement accuracy evaluation
- [X] Improve CNN model
- [X] Upload best model
- [X] Upload example images
- [X] Merge model with main program
- [X] Document CNN notebook
- [X] Document Accuracy Tests notebook
- [ ] Document main program


[pwc]: https://paperswithcode.com
[original_paper]: https://paperswithcode.com/paper/a-smartphone-application-to-detection-and
[original_repository]: https://github.com/FrexG/ycgcr_leaf_segmentation
[BRACOL_dataset]: https://data.mendeley.com/datasets/yy2k5y8mxg/1
[drive_dataset]: https://drive.google.com/file/d/1-L_L6BWnu-1szQvsKBoMz18K64-_iAGV/view?usp=sharing
[drive_best_model]: https://drive.google.com/file/d/1bG_zCeSDgv538UkPjF62TjqpeHZ8ZBkK/view?usp=sharing
