# Safe Sea Voyage

## Overview

![Screenshot from 2024-03-09 13-50-03](https://github.com/morikeli/safe-sea-voyage/assets/78599959/5fb00fc9-4a5d-4593-b274-f98e5d37a75f)

This is a machine learning model that predicts whether you would have survived the Titanic incident on 15 April 1912. The model uses Random Forest to make prediction. For more details about how I trained the model, click [My machine learning projects](https://github.com/morikeli/ml-projects-arena) and follow the installation guide in README.md You can also click 'titanic-survival-prediction' and view 'titanic-survival-prediction.ipynb' Jupyter notebook.

## User instructions
To use the app, click [link](https://safe-sea-voyage.streamlit.app/) and enter data in the input fields provided. Once you are done, click the submit button and wait for response. A message with the outcome results will be displayed below the submit button.

## Developer instructions
Installation instructions

```(bash)
  $ cd Desktop
  $ git clone https://github.com/morikeli/safe-sea-voyage.git
  $ python3 -m venv .safe-seas-venv
  $ source .safe-seas-venv/bin/activate
  $ pip install -r requirements.txt
```
Once the installation is done, type the following command to run the streamlit web app:
```(bash)

  $ streamlit run main.py

```

## Known issues
Incase of an error or bug create an issue using the `Issues` tab or create a new branch using Git and make a pull request.

Don't forget to star the repo 🌟😉
