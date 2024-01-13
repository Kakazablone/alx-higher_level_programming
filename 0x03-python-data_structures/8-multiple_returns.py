#!/usr/bin/python3
def multiple_returns(sentence):
    t_sentence = (len(sentence),
                  sentence[0] if sentence else "None")
    return t_sentence
