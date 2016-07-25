# Language Analyzer

### Summary
---
This project is a language analyzer that analyzes 2016 presidential nominees' tweets. The program is intended to analyze a twitter message based on categories relating to the presidiential race. The categories used are sentiment, behavior, and domain.

Sentiment: The sentence gets scanned for the positive, neutral, or negative keywords then produces a value based on the amount of matches found.

Behavior Predictor: The behavior of the sentence can be predicted to see if it fits into the categories of Dictator, Hippie, Blame, Childish, Mockery, Pandering, Supportive, Promises, and Patriotic.

Domain: The sentence is evaluated to see if it fits into the topic of Healthcare, War, Climate, and Political Correctness.

### Example
---
![Light Example](/readme_images/light_example.png)

### Motivation
---

The motivation behind this project is to scan the presidential tweets and help citizens make a more conscious and informed decision for the Fall 2016 election.

### Installation
---
If you're on Mac OS X, consider installing with [Homebrew](https://github.com/yyuu/pyenv#homebrew-on-mac-os-x). Run the command ```$ python --version``` from your command line , we recommend Python 3.3.6

If you do not have pyenv use this [link](https://github.com/yyuu/pyenv#homebrew-on-mac-os-x) to install.

This project was built using Python 3.3, click [here](https://www.python.org/download/releases/3.3.0/) to install this version.

### Test the code
---
We implemented test driven development in this project. First we wrote a complete test suite for each of our modules. The test suite provided the framework and planning for the logic and implementation. Here is an example of passing tests used to assign values to the behvior predictor module.

![Behavior Tests Passing](/readme_images/test_file_screen_shot.png)

##### To run a test file for yourself:
Type 'python' to start the python interpreter then the test file name you want to run. Here’s an example of running the behavior_predictor test file: ➜  
``` python test_behavior_predictor.py -v ```

### Contributors
---
- [Amari Ashwood](https://github.com/ashwoodaa)
- [Keith Bradley](https://github.com/keithbradley1)
- [Carter Harris](https://github.com/carter-harris)
- [Jessica Wynn](https://github.com/Jessicashinjo)

### License
---
MIT
