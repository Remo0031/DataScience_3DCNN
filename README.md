# DataScience_3DCNN
This repository is an implementation of 3D CNN on SPHAR dataset which includes Training, Validation and Inference 

# Required Files
- python3==3.6.13
- opencv3==3.4.2
- keras==2.6.0
- numpy==1.19.2
- tqdm==4.64.1

# Options
Options of 3dcnn.py are as following:
- --batch batch size, default is 128
- --epoch the number of epochs, default is 100
- --videos a name of directory where dataset is stored, default is UCF101
- --nclass the number of classes you want to use, default is 101
- --output a directory where the results described above will be saved
- --color use RGB image or grayscale image, default is False
- --skip get frames at interval or contenuously, default is True
- --depth the number of frames to use, default is 10

You can see more information by using --help option

# Structure of Dataset
- Dataset/
  - CarCrash/
    - CarCrash1.mp4
    - CarCrash2.mp4
  - Walking/
    - walking1.mp4
    - walking2.mp4
    - ...
 
# How to run
To run training use this make sure to change the necessary Arguments
```bash
python 3dcnn.py --batch 32 --epoch 50 --videos dataset/ --nclass 10 --output 3dcnnresult/ --color True --skip False --depth 10
```

To Run the inference 

Change the necessary directory in the inference.ipynb located at the 3dcnnresult

To Run the Validation

Change the directory location within loaddata of validation.ipynb to the directory of your valid dataset 

# Reminder
Make sure the packages you install are compatible with each other to not encounter error while trying the model
