from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

response = client.responses.create(
    model="gpt-5.5",
    input="BOAT AI LAB 起動テスト成功！"
)

print(response.output_text)
