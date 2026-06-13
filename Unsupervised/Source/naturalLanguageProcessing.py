##
## EPITECH PROJECT, 2026
## G-AIA-400-MPL-4-1-cvrie-2
## File description:
## naturalLanguageProcessing
##

import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer

DOMAIN_SPECIFIC_STOP_WORDS = {
    "afternoon",
    "morning",
    "day",
    "week",
    "month",
    "also",
    "almost",
    "ago",
    "along",
    "across",
    "actual",
    "afterward",
    "around",
    "away",
    "back",
    "alone",
    "always",
    "anything",
    "appear",
    "appoint",
    "appointment",
    "yesterday",
    "year",
    "weekend",
    "night",
    "sometimes",
    "often",
    "frequent",
    "frequently",
    "never",
    "recent",
    "recently",
    "bag",
    "bathroom",
    "bed",
    "birthday",
    "car",
    "chair",
    "computer",
    "desk",
    "dinner",
    "door",
    "drink",
    "eat",
    "find",
    "found",
    "go",
    "goes",
    "gone",
    "happen",
    "happened",
    "look",
    "make",
    "made",
    "play",
    "said",
    "see",
    "take",
    "taken",
    "took",
    "walk",
    "work",
    "woke",
    "wake",
    "bit",
    "cause",
    "certain",
    "could",
    "different",
    "due",
    "else",
    "even",
    "fine",
    "first",
    "little",
    "lot",
    "much",
    "one",
    "something",
    "thing",
    "think",
    "thought",
    "two",
    "use",
    "ask",
    "asking",
    "assume",
    "area",
    "avoid",
    "became",
    "become",
    "come",
    "came",
    "get",
    "got",
    "give",
    "gave",
    "keep",
    "know",
    "leave",
    "mean",
    "meet",
    "need",
    "put",
    "tell",
    "told",
    "try",
    "trying",
    "using",
    "minute",
    "hour",
    "daily",
    "early",
    "late",
    "period",
    "routine",
    "doctor",
    "friend",
    "brother",
    "daughter",
    "father",
    "mother",
    "wife",
    "partner",
    "family",
    "home",
    "house",
    "office",
    "school",
    "room",
    "can",
    "ca",
    "would",
    "should",
    "might",
    "may"
}

MEDICAL_SYNONYMS = {
    "achy": "ache",
    "aching": "ache",
    "allergic": "allergy",
    "allergies": "allergy",
    "feverish": "fever",
    "itchy": "itch",
    "nauseated": "nausea",
    "nauseous": "nausea",
    "swollen": "swell",
    "stiffen": "stiff",
    "worse": "bad",
    "worsen": "bad",
    "worst": "bad",
    "thirsty": "thirst",
    "darker": "dark",
    "deeper": "deep",
    "faster": "fast",
    "harder": "hard",
    "heavier": "heavy",
    "higher": "high",
    "lighter": "light",
    "longer": "long",
    "lower": "low",
    "paler": "pale",
    "sharper": "sharp",
    "sharply": "sharp",
    "stronger": "strong",
    "thicker": "thick",
    "weaker": "weak"
}

def _ensureNltkResources():
    # Download once
    resources = [
        "punkt",  # Tokenizer 1
        "punkt_tab", # Tokenizer 2
        "stopwords",  # Stop words list
        "wordnet",  # Lemmatization dictionary
    ]
    for resource in resources:
        nltk.download(resource, quiet=True)

def _getSpecificStopWords(customWords=None):
    stopWords = set(stopwords.words("english")).union(DOMAIN_SPECIFIC_STOP_WORDS)
    if customWords:
        stopWords = stopWords.union(set(customWords))
    return stopWords

def cleanTextNLTK(text):
    _ensureNltkResources()

    # Load stop words and initialize lemmatizer
    stopWords = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    # Lowercase
    text = text.lower()

    # Tokenize text
    words = word_tokenize(text)

    # Remove stop words and lemmatize
    cleanedWords = [
        lemmatizer.lemmatize(word)
        for word in words
        # Remove punctuation
        if word.isalpha() and word not in stopWords
    ]

    return " ".join(cleanedWords)

def cleanTextExpert(text, customWords=None):
    _ensureNltkResources()

    stemmer = SnowballStemmer("english")
    specificStopWords = _getSpecificStopWords(customWords)

    text = text.lower()
    words = word_tokenize(text)

    cleanedWords = []
    for word in words:
        if word.isalpha() and word not in specificStopWords:
            if word in MEDICAL_SYNONYMS:
                word = MEDICAL_SYNONYMS[word]

            stemmed_word = stemmer.stem(word)
            cleanedWords.append(stemmed_word)

    return " ".join(cleanedWords)

def cleanTextST(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

if __name__ == "__main__":
    print(
        cleanTextNLTK(
            "This is an example sentence, showing off the stop words filtration and lemmatization process!"
        )
    )
    print(
        cleanTextExpert(
            "This is an example sentence, showing off the stop words filtration and lemmatization process!"
        )
    )
    print(
        cleanTextST(
            "This is an example sentence, showing off the stop words filtration and lemmatization process!"
        )
    )
