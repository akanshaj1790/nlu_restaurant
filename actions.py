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

class ActionCuisineValidation(Action):
	def name(self):
		return 'action_cuisine_valid'
		
	def run(self, dispatcher, tracker, domain):
		list = ["chinese","mexican","american","italian","south indian","north indian"]
		cuisine = tracker.get_slot('cuisine')
		if cuisine is not None:
			if cuisine.lower() in list:
				return[SlotSet('cuisine',cuisine)]
			else:
				dispatcher.utter_message("invalid Cuisine, not in the list")
				return[SlotSet('cuisine',None)]
		else:
			dispatcher.utter_message("Please enter valid cuisine")
			return[SlotSet('cuisine', None)]			

			
class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_location'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		tier1_tier2 = ['agra','ajmer','aligarh','allahabad','amravati','amritsar','asansol','aurangabad','bareilly','belgaum','bhavnagar','bhiwandi','bhopal','bhubaneswar','bikaner','bokaro steel city','chandigarh','coimbatore','cuttack','dehradun','dhanbad','durg-bhilai nagar','durgapur','erode','faridabad','firozabad','ghaziabad','gorakhpur','gulbarga','guntur','gurgaon','guwahati‚ gwalior','hubli-dharwad','indore','jabalpur','jaipur','jalandhar','jammu','jamnagar','jamshedpur','jhansi','jodhpur','kannur','kanpur','kakinada','kochi','kottayam','kolhapur','kollam','kota','kozhikode','kurnool','lucknow','ludhiana','madurai','malappuram','mathura','goa','mangalore','meerut','moradabad','mysore','nagpur','nanded','nashik','nellore','noida','palakkad','patna','pondicherry','raipur','rajkot','rajahmundry','ranchi','rourkela','salem','sangli','siliguri','solapur','srinagar','sultanpur','surat','thiruvananthapuram','thrissur','tiruchirappalli','tirunelveli','tiruppur','ujjain','bijapur','vadodara','varanasi','vasai-virar city','vijayawada','visakhapatnam','warangal','ahmedabad','bangalore','chennai','delhi','hyderabad','kolkata','mumbai','pune']
		msg=""
		if loc in tier1_tier2:
			msg="Glad to inform we operate in this city!"
			dispatcher.utter_message("----"+msg)
			return [SlotSet('location',loc)]
		else:
			msg="We do not operate in that area yet!"
			dispatcher.utter_message("----"+msg)
			return [SlotSet('location','None')]

class ActionValidateEmail(Action):
	def name(self):
		return 'action_validate_email'
		
	def run(self, dispatcher, tracker, domain):
		pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
		tracker_email = tracker.get_slot('email')
		if tracker_email is not None:
			if re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",tracker_email):
				return[SlotSet('email',tracker_email)]
			else:
				dispatcher.utter_message("Invalid email , please validate and re-enter")
				return[SlotSet('email',None)]
		else:
			dispatcher.utter_message("Re-tpye email again !! ")
			return[SlotSet('email', None)]

			
class ActionSendEmail(Action):
	def name(self):
		return 'action_send_mail'
		
	def run(self, dispatcher, tracker, domain):
		tracker_email = tracker.get_slot('email')
		if tracker_email is not None:
			dispatcher.utter_message("Email Sent")
			return[SlotSet('email',tracker_email)]
		else:
			dispatcher.utter_message("We cannot send the details over email")
			return[SlotSet('email',None)]
			