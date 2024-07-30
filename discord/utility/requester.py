from requests import Session

class Requester:
	def __init__(self, token: str = None) -> None:
		self.session = Session()
		
		if token:
			self.set_header('Authorization', token)
	
	def process_url(self, url: str) -> str:
		return url
	
	
	def set_header(self, header: str, value: str):
		self.session.headers[header] = value
	
	def request(self, url: str, method: str = 'GET', json: dict = None, params: dict = None):
		new_url = self.process_url(url=url)
		
		response = self.session.request(method=method, url=new_url, params=params, json=json)
		
		json_data = None
		
		try:
			json_data = response.json()
		except:
			json_data = {}
		
		return json_data, response
	
	def delete(self, url: str, params: dict = None):
		return self.request(url=url, method='DELETE', params=params)
	
	def patch(self, url: str, json: dict = None, params: dict = None):
		return self.request(url=url, method='PATCH', json=json, params=params)
	
	def post(self, url: str, json: dict = None, params: dict = None):
		return self.request(url=url, method='POST', json=json, params=params)
	
	def get(self, url: str, params: dict = None):
		return self.request(url=url, method='GET', params=params)