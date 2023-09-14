import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import PyPDF2 
import pandas as pd
import re
from collections import Counter
import math

# Downloads all the pdfs into a directory
def download_pdfs():
    website_url = "https://proceedings.mlr.press/v202/"
    response = requests.get(website_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        if not os.path.exists("pdfs"):
            os.makedirs("pdfs")

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

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def create_df(file_name):
    pdf_directory = "pdfs"  # Replace with the actual directory
    pdf_texts = []

    if(file_name):
        pdf_path = os.path.join(pdf_directory, file_name)
        text = extract_text_from_pdf(pdf_path)
        pdf_texts.append(text)
    
    else:
        for file in os.listdir(pdf_directory):
                pdf_path = os.path.join(pdf_directory, file)
                text = extract_text_from_pdf(pdf_path)
                pdf_texts.append(text)

    combined_text = " ".join(pdf_texts)

    words = re.findall(r"[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+", combined_text.lower())

    word_freq = pd.Series(Counter(words))
    return word_freq

def f1():
    df = create_df()
    most_common = df.nlargest(10)
    print(most_common)

def f2(word, file):
    df = create_df(file)
    freq_of_word = df[word]
    total_freq = df.sum()
    print(total_freq)
    prob_of_word = freq_of_word / total_freq
    entropy = -(prob_of_word * math.log(prob_of_word, 2) + (1 - prob_of_word) * math.log(1 - prob_of_word, 2))
    print(entropy)

f2("of", "aamand23a.pdf")


