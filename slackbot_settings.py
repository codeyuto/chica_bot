import os
API_TOKEN=os.environ["BOT_API_TOKEN"]
# 知らない言葉を聞いた時のデフォルトの応答
DEFAULT_REPLY = "どうしたの？"
 
#外部ファイルの読み込み
PLUGINS = [
    "slackbot.plugins",
    "botmodule"
]