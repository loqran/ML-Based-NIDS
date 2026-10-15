# ML Based Network Intrusion Detection System (NIDS)

## Overview

This research project aims to answer the following question: Does an Intrusion Detector Travel? Measuring and Explaining Cross-Network Failure in ML-Based NIDS

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
