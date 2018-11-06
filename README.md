# robot_learning
This is the repository for the robot learning project by Nina Tchirkova and Isaac Vandor

## To learn more:
[See the writeup](https://github.com/isaacvandor/robot_learning/blob/master/project_writeup.md)

[Read the papers linked here](https://github.com/isaacvandor/robot_learning/blob/master/project_proposal.md)

## To get up and running:
1. Go to this Google Drive link to download the dataset used: https://drive.google.com/drive/folders/1EBNk1qrS5vjNRIgOwIoJWuwqBjcyWvA8?usp=sharing
2. Clone this repository
3. Move the downloaded folder to the base of this project repo (i.e. robot_learning is the name of this repo, speech_dataset should be within robot_learning)
4. Open up a terminal window and start ros with `roscore`
5. Open up a new terminal window and run `commands.py`
6. Open up another terminal window and run `predict.py`

If you want to change the spectrogram being inputted into the model, you can call `predict.py` with the command line argument -p followed by the path to your spectrogram. For other uses, contact either Nina or Isaac.
