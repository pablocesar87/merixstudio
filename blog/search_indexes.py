import datetime
from haystack import indexes
from .models import Entry

'''
I have implemented the whole search process but unfortunatly
it is not working due to a an Attribute error when the search
is being performed. I think the problem is with Solr and the scheme.xml
file. But for know I can not find how to solve it.Also I did not
include Solr in requirements to avoid further errors when checking
my project.
'''


class EntryIndex(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(model_attr='title')
    text = indexes.CharField(document=True, use_template=True)
    created_date = indexes.DateTimeField(model_attr='created_date')

    def get_model(self):
        return Entry

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
