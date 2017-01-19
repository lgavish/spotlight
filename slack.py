from slackclient import SlackClient
import configparser

# Load configs
# To retrieve value: print(c['variable'])
config = configparser.ConfigParser()
config.sections()
config.read('/etc/spotlight/spotlight.cfg')
c = config['spotlight']

slack_token = c['slack_token']
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postMessage",
  channel=c['channel'],
  text=c['text']
)
