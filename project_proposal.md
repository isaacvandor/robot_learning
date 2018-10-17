## List the team members
Nina Tchirkova and Isaac Vandor

## In 4-5 sentences, what is the big idea of your project?

## Have you found any papers or blog posts that have done something similar to what you are proposing?
[How to Do Speech Recognition with Deep Learning](https://medium.com/@ageitgey/machine-learning-is-fun-part-6-how-to-do-speech-recognition-with-deep-learning-28293c162f7a)

[Mozilla Machine Learning Using Voice](https://research.mozilla.org/machine-learning/)

[Microsoft: Deep Learning for Speech/Language Processing](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/interspeech-tutorial-2015-lideng-sept6a.pdf)

[Audio Recognition with Tensorflow](https://www.tensorflow.org/tutorials/sequences/audio_recognition)

[Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech)

[Voice Recognition Tech Using Neural Nets](https://www.researchgate.net/publication/279448703_Voice_Recognition_Technology_Using_Neural_Networks)

## In terms of the system that you will have running on the robot, what is your MVP?  What is your stretch goal?

## Describe your learning orientation (top-down versus bottom-up) and why you have chosen it.  In particular if you choose bottom-up, make sure you specify what this will mean (e.g., which algorithms will you implement, will you eventually switch to a standard toolkit, etc.).
For this project, we will use a top-down approach as we intent to apply known frameworks for machine learning to the problem of robot movement based on voice recognition. We feel like this approach is best since it allows us to leverage existing datasets and frameworks (see Blog Posts/Papers section above) in order to get a jump-start on the integration and robot control aspects that make this project interesting.

## What is your data collection plan?  How do you plan to get the data needed for your project?  How much data do you think you'll need?  Are there existing datasets you can leverage?
To start, we will make use of the [Speech Commands Dataset](https://arxiv.org/abs/1804.03209), which includes over 105,000 WAVE audio files of people saying 30 different words. If we need more data than that, we can collect our own voices or continue to leverage existing datasets like [Mozilla's Common Voice](https://www.kaggle.com/mozillaorg/common-voice) and others.

## What sorts of learning algorithms will you apply?  You could choose these based on what you think will work the best or what you want to learn about the most.

## What non-learning baseline algorithm will you compare to?
