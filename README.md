# Language Analyzer

### Summary
---
A language analyzer that analyzes 2016 presidential nominees' tweets from Twitter.
This program is intended to analyze a sentence, in our specific case tweets, for sentiment, behavior, and domain.

Sentiment: The sentence gets scanned for the positive, neutral, or negative keywords then produces a value based on the amount of matches found.

Behavior Predictor: The behavior of the sentence can be predicted to see if it fits into the categories of Dictator, Hippie, Blame, Childish, Mockery, Pandering, Supportive, Promises, and Patriotic.

Domain: The sentence is evaluated to see if it fits into the domain of Healthcare, War, Climate, and Political Correctness.

### Example
---
![Light Example](/readme_images/light_example.png)

### Motivation
---

The motivation behind this project is to scan the presidential tweets and help citizens make a more conscious and informed decision for the Fall 2016 election.

### Installation
---
If you're on Mac OS X, consider installing with Homebrew. the link would be  -> https://github.com/yyuu/pyenv#homebrew-on-mac-os-x     , Run the comman python --version from your command line , we recommend Python 3.3.6

If you do not have pyenv use this [link][https://github.com/yyuu/pyenv#homebrew-on-mac-os-x] to install.

### Test the code
---
To run a test file type python to start the python interpreter then the test file name you want to run. Here’s an example of running the behavior_predictor test file: ➜  language-analyzer-lazer-powered-cthulhu git:(kb-readme) python test_behavior_predictor.py -v

### Contributors
---

### License
---
MIT
