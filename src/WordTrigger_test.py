import feedparser
import string
import time
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

class NewsStory():
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def getGuid(self):
        return self.guid

    def getTitle(self):
        return self.title

    def getSubject(self):
        return self.subject

    def getSummary(self):
        return self.summary

    def getLink(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, text):
        text = str(text).split(" ")
        for word in text:
            if "'s" not in word:
                text[text.index(word)] = word.translate(None, string.punctuation)
            else:
                text[text.index(word)] = word.strip("'s")
        for word in text:
            text[text.index(word)] = word.lower()
        return str(self.word) in text or str(self.word) + "'s'" in text
# TODO: TitleTrigger

class TitleTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word.lower())

    def evaluate(self, story):
        return WordTrigger.isWordIn(self, story.getTitle())


class SubjectTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word.lower())

    def evaluate(self, story):
        return WordTrigger.isWordIn(self, story.getSubject())


class SummaryTrigger(WordTrigger):
    def __init__(self, word):
        WordTrigger.__init__(self, word.lower())

    def evaluate(self, story):
        return WordTrigger.isWordIn(self, story.getSummary())



class NotTrigger():
    def __init__(self, T):
        self.T = T

    def evaluate(self, x):
        return not (self.T).evaluate(x)


class AndTrigger():
    def __init__(self, T, T2):
        self.T = T
        self.T2 = T2

    def evaluate(self, x):
        return self.T.evaluate(x) and self.T2.evaluate(x)


class OrTrigger():
    def __init__(self, T, T2):
        self.T = T
        self.T2 = T2

    def evaluate(self, x):
        return self.T.evaluate(x) or self.T2.evaluate(x)


# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        story_summary = story.getSummary()
        story_subject = story.getSubject()
        story_title = story.getTitle()
        text = self.phrase.split(" ")
        for word in text:
            text[text.index(word)] = word.translate(None, string.punctuation)
        in_summary = True
        in_title = True
        in_subject = True
        for word in text:
            if word not in story_summary:
                in_summary = False
        for word in text:
            if word not in story_title:
                in_title = False
        for word in text:
            if word not in story_subject:
                in_subject = False
        print text
        return (in_summary or in_title or in_subject) == True

phrase = PhraseTrigger("New York City")
a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
print phrase.evaluate(a)
