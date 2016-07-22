
from all_messages import *
from message_tokenizer import *
from domain_identifier import *
from behavior_predictor import *
from sentiment_identifier import *



def execute_analyzer():
  ''' This will import the tweets and tokenize them in multiple ways.

        1. Turn the message to all lowercase in the form of a list
        2. Turn the string into an alphanumeric list
        3. Split the message on spaces
        4. Strip the message of all punctuation
        5. Runs the message through the healthcare key domain for matches
        6. Runs the message through the war key domain for matches
        7. Runs the message through the climate change domain for matches

        '''

  for dicts in twitter_feeds:

    tokenizer = Tokenizer(dicts['tweet'])

    lowercase_message = tokenizer.lowercase()
    # print(lowercase_message)

    alpha_the_message = tokenizer.alphanumeric()
    # print(alpha_the_message)

    split_the_message = tokenizer.split_message()
    # print(split_the_message)

    strip_the_punctuation_of_message = tokenizer.stripped_message()
    # print(strip_the_punctuation_of_message)

    word_count_of_message = tokenizer.word_count()
    print(word_count_of_message)

    word_position_of_message = tokenizer.word_position()
    print(word_position_of_message)

    sentence_count_of_message = tokenizer.sentence_count()
    print(sentence_count_of_message)

    punctuation_of_message = tokenizer.punctuation()
    print(punctuation_of_message)



  # ------------------------- DOMAIN ----------------------------------------

    domain = Domain_Identifier(strip_the_punctuation_of_message)

    healthcare_domain = domain.check_healthcare()
    print(healthcare_domain)

    war_domain = domain.check_war()
    print(war_domain)

    climate_change_domain = domain.check_climate_change()
    print(climate_change_domain)



  # ------------------------- SENTIMENT --------------------------------------

    sentiment = Sentiment_Identifier(strip_the_punctuation_of_message)

    positive_sentiment = sentiment.check_positive()
    print(positive_sentiment)

    negative_sentiment = sentiment.check_negative()
    print(negative_sentiment)

    neutral_sentiment = sentiment.check_neutral()
    print(neutral_sentiment)


  # ------------------------- BEHAVIOR ---------------------------------------

    # behavior = Behavior_Predictor(strip_the_punctuation_of_message)

    # dictator_behavior = behavior.check_dictator()
    # print(dictator_behavior)

    # hippie_behavior = behavior.check_hippie()
    # print(hippie_behavior)

    # blame_behavior = behavior.check_blame()
    # print(blame_behavior)

    # childish_behavior = behavior.check_childish()
    # print(childish_behavior)

    # mockery_behavior = behavior.check_mockery()
    # print(mockery_behavior)

    # pandering_behavior = behavior.check_pandering()
    # print(pandering_behavior)

    # supportive_behavior = behavior.check_supportive()
    # print(supportive_behavior)

    # promises_behavior = behavior.check_promises()
    # print(promises_behavior)

    # patriotic_behavior = behavior.check_patriotic()
    # print(patriotic_behavior)




  # return (lowercase_message, alpha_the_message, split_the_message, strip_the_punctuation_of_message, word_count_of_message, word_position_of_message, word_position_of_message, punctuation_of_message)
    # return (lowercase_message, alpha_the_message, split_the_message, strip_the_punctuation_of_message)

execute_analyzer()
