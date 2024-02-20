# import json
# with open("basic_info.json", 'r') as file:
#    data = json.load(file)
#
# print(data, type(data))

from database import Db

obj = Db()
print(obj.total_count())
obj.close_connection()
