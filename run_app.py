from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-465091562931-465017512964-465024487348-24c5043b6286207eed57f0cd0fccf988', #app verification token
							'xoxb-465091562931-464459251456-K3wPb0C9LU1fTXSHopTZkKYX', # bot verification token
							'5umlFTkIKkWU0fMkTbydSfvX', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))