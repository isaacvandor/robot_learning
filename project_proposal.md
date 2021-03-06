## List the team members
Nina Tchirkova and Isaac Vandor

## In 4-5 sentences, what is the big idea of your project?

Our goal is to have a program that recognizes a certain individual talking and then has the robot move toward that person. Ideally, we will have the robot "listening" for one of our voices, and ignoring everyone elses as well as other noises. We will train the robot using a data set of other voices and noises, as well as our voices.
## Have you found any papers or blog posts that have done something similar to what you are proposing?
[How to Do Speech Recognition with Deep Learning](https://medium.com/@ageitgey/machine-learning-is-fun-part-6-how-to-do-speech-recognition-with-deep-learning-28293c162f7a)

[Mozilla Machine Learning Using Voice](https://research.mozilla.org/machine-learning/)

[Microsoft: Deep Learning for Speech/Language Processing](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/interspeech-tutorial-2015-lideng-sept6a.pdf)

[Audio Recognition with Tensorflow](https://www.tensorflow.org/tutorials/sequences/audio_recognition)

[Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech)

[Voice Recognition Tech Using Neural Nets](https://www.researchgate.net/publication/279448703_Voice_Recognition_Technology_Using_Neural_Networks)

[Speech Recognition for Robot Control](http://www8.cs.umu.se/education/examina/Rapporter/ShafkatKibria.pdf)

[Connectionist Temporal Classification](http://www.cs.toronto.edu/~graves/icml_2006.pdf)

[CMUSphinx](https://cmusphinx.github.io/)

## In terms of the system that you will have running on the robot, what is your MVP?  What is your stretch goal?
The MVP is for the robot to recognize one voice and ignore all other noise and then move toward that voice. A stretch goal would be to incorporate multiple voices that are acceptable, or have the robot listen to commands from the good voice.

## Describe your learning orientation (top-down versus bottom-up) and why you have chosen it.  In particular if you choose bottom-up, make sure you specify what this will mean (e.g., which algorithms will you implement, will you eventually switch to a standard toolkit, etc.).
For this project, we will use a top-down approach as we intent to apply known frameworks for machine learning to the problem of robot movement based on voice recognition. We feel like this approach is best since it allows us to leverage existing datasets and frameworks (see Blog Posts/Papers section above) in order to get a jump-start on the integration and robot control aspects that make this project interesting.

## What is your data collection plan?  How do you plan to get the data needed for your project?  How much data do you think you'll need?  Are there existing datasets you can leverage?
To start, we will make use of the [Speech Commands Dataset](https://arxiv.org/abs/1804.03209), which includes over 105,000 WAVE audio files of people saying 30 different words. If we need more data than that, we can collect our own voices or continue to leverage existing datasets like [Mozilla's Common Voice](https://www.kaggle.com/mozillaorg/common-voice) and others.

## What sorts of learning algorithms will you apply?  You could choose these based on what you think will work the best or what you want to learn about the most.
There are a number of learning algorithms that can be used for voice recognition on the Neatos. One of the strategies we could try is PCA while another option is to create a convolutional neural network and feed new voice clips into it to do the recognition component. One of the early explorations of this project will be testing out the vartious learning algorithms possible for this and moving forward with the one that produces the best results.

## What non-learning baseline algorithm will you compare to?
While there is not necessarily an algorithm for voice recognition, one of the most common approaches used prior to the use of deep learning techniques was template matching. Essentially, a set of audio clips is stored and then a second set is matched against all of the clips in the first set until a match is found. We can evaluate the successes and drawbacks of our own implementations by comparing the run time and the accuracy of the template matching with our deep learning approach.
