from datetime import datetime

def driverPath():
	return 'C:\\code\\selenium\\driver\\chromedriver.exe'

def baseUrl():
	return "http://10.161.93.66/"

def getCurrentTime():
	format = "%a %b %d %H:%M:%S %Y"
	return datetime.now().strftime(format)

def timeDiff(starttime, endtime):
	format = "%a %b %d %H:%M:%S %Y"
	return datetime.strptime(endtime, format) - datetime.strptime(starttime, format)


class TestCaseInfo(object):  
    """description of class"""  
    def __init__(self, id="",name="",owner="",result="Failed",starttime="",endtime="",secondsDuration="",errorinfo=""):  
        self.id = id
        self.name = name
        self.owner = owner
        self.result = result
        self.starttime = starttime
        self.endtime = endtime
        self.secondsDuration = secondsDuration
        self.errorinfo = errorinfo

