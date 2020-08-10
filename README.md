# Ethoflow
A computer vision and artificial intelligence-based software for automatic behavior analysis

**Please cite our manuscript:**

Bernardes, R. C., Lima, M. A. P., Guedes, R. N. C., & Martins, G. F. (2020). Ethoflow: computer vision and artificial intelligence-based software for automatic behavior analysis. BioRxiv, 2020.07.23.218255. doi:10.1101/2020.07.23.218255

DOI of the data: [![DOI](https://zenodo.org/badge/281779165.svg)](https://zenodo.org/badge/latestdoi/281779165)
__________________________________________________________________
Authors:
   
  - PhD [Rodrigo Cupertino Bernardes](https://www.researchgate.net/profile/Rodrigo_Cupertino_Bernardes) (Federal University of Vicosa). *developer*. Email: rodrigo.bernardes@ufv.br
  
  - PhD Maria Augusta Pereira Lima (Federal University of Vicosa).  
  - PhD Raul Narciso Carvalho Guedes (Federal University of Vicosa).
  - PhD Gustavo Ferreira Martins (Federal University of Vicosa).
  
  __________________________________________________________________
  ## Getting started
  To use graphics processing unit (GPU), install (recommended version for windows 10):
  
  +[CUDA 10](https://developer.nvidia.com/cuda-10.0-download-archive) and [CUDNN 7.4](https://developer.nvidia.com/rdp/cudnn-archive)
  + Install python directly from python.org (recommended version 3.6.8). This will already come with pip
  + install virtualenv - open the prompt and run: pip install virtualenv
  + Create a virtual environment - virtualenv path\path... 
  + Activate the environment and inside the Ethoflow folder, install dependencies by running:
    pip install -r requirements.txt
    
  **Obs.:** the version to be installed from the tensorflow library requires a machine with a GPU. If you are going to use ethoflow on a machine without a gpu, install the CPU-only version: 'pip install tensorflow == 1.14.0'  
    
    
__________________________________________________________________

This repository contains

  * Ethoflow_v1: This folder contains the files of source code.
  
      + images: icons and images of the graphical user interface (GUI)
      + Ethoflow: It is the main script
      + gui: The information regarding the GUI 
      + utils
      
      + make_mask_rcnn_data: folders were the files to generate instance segmentation model train data with an heuristic 
           + backgorunds: folder where random backgrounds should be placed to Ethoflow get.
           + mask_imgs: folder where Ethoflow saves the images to train instance segmentation model
           + mask_video_tests: video example to Ethoflow run heurist and to test after training
           + train: examples of the images generate to train Ethoflow to recognize bees (*Melipona quadrifasciata*) in random background
           + val: examples of the images generate to validate Ethoflow in recognition of the bees (*M. quadrifasciata*) in random background
           
            **Obs.:** after generate images, paste to:  train_mask_rcnn/Mask_RCNN/dataset

      + train_mask_rcnn: After generate the dataset (in make_mask_rcnn_data), we recommend upload this folder in Google colab to train the model.
           + logs: when training a model, it will be saved in this folder train_mask_rcnn/Mask_RCNN/logs. Paste this model in the train_mask_rcnn / logs folder to be able to inspect the model 
           + Mask_RCNN: files needed to Ethoflow run instance segmentation model.
           + Inspect_trained_model: notebook to check the trained model
           + Train_instance_segmentation: notebook to train  instance segmentation model
           
       + complex_behavior: folder with files to train the model in recognition complex behavior
           + cnn: it contains a notebook to train the model, a file with necessary functions and data example
           + train_imgs_behavior: example of data about complex behavior (trophallaxis) in stingless bee *Melipona quadrifasciata*
           
       + utils: it contains files with functions to run into Ethoflow
       
       + videos_example_ethoflow: examples of files processed with Ethoflow
      
  
  * Dataset: files used in manuscript
  
       + data_software_application: data from behavioral assay in Ethoflow validation 
       + data from software performance associated with The fps and centrality of individuals 
