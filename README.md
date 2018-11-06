# Robot Learning
This is the repo for the comprobo robot learning project by Nina Tchirkova and Isaac Vandor 

## Project Goals
The goal of this project was to have a robot be able to "hear" a command and respond to it by doing a certain behavior. The way the robot would interpret the sound was by using a neural net that was trained on many sound files of people saying words. 

## Implementation
Talk about data set / neural net here

To collect test data, sound data is collected by connecting to a Raspberry Pi that is able to record audio. The continuous wav file is broken down into 1.5 seconds chunks at 0.1 second intervals. To minimize the amount of data to be processed, each chunk is condensed into an ogg file to see if it contains any sound. We chose this strategy because of the paper, *Speech Commands: A Dataset for Limited-Vocabulary Speech Recognition* by Pete Warden. If the ogg file is not silent, then a 1.5 second wav file is saved to a directory. All the wav files from this directory are converted into spectograms and passed through the neural net. Based on the word the neural net thinks is the wav file, the robot does a specific action.

## Design Decision
To model other natural language processing systems, we decided to work with a continuous stream of input. This meant that most of the sound we were recording was not even a word. This presented some extra challenges but we learned that using Python, it is possible to simultaneously read and write to the same file.

## Challenges
A major challenge we encountered was that our model was overfitting to the data set. This meant that every word was determined to be "bird".

## Future Work and Improvements
One obvious improvement would be to improve the accuracy of our model. This could be done by determining what features of the spectogram are the most important and then condensing the spectorgrams to where those are located. There could also be better preprocessing of wav files so that truly relevant spectrograms are processed. 

## Interesting Findings
Although probably not advisable, it is totally possible to read from a file that is also being written to at the same time. We took care so that the model always read from a part that was already written. 
