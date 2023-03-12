import bs
from datetime import datetime
date = datetime.now().strftime('%d')

enableTop5effects = True
enableTop5commands = False
enableCoinSystem = True
powerupShield = False
enableStats = True

print 'Enable Stats: ', enableStats

spamProtection = True

coinTexts = ['swipe bomb to jumb to perform backflip']

questionDelay = 55 #60 #seconds
questionsList = {'Who is the editor of this server?': 'bluekg', 'Who is the main owner of this server??' : 'bluekg','who is the pm of india?':'modi','Do you love this server?':'yes','How many owners in this server?':'2','Do u know owners are ultra pro players of bs?':'yes',
       'add': None, 
       'multiply': None}

availableCommands = {'/nv': 50, 
   '/ooh': 5, 
   '/playSound': 10, 
   '/box': 30, 
   '/boxall': 60, 
   '/spaz': 50, 
   '/spazall': 100, 
   '/inv': 40, 
   '/invall': 80, 
   '/tex': 20, 
   '/texall': 40, 
   '/freeze': 60, 
   '/freezeall': 100, 
   '/sleep': 40, 
   '/sleepall': 80, 
   '/thaw': 50, 
   '/thawall': 70, 
   '/kill': 80, 
   '/killall': 150, 
   '/end': 100, 
   '/hug': 60, 
   '/hugall': 100, 
   '/tint': 90, 
   '/sm': 50, 
   '/fly': 50, 
   '/flyall': 100, 
   '/heal': 50, 
   '/healall': 70, 
   '/gm': 2000000000000, 
   '/custom': 250}

availableEffects = {'ice': 500, 
   'sweat': 750, 
   'scorch': 500, 
   'glow': 400, 
   'distortion': 750, 
   'slime': 500, 
   'metal': 500, 
   'surrounder': 100}
