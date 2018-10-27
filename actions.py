from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"A92455283a69db9c0887d461c9228c52"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine').lower()
		pricerange = tracker.get_slot('price')
		price_min=0
		price_max=5000
		if (pricerange == '1'):
			price_max = 300
		else:
			if (pricerange == '2'):
				price_min = 300
				price_max = 700
			else:
				if (pricerange =='3'):
					price_min= 700
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85,'american':1,'mexican':73}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),price_min, price_max, 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ "has been rated" + restaurant['restaurant']['user_rating']['aggregate_rating'] +"\n"

		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

