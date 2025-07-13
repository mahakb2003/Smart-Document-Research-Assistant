# backend/summarizer.py
''' from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer(text[:3000], max_length=150, min_length=50, do_sample=False)[0]['summary_text']'''
from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    result = summarizer(text[:3000], max_length=150, min_length=50, do_sample=False)
    return result[0]['summary_text']

