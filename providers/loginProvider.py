import os

def getLoginMock():
    return (os.environ.get('MQL_LOGIN'), os.environ.get('MQL_PASSWORD'))