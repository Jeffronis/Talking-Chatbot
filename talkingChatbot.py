from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from gtts import gTTS
import os
bot = ChatBot(
    "Math & Time Bot",
    logic_adapters=[
        #allows the chat bot to do basic math and give the user the current time
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
    ],
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter"
)
bot.set_trainer(ChatterBotCorpusTrainer)

bot.train(
    # training data for converstations humor and greetings
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
    "chatterbot.corpus.english.humor"
)
while True:
    #user input
    inputText = input("Talk to the bot...")
    #Get response to the input text
    response = bot.get_response(inputText)
    gTTSresponse = response.text
    tts = gTTS(text=gTTSresponse, lang='en')
    tts.save("Botresponse.mp3")
    #Uses the defalt media player to play audio file
    os.startfile("Botresponse.mp3")
    print(response)

    #some issues with replies not mathing what the user said
    #ex asking what movies they like can trigger the timelogic and give the time instead.
    #overall the responses with mulitple adapters need tweaking to get better responses.