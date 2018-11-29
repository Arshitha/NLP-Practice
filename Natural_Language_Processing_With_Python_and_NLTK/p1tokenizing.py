from nltk.tokenize import sent_tokenize, word_tokenize

# tokenizing - basically different types of grouping like 

# word tokenizers (grouping by words) and sentence tokenizers (grouping by sentence)

# lexicon and corporas 

# corpora - body of text. Eg: medical journals, presidential speeches or the english language
# lexicon - like a dictionary - words and their meanings

# investor speak and endglish-speak 

# investor-speak 'bull' = someone who is positive about the market
# english-speak 'bull' = scary animal

example_text = "Hello there, how are you doing today? The weather is great and Python is awesome. Sentdex is crazy."

print(sent_tokenize(example_text))
print(word_tokenize(example_text))