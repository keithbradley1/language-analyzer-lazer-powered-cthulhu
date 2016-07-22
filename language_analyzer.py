
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
    # print(word_count_of_message)

    word_position_of_message = tokenizer.word_position()
    # print(word_position_of_message)

    sentence_count_of_message = tokenizer.sentence_count()
    # print(sentence_count_of_message)

    punctuation_of_message = tokenizer.punctuation()
    # print(punctuation_of_message)


    print()
    print()
    print("Trump said, 'Our country is totally divided and our enemies are watching. We are not looking good, we are not looking smart, we are not looking tough!'")
    print()
    print()
    print(" ~ On a scale of: 1 to 5 ~ ")
    print()
    print()


  # ------------------------- DOMAIN ----------------------------------------
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DOMAIN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    domain = Domain_Identifier(strip_the_punctuation_of_message)

    healthcare_domain = domain.check_healthcare()

    print()
    print("His message contained a HEALTHCARE value of: ", healthcare_domain)

    war_domain = domain.check_war()
    print()
    print("His message contained a WAR value of: ", war_domain)

    climate_change_domain = domain.check_climate_change()
    print()
    print("His message contained a CLIMATE CHANGE value of: ", climate_change_domain)

    print()
    print("His message contained a POLITICAL CORRECTNESS value of: ", "TOO MUCH TO CALCULATE ¯\_(ツ)_/¯ ")
    print()
    print()


  # ------------------------- SENTIMENT --------------------------------------
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SENTIMENT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    sentiment = Sentiment_Identifier(strip_the_punctuation_of_message)

    positive_sentiment = sentiment.check_positive()
    print()
    print("His message contained a POSITIVE value of: ", positive_sentiment)

    negative_sentiment = sentiment.check_negative()
    print()
    print("His message contained a NEGATIVE value of: ", negative_sentiment)


    neutral_sentiment = sentiment.check_neutral()
    print()
    print("His message contained a NEUTRAL value of: ", neutral_sentiment)
    print()
    print()

  # ------------------------- BEHAVIOR ---------------------------------------
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BEHAVIOR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # behavior = Behavior_Predictor(strip_the_punctuation_of_message)

    dictator_behavior = behavior.check_dictator()
    print()
    print("His message contained a DICTATOR value of: ", dictator_behavior)


    hippie_behavior = behavior.check_hippie()
    print()
    print("His message contained a HIPPIE value of: ", hippie_behavior)


    blame_behavior = behavior.check_blame()
    print()
    print("His message contained a BLAME value of: ", blame_behavior)


    childish_behavior = behavior.check_childish()
    print()
    print("His message contained a CHILDISH value of: ", childish_behavior)


    mockery_behavior = behavior.check_mockery()
    print()
    print("His message contained a MOCKERY value of: ", mockery_behavior)


    pandering_behavior = behavior.check_pandering()
    print()
    print("His message contained a PANDERING value of: ", pandering_behavior)


    supportive_behavior = behavior.check_supportive()
    print()
    print("His message contained a SUPPORTIVE value of: ", supportive_behavior)


    promises_behavior = behavior.check_promises()
    print()
    print("His message contained a PROMISES value of: ", promises_behavior)


    patriotic_behavior = behavior.check_patriotic()
    print()
    print("His message contained a PATRIOTIC value of: ", patriotic_behavior)
    print()
    print()



  # return (lowercase_message, alpha_the_message, split_the_message, strip_the_punctuation_of_message, word_count_of_message, word_position_of_message, word_position_of_message, punctuation_of_message)
    # return (lowercase_message, alpha_the_message, split_the_message, strip_the_punctuation_of_message)

execute_analyzer()
