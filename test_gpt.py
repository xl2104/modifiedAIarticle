import openai
# from openai import OpenAI

# Your OpenAI API Key
# client = OpenAI()
# client.api_key = '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'


openai.api_key = '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'
#  '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'


# Function to summarize the article in layman terms


# Function to summarize the article in layman terms
def sum_article(text):

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
        messages=[
            # {"role": "system", "content": "You are a helpful assistant that simplifies medical articles into easy-to-understand language for non-medical users."},
            {"role": "user",
             "content": f"Summarize the following medical article in simple terms:\n\n{text}"
             }
        ],
        max_tokens=300,  # Limit to a short summary
        temperature=0.5  # Controls creativity; lower is more factual
    )

# Function to summarize the article in layman terms


def sum_chi_article(text):

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
        messages=[
            # {"role": "system", "content": "You are a helpful assistant that simplifies medical articles into easy-to-understand language for non-medical users."},
            {"role": "user",
             #  "content": f"explain the following medical report in Chinese to a layman, explain all the jargons so that none-professional people would understand:\n\n{text}"
             "content": f"请对以下报告进行解释，尤其里面的术语和检查单位，请给到正常范围和目前检查结果的临床意义。 请用通俗易懂的文字表述: \n\n{text}"
             }
        ],
        max_tokens=300,  # Limit to a short summary
        temperature=0.4  # Controls creativity; lower is more factual
    )

# # Extracting the summarized contents

    summary = response.choices[0].message.content.strip()
    return summary
# #
#  # Correct way to extract the message content
#     summary = response['choices'][0]['message']['content'].strip()
#     return summary


# Example article
article_text = """
Diabetes mellitus is a group of metabolic disorders characterized by a chronic hyperglycemic condition resulting from deficiencies in insulin secretion or action. Chronic hyperglycemia is associated with long-term damage, dysfunction, and failure of various organs, including the eyes, kidneys, nerves, heart, and blood vessels.
Treatment involves lifestyle modifications and pharmacological interventions, such as insulin therapy, to maintain normoglycemia and prevent complications.
"""

chinese_text = """
海马体积【MTA评分]
    影像所见:
    全脑萎缩[GCA评分]: 1分脑室系统未见确切扩张。
    海马体积MTA评分: 左侧海马1分，右侧海马1分，双侧海马和岛叶信号未见确切异常。脑微出血: 无。
    颅内未见确切皮层表面铁沉积。
    白质高信号【Fazekas评分]: 脑室周围白质1分，深部白质1分。脑血流灌注未见确切特异性改变。总结意见:
    脑萎缩: 脑白质高信号，Fazekas1级。
"""

# Get summary
summary = sum_chi_article(chinese_text)
print("输入文字，开始智能解读... ...")


def trans_summary(article):

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
        messages=[
            # {"role": "system", "content": "You are a helpful assistant that simplifies medical articles into easy-to-understand language for non-medical users."},
            {"role": "user",
             "content": f"Translate the following summary of a  medical article into Mandarin Chinese:\n\n{article}"
             }
        ],
        max_tokens=300,  # Limit to a short summary
        temperature=0.5  # Controls creativity; lower is more factual
    )

# # Extracting the summarized contents

    translated = response.choices[0].message.content.strip()
    return translated
