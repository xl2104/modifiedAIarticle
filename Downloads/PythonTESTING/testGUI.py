import tkinter as tk
from tkinter import messagebox
from test_scrape import scrape_content_and_date
from test_gpt import sum_article, trans_summary
import requests
from bs4 import BeautifulSoup
import openai


# Set your OpenAI API Key

openai.api_key = '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'

# Function to fetch and summarize the article content


def summarize_article():
    url = url_entry.get()  # Get the URL entered by the user
    if not url:
        messagebox.showerror("Error", "Please enter a URL!")
        return

    try:
        # Fetch the article content
        response = requests.get(url)
        response.raise_for_status()

        # # Parse the HTML content with BeautifulSoup using scrape_content_and_date

        article_text, date, title = scrape_content_and_date(url)

        # # Parse the HTML content with BeautifulSoup
        # soup = BeautifulSoup(response.content, 'html.parser')

        # # Extract text from the article, assuming paragraphs are in <p> tags
        # paragraphs = soup.find_all('p')
        # article_text = ' '.join([para.get_text() for para in paragraphs])

        # Call OpenAI API to summarize the article
        summary = sum_article(article_text)
        translated = trans_summary(summary)

        # prompt = f"Summarize the following article in simple language:\n\n{article_text}"
        # summary_response = openai.Completion.create(
        #     engine="gpt-3.5-turbo",  # Use GPT-4 if you have access
        #     prompt=prompt,
        #     max_tokens=300,
        #     temperature=0.5
        # )

        # summary = summary_response.choices[0].text.strip()

        # Display the summarized text in the output box
        result_text.delete(1.0, tk.END)  # Clear previous output
        result_text.insert(tk.END, summary)
        result_title.config(text=f"Title: {title}")
        result_date.config(text=f"Date: {date}")

        # display translated summary below
        translated_text.delete(1.0, tk.END)  # Clear previous output
        translated_text.insert(tk.END, translated)

    except requests.exceptions.RequestException as e:
        messagebox.showerror(
            "Error", f"Failed to retrieve article. Error: {e}")
    except openai.error.OpenAIError as e:
        messagebox.showerror("Error", f"OpenAI API error: {e}")


# Create the main application window
root = tk.Tk()
root.title("Article Summarizer")

# URL Input Label and Entry Box
url_label = tk.Label(root, text="Enter Article URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Summarize", command=summarize_article)
submit_button.pack(pady=10)

# Output for the title and date
result_title = tk.Label(root, text="Title: ")
result_title.pack(pady=10)

result_date = tk.Label(root, text="Date: ")
result_date.pack(pady=10)


# Output Text Box for displaying the summary
result_label = tk.Label(root, text="Summarized Article:")
result_label.pack(pady=10)

result_text = tk.Text(root, height=7, width=80)
result_text.pack(pady=10)

# output translated version of summary
translated_label = tk.Label(root, text="Translated Article:")
translated_label.pack(pady=10)

translated_text = tk.Text(root, height=7, width=80)
translated_text.pack(pady=10)

# Start the GUI event loop
root.mainloop()
