from google.genai import types
from google import genai

# 1. 帶入金鑰建立 Client 物件


client = genai.Client(api_key=api_key)

# 2. 建立對話（指定最新的模型，這裡以最新的 gemini-3.5-flash 為例）

chat = client.chats.create(model='gemini-3.5-flash')

# 3. 發送第一輪問題

response1 = chat.send_message('靜宜資管有什麼特色')

print("--- 第一輪回應 ---")

print(response1.text)

# 4. 發送第二輪問題（模型會自動記得前面的對話脈絡）

response2 = chat.send_message('可否提供該科系相關的笑話')

print("\n--- 第二輪回應 ---")

print(response2.text)           



# 在全域（函式外面）建立 Client 物件，只初始化一次即可，不用每次初始化


app = Flask(__name__)

@app.route("/AI")

def AI():

# 每次使用者拜訪該路徑時，直接使用全域的 client 呼叫模型

response = client.models.generate_content(

model='gemini-3.5-flash',

contents='我想查詢靜宜大學資管系的評價？',

)

# 回傳生成的文字

return response.text

@app.route("/webhook7", methods=["POST"])

def webhook7():

# build a request object

req = request.get_json(force=True)

# fetch queryResult from json

action = req.get("queryResult").get("action")

#msg = req.get("queryResult").get("queryText")

#info = "動作：" + action + "； 查詢內容：" + msg

if (action == "rateChoice"):

…

elif (action == "input.unknown"):

instruction_text = (

"你是一個熱心且知識豐富的專業智慧助理。"

"對於使用者的提問，請回覆重點的關鍵字，不要重述問題。"

)

ai_config = types.GenerateContentConfig(

max_output_tokens=500,

system_instruction=instruction_text

)
response = client.models.generate_content(

model='gemini-3.5-flash',

contents=req["queryResult"]["queryText"],

config=ai_config,

)

if response.text:

info = response.text

else:

info = "抱歉，我現在無法生成回應，請稍後再試。"

return make_response(jsonify({"fulfillmentText": info}))
