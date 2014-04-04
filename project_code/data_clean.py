import pandas as pd
import json
from urlparse import urlparse, parse_qsl
import re


def expand_column_response_body(data):
	'''
	Create all-inclusive columns within response_body keys, cpc, cpm
	Input:
		data: dataframe
	Output:
		data: dataframe with additional columns
	'''
	##--parse dataframe
	body = data['response_body'].apply(json.loads)
	##--generate key list
	key_list = []
	for index in list(body.keys()):
		key_list += body[index].keys()
	key_list = set(key_list)
	#--expand columns
	for i in key_list:
		data[i] = body.map(lambda x: x.get(i, None))
	return data


def get_html_device_model(data, mobil_list = ['iPhone', 'Linux', 'iPod', 'iPad', 'PlayBook', 'BlackBerry']):
	'''
	expand column from html and get device model
	Input:
		data: dataframe
	Output:
		data: dataframe with device columns
	'''
	html_parse = data.html.apply(urlparse)
    f = lambda x: dict(parse_qsl(x[4])).get(html_keys, None)
	for html_keys in dict(parse_qsl(html_parse.iloc[0][4])).keys():
    	data[html_keys] = html_parse.map(f)
    def f(x):
    	if not x:
        	return None
    	if x == "Android":
        	return x
    return re.findall(r"[^\W]+", (x.split(' ')[1]))
	data['device_model'] = data.ua.map(f)
	def g(x):
    	try:
        	x = x[0]
    	except:
        	pass
    return x
	data.device_model = data.device_model.map(g)
	data = data[data.device_model.isin(mobil_list)]
	return data



if __name__ == "__main__":
	##--load data
	data_ejam = pd.read_csv('eJam.txt', sep = '\t', na_values=["nan"], names = ['network', 'app_id', 'adunit_id', \
		'country', 'udid', 'req_id', 'timestamp', 'sdk_version', 'os_version', 'carrier', 'request_url', \
		'response_code', 'response_body', 'is_valid_ad'])
	##--remove unuseful rows
	data_ejam = data_ejam[data_ejam.response_body != '{"error":"No available creatives"}']
	data_ejam = data_ejam[data_ejam.response_body != '{""}']
	data_ejam = data_ejam[data_ejam.response_body.notnull()]
	#--expand timestamp from epoch to dayofweek and hour
	data_ejam.timestamp=pd.to_datetime((data_ejam['timestamp']).astype(int),unit='s')
	data_ejam['dayofweek'] = data_ejam.timestamp.map(lambda x: x.dayofweek)
	data_ejam['hour'] = data_ejam.timestamp.apply(lambda x: x.hour)
	##--parse columns
	data_ejam = expand_column_response_body(data_ejam)
	data_ejam = get_html_device_model(data_ejam)

