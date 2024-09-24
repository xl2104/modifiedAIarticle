import requests
from bs4 import BeautifulSoup

# Function to scrape content from a URL


def scrape_content(url):
    # Fetch the content from the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Initialize variables to store the article's text and word count
        word_count = 0
        content = []

        # Extract specific content from the page (for example, all paragraphs)
        # You can change this based on the page structure
        paragraphs = soup.find_all('p')
        heading = soup.find("h1").text

        # Concatenate and return the text from the paragraphss
        content = "\n\n".join([para.get_text() for para in paragraphs])
        return heading, content
    else:
        return f"Failed to retrieve content. Status code: {response.status_code}"


def scrape_content_and_date(url):
    # Fetch the content from the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Initialize variables to store the article's text and word count
        word_count = 0
        content = []

        # Find all paragraphs in the article (can be adjusted for the specific website structure)
        paragraphs = soup.find_all('p')
        heading = soup.find("h1").text

        # Iterate over the paragraphs and accumulate words
        for para in paragraphs:
            para_text = para.get_text()
            words = para_text.split()

            # Check if adding this paragraph would exceed the  word limit
            if word_count + len(words) > 400:
                # Add only enough words to reach limit
                remaining_words = 400 - word_count
                content.append(" ".join(words[:remaining_words]))
                break
            else:
                # Add the entire paragraph's text if it doesn't exceed the word limit
                content.append(para_text)
                word_count += len(words)

        # Join the list of paragraphs into a single string
        article_content = "\n\n".join(content)

        # Attempt to scrape the date of the article (adjust this based on the structure of the site)
        date = None

        # Example 1: Search for a <time> tag
        time_tag = soup.find('time')

        if time_tag and time_tag.has_attr('datetime'):
            date = time_tag['datetime']

        if time_tag:
            date = time_tag.text

        # Example 2: Search for meta tag with name='date' (if applicable)
        # if not date:
        #     meta_tag = soup.find('meta', {'name': 'date'})
        #     if meta_tag and meta_tag.has_attr('content'):
        #         date = meta_tag['content']

        # Example 3: Search for <span> or <div> with specific classes (depending on the site)
        if not date:
            # Example class name
            date_tag = soup.find('span', class_='article-date')
            if date_tag:
                date = date_tag.get_text()

        # Return the first 800 words and the extracted date
        return article_content, date, heading

    else:
        return None, None
# Example usage
# Replace with the actual URL


# url = 'https://www.frontiersin.org/journals/neuroimaging/articles/10.3389/fnimg.2023.1062493/full'
# url = 'https://www.forbes.com/sites/johnperrotto/2024/07/25/tigers-gio-urshela-sparks-effort-to-find-cure-for-rare-disease-dipg/'
url = 'https://www.sciencealert.com/world-first-13-year-old-child-cured-of-a-deadly-brain-cancer'

scraped_content, date, title = scrape_content_and_date(url)
# Output the scraped content and date
print(f"""
Title of Article: {title}

URL of the Article: {url}

Content Synoposis:\n{scraped_content}"
""")
if date:
    print(f"Date: {date}")
else:
    print("Date: not found.")


# url = 'https://www.clinicaltrialsarena.com/news/childrens-cancer-institute-brain-cancer/'
# title, scraped_content = scrape_content(url)
# print(f"""
# Title of Article: {title}

# Content:
# {scraped_content}
# """)
