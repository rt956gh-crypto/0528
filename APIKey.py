from google import genai



# 直接體驗最新一代的 3.5 Flash

response = client.models.generate_content(

model='gemini-3.5-flash',

contents='靜宜資管有甚麼特色',

)

print(response.text)
