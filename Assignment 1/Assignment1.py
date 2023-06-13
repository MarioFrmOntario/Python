
import string

"""
functionally this code grabs the sample.txt file, runs through all possible words on the file without any punctuation and returns a count of each unique word.
the code then takes that count and returns a report of each unique word in descending order.

Mario Spina
Student ID: 200187077

"""

# Define the name of the input and output files
samplefile = "sample.txt"
reportfile = "report.txt"

#function to count the words in a file
def counting_words(samplefile): 
    # Open the file in read mode
    with open(samplefile, "r") as file:
        # Convert the text in the file to lowercase and split it into separate words
        text = file.read().lower().split()

    # Initialize an empty dictionary to store the word counts
    wordcount = {}

    # Loop over each word in the text
    for words in text:
        
        # Remove punctuation from words. There seemed to be a couple of variations on how to tackle the counting without picking up punctuation. This one seemed the most straightforward and clean way to deal with the issue.
        # used https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string as a means of figuring out the most efficient way

        words = words.translate(words.maketrans('', '', string.punctuation))

        # If the word is already in the dictionary, increment its count
        if words in wordcount:
            wordcount[words] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            wordcount[words] = 1

    # Return the word count dictionary
    return wordcount  

# function to write the word count to a report file
def wordreport(wordcount, reportfile):
    #  function to use as the sorting key (the word count)
    def sort_key(item):
        return item[1]

    # Sort the words in descending order by their counts from highest to lowest
    sortedwords = sorted(wordcount.items(), key=sort_key, reverse=True)

    # Find the length of the longest word, or use 0 if there are no words to stop -----ValueError: max() arg is an empty sequence---- from occuring in the argument when testing.
    wordlength = max(len(words) for words, _ in sortedwords) + 1 if sortedwords else 0

    # Open the report file in write mode
    with open(reportfile, 'w') as report_file:
        # Write the header to the report file
        header = '{:<{}}\tFrequency\n'.format('Word', wordlength)
        report_file.write(header)

        # Loop over each word and its count
        for word, count in sortedwords:
            # Write the word and its count to the report file while making it look clean 
            report_file.write('{:<{}} |\t{:<2d}\n'.format(word, wordlength, count))

# Count the words in the sample file
wordcount = counting_words(samplefile)

# Write the word count to the report file
wordreport(wordcount, reportfile)
