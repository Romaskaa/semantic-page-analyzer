from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=""
)

def generate_content(topic, knowledge):

    prompt = f"""
Создай SEO статью.

Тема:
{topic}

База знаний:
{knowledge}

Требования:
- SEO оптимизация
- H1 H2 H3
- FAQ
"""

    response = client.chat.completions.create(
        model="stepfun/step-3.5-flash:free",
        messages=[
            {
                "role": "system",
                "content": "Ты SEO эксперт"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        extra_body={
            "reasoning": {"enabled": True}
        }
    )

    return response.choices[0].message.content