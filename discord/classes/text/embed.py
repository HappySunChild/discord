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
		self.video = None
		self.thumbnail = None
		
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
	
	
	def set_video(self, url: str, height: int = None, width: int = None):
		self.video = {
			'url': url,
			'height': height,
			'width': width
		}
	
	def set_image(self, url: str, height: int = None, width: int = None):
		self.image = {
			'url': url,
			'height': height,
			'width': width
		}
	
	def set_thumbnail(self, url: str, height: int = None, width: int = None):
		self.thumbnail = {
			'url': url,
			'height': height,
			'width': width
		}
	
	def set_footer(self, text: str, icon_url: str = None):
		self.footer = {'text': text, 'icon_url': icon_url}
	
	def set_author(self, name: str, icon_url: str = None):
		self.author = {'name': name, 'icon_url': icon_url}
	
	def _get_data(self):
		data = {
			'url': self.url,
			
			'title': self.title,
			'type': self.type.value,
			'description': self.description,
			'color': self.color,
			
			'thumbnail': self.thumbnail,
			'image': self.image,
			'fields': self.fields,
			'footer': self.footer,
			'author': self.author
		}
		
		return data