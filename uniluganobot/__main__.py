from interfaces.telegram.usibot import UsiBot

try:
    UsiBot.run()
except KeyboardInterrupt:
    print('Quitting')
