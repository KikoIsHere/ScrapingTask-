# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_jsonschema.item import JsonSchemaItem

class CrawlerItem(JsonSchemaItem):
	jsonschema =     {
		"$schema": "http://json-schema.org/draft-04/schema#",
		"title": "Article",
		"description": "A article",
		"type": "object",
		"properties": {
			"name": {
				"type": "string"
			},
			"price": {
				"type": "number"
			},
			"color": {
				"type": "string",
			},
			"sizes": {
				"type": "array",
			},
		},
		"required": ["name", "price", "color", "sizes"]
	}