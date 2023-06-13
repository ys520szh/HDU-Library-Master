import yaml
import os

class ConfigParser():
    def __init__(self, configFile):
        self.configFile = configFile
        self.config = None
        self.template = """
data:
  query_data:
    beginTime: 8
    duration: 14
    num: '196'
    space_category[category_id]: '1524'
    space_category[content_id]: '3'
planCode: [2:1524:196:8:14]
session:
  headers:
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101
      Firefox/101.0
  params:
    LAB_JSON: '1'
  trust_env: false
  verify: false
urls:
  book_seat: https://hdu.huitu.zhishulib.com/Seat/Index/bookSeats
  login: https://hdu.huitu.zhishulib.com/User/Index/login
  query_seats: https://hdu.huitu.zhishulib.com/Seat/Index/searchSeats
  query_rooms: https://hdu.huitu.zhishulib.com/Space/Category/list
  index: https://hdu.huitu.zhishulib.com/
  index: https://hdu.huitu.zhishulib.com/
user_info:
  login_name: 20081822
  org_id: '104'
  password: 20081822
plans: []
job:
  maxTrials:
  delay:
  logDetails:
  executeTime:
"""
    
    def createConfig(self):
        with open(self.configFile, 'w+', encoding="utf-8") as f:
            self.config = yaml.load(self.template, Loader=yaml.FullLoader)
            yaml.dump(self.config, f, encoding="utf-8", allow_unicode=True)
    
    def parseConfig(self):
        with open(self.configFile, 'r', encoding="utf-8") as f:
            self.config = yaml.load(f, Loader=yaml.FullLoader)
        return self.config
      
    def saveConfig(self, config):
        with open(self.configFile, 'w', encoding="utf-8") as f:
            yaml.dump(config, f, encoding="utf-8", allow_unicode=True)
    
    def delConfigFile(self):
        os.remove(self.configFile)


if __name__ == "__main__":
    config = ConfigParser("config.yaml")
    config.createConfig(config)
