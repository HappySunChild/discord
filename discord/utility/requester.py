from requests import Session

class Requester:
	def __init__(self, token: str) -> None:
		self.session = Session()
		
		self.set_header('Authorization', token)
	
	def set_header(self, header: str, value: str):
		self.session.headers[header] = value
	
	def request(self, url: str, method: str = 'GET', json: dict = None, params: dict = None):
		response = self.session.request(method=method, url=url, params=params, json=json)
		
		return response.json(), response
	
	def patch(self, url: str, params: dict = None):
		return self.request(url=url, method='PATCH', params=params)
	
	def post(self, url: str, json: dict = None):
		return self.request(url=url, method='POST', json=json)
	
	def get(self, url: str, params: dict = None):
		return self.request(url=url, method='GET', params=params)