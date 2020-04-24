import sys
import os
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_PATH = PROJECT_PATH + '/app/'
CHATBOT_PATH = PROJECT_PATH + '/chatbot/'
sys.path.insert(0, APP_PATH)
sys.path.insert(0, CHATBOT_PATH)
