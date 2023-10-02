import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import PyPDF2 
import pandas as pd
import re
from collections import Counter
import math
import random
import numpy as np

# Downloads all the pdfs into a directory
def download_pdfs():
    website_url = "https://proceedings.mlr.press/v202/"
    response = requests.get(website_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        if not os.path.exists("pdfs"):
            os.makedirs("pdfs")

        # Find all the links
        links = soup.find_all('a', href=True)
        for link in links:
            href = link.get('href')
            if href.endswith('.pdf'):
                pdf_url = urljoin(website_url, href)
                filename = os.path.join("pdfs", os.path.basename(pdf_url))

                pdf_response = requests.get(pdf_url)
                if pdf_response.status_code == 200:
                    with open(filename, 'wb') as pdf_file:
                        pdf_file.write(pdf_response.content)

# Extracts text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        # Go through all the pages
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

# Creates a frequency table based on the file given, if no file is given creates for all the files
def create_freq_table(file_name = None):
    pdf_directory = "pdfs"
    pdf_texts = []

    # Option 1
    if(file_name):
        pdf_path = os.path.join(pdf_directory, file_name)
        text = extract_text_from_pdf(pdf_path)
        pdf_texts.append(text)
    # Option 2: Go through all the PDFs
    else:
        for file in os.listdir(pdf_directory):
            pdf_path = os.path.join(pdf_directory, file)
            text = extract_text_from_pdf(pdf_path)
            pdf_texts.append(text)
    
    # Combine all the text into a string
    combined_text = " ".join(pdf_texts)
    # Pick words
    words = re.findall(r"[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+", combined_text.lower())
    word_freq = pd.Series(Counter(words))
    return word_freq

"""
What are the top 10 common words in the ICML papers?
"""
def f1():
    freq_table = create_freq_table()
    most_common = freq_table.nlargest(10)
    print(most_common)

"""
Let Z be a randomly selected word in a randomly selected ICML paper. Estimate the entropy
of Z.
"""
def f2():
    # Select a random file
    file = random.choice(os.listdir("pdfs"))
    # Create series specific to the file
    freq_table = create_freq_table(file)
    # Select a random word
    num = random.randint(0, freq_table.size - 1)
    word = freq_table.index[num]
    freq_of_word = freq_table[word]
    total_freq = freq_table.sum()
    prob_of_word = freq_of_word / total_freq
    entropy = -(prob_of_word * math.log(prob_of_word, 2) + (1 - prob_of_word) * math.log(1 - prob_of_word, 2))
    print(f"The estimated entropy for the word {word} in file {file} is {entropy}")

"""
Synthesize a random paragraph using the marginal distribution over words.
"""
def f3():
    freq_table = create_freq_table()
    probs = freq_table.values / freq_table.sum()
    paragraph = ""
    # Sample 250 words (about a paragraph)
    for i in range(0, 250):
        word = np.random.choice(freq_table.index, p=probs)
        if(i == 0):
            word = word.capitalize() + " "
        elif(i == 249):
            word = word + "."
        else:
            word = word + " "
        paragraph += word
    print(paragraph)

# download_pdfs()
f1()
f2()
f3()



