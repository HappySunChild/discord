from ...enums import EmbedType

class Embed:
	def __init__(self, title: str, description: str = None, type: EmbedType = EmbedType.Rich, **kwargs) -> None:
		self.title = title
		self.description = description
		self.type = type
		self.color = kwargs.get('color')
		
		self.url = kwargs.get('url')
		self.footer = kwargs.get('footer')
		self.author = kwargs.get('author')
		self.image = None
		
		self.fields = []
	
	def add_field(self, name: str, value: str, inline: bool = True):
		self.fields.append({'name': name, 'value': str(value), 'inline': inline})
	
	
	def set_title(self, title: str):
		self.title = title
	
	def set_description(self, desc: str):
		self.description = desc
	
	def set_color(self, color: int):
		self.color = color
	
	def set_url(self, url: str):
		self.url = url
	
	
	def set_image(self, url: str):
		self.image = {'url': url}
	
	def set_footer(self, text: str):
		self.footer = {'text': text}
	
	def set_author(self, name: str):
		self.author = {'name': name}
	
	def _get_data(self):
		data = {
			'url': self.url,
			
			'title': self.title,
			'type': self.type.value,
			'description': self.description,
			'color': self.color,
			
			'image': self.image,
			'fields': self.fields,
			'footer': self.footer,
			'author': self.author
		}
		
		return data