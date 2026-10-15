# ML Based Network Intrusion Detection System (NIDS)

## Overview

This research project aims to answer the following question: Does an Intrusion Detector Travel? Measuring and Explaining Cross-Network Failure in ML-Based NIDS

The research proposal will soon be added to the github.

The project website can be found here: https://sites.google.com/oakland.edu/csi-4460-team-4/

## Setup Instructions

### Repo Clone and Setup

If you do not already have `uv` installed, you can do so from here -> https://docs.astral.sh/uv/getting-started/installation/

Once `uv` is installed clone the repository to your local machine

```
git clone https://github.com/loqran/ML-Based-NIDS.git ML-Based-NIDS
cd ML-Based-NIDS
```

Then setup everything by running

```
uv run
```

This will create a `.venv`, and install all the necessary libraries and ensure there is no version mismatch

Make sure to also run `mkdir data/` to create a folder for the two datasets. Dataset installation instruction can be found below.

### Datasets

The Datasets we will be using are NF-UNSW-NB15-v2 and NF-CSE-CIC-IDS2018-v2. Both of these datasets can be found here https://staff.itee.uq.edu.au/marius/NIDS_datasets/. After installing both datasets move them into the `data/` folder within the project directory. Then run the following commands to unzip the data.

```
unzip b3427ed8ad063a09_MOHANAD_A4706.zip
unzip fe6cb615d161452c_MOHANAD_A4706.zip
```

Once the files are unzipped and ready, ensure you activate the `.venv`. Then to clean the dataset, labeling each flow as either benign (0) or attack (1) and removing IP addresses run the following from the project root:

```
python tools/clean.py
```

### Jupyter Notebook

After running `clean.py` the data will be ready for processing. In the future I might integrate `clean.py` into the notebook to make the process more straight forward. To access jupyter notebook, in your terminal run

```
uv run jupyter lab
```

You can then access the notebook at http://localhost:8888/. From there you can find the code in the `notebooks/` folder.

### Pushing to the repo

Prior to pushing anything ensure that you are on a new branch, you can do that by running

```
git checkout -b <branch-name>
```

Then to push that branch to the repo do

```
git push -u origin <branch-name>
```

This will prevent multiple pushes to main at the same time. I do not want to deal with _git_ troubleshooting.
