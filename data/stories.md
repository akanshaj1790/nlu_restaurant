## Generated Story 255706069223404498
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- action_cuisine_valid
	- utter_ask_pricerange
* restaurant_search{"price": "1"}
	- slot {"price" : "1"}
    - action_restaurant
	- utter_ask_mail
    - slot{"location": "delhi"}
    - utter_goodbye
    - export

## Generated Story 1993277579540566202
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- action_cuisine_valid
	- utter_ask_pricerange
* restaurant_search{"price": "3"}
	- slot {"price" : "3"}
    - action_restaurant
	- utter_ask_mail
    - utter_goodbye

## Generated Story 3320800183399695936
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- action_check_location
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- action_cuisine_valid
	- utter_ask_pricerange
* restaurant_search{"price": "2"}
	- slot {"price" : "2"}
    - action_restaurant
	- utter_ask_mail
* goodbye
    - utter_goodbye

## Generated Story -4639179087166749998
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- action_cuisine_valid
    - action_restaurant
	- utter_ask_mail
    - slot{"location": "delhi"}
    - export


## Generated Story 4963448062290237512
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
	- action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- action_cuisine_valid
	- utter_ask_pricerange
	- slot{"price":"1"}
* restaurant_search{"price": "3"}
	- slot {"price" : "3"}
    - action_restaurant
	- utter_ask_mail
* affirm
    - utter_goodbye
    - export

	
## Generated Story 3549012137537341774
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "pune" , "price": "1"}
	- action_check_location
    - slot{"cuisine": "mexican"}
    - slot{"location": "pune"}
	- slot{"price": "1"}
    - action_restaurant
    - slot{"location": "pune"}
    - export
## Generated Story -6232213065080115956
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - slot{"location": "mumbai"}
	- action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- action_cuisine_valid
    - utter_ask_pricerange
	- slot{"price":"3"}
* restaurant_search
    - action_restaurant
	- utter_ask_mail
    - slot{"location": null}
* affirm
    - utter_goodbye
    - export

## Generated Story -6232213065080115956
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- action_cuisine_valid
    - utter_ask_pricerange
	- slot{"price":"1"}
* restaurant_search
    - action_restaurant
	- utter_ask_mail
    - slot{"location": null}
* affirm
    - utter_goodbye
    - export

## Generated Story -5615955838050432678
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - action_cuisine_valid
    - slot{"cuisine": "chinese"}
    - utter_ask_pricerange 
* restaurant_search{"price" :"2" }
	- slot{"price":"2"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_mail
* restaurant_search
    - utter_goodbye
    - export

## Generated Story 6218935663485729965
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - action_check_location
    - slot{"location": "None"}
    - utter_ask_cuisine
* restaurant_search{"location": "mexican"}
    - slot{"location": "mexican"}
    - action_cuisine_valid
    - slot{"cuisine": null}
    - utter_ask_pricerange
* restaurant_search{"price":"3"}
	- slot{"price":"3"}
    - action_restaurant
    - utter_ask_mail
	- slot{"email":"akansha@gmailcom"}
	- action_send_mail
* restaurant_search
    - utter_goodbye
    - export

## Generated Story -8477124718590771868
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search
    - action_cuisine_valid
    - slot{"cuisine": null}
    - utter_ask_pricerange
* restaurant_search
    - action_restaurant
    - utter_ask_mail
* affirm
    - action_send_mail
    - slot{"email": null}
    - utter_goodbye
    - export

## Generated Story 3327178249186022696
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search
    - action_check_location
    - slot{"location": "None"}
    - action_cuisine_valid
    - slot{"cuisine": "chinese"}
    - utter_ask_pricerange
* restaurant_search
    - action_restaurant
    - slot{"location": "None"}
    - utter_ask_mail
* affirm
    - action_send_mail
    - slot{"email": null}
    - utter_goodbye
* restaurant_search
    - export

