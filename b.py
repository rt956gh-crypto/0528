@app.route('/ask', methods=['GET', 'POST'])

def ask():

if request.method == "POST":

user_prompt = request.form.get('prompt', '')

if not user_prompt:

return "請輸入內容", 400

try:

response = client.models.generate_content(

model='gemini-3.5-flash',

contents=user_prompt,

)

return response.text

except Exception as e:

return f"發生錯誤: {str(e)}", 500

else:

# 當使用者直接打開網頁 (GET) 時，顯示輸入框畫面

return render_template("ask.html")

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

info = req["queryResult"]["queryText"]

return make_response(jsonify({"fulfillmentText": info}))
