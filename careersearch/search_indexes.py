import datetime
from haystack import indexes
from userprofile.models import Vacancy

class VacancyIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	job = indexes.CharField(model_attr='job')
	description = indexes.CharField(model_attr='description')		
	region = indexes.CharField(model_attr='region')	
	sector = indexes.CharField(model_attr='sector')			
	level = indexes.CharField(model_attr='level')			
	employment = indexes.CharField(model_attr='employment')		
	offer = indexes.CharField(model_attr='offer')			
	properties = indexes.CharField(model_attr='properties')		
	demands = indexes.CharField(model_attr='demands')			
	knowledge =	indexes.CharField(model_attr='knowledge')		
	timestamp = indexes.CharField(model_attr='timestamp')		

	def get_model(self):
		return Vacancy

	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated"""
		return self.get_model().objects.filter(timestamp__lte=datetime.datetime.now())
	
	type = indexes.CharField(model_attr='properties')