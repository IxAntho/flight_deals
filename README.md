# Flight Deal Finder

## Overview

This project is designed to search for flight prices and send SMS notifications if good deals are found. The main steps involved are:

1. Get a list of cities and prices from the Sheety API
2. Look up the IATA codes for each city using the Flight Search API
3. Update the Google Sheet with IATA codes using the Sheety API
4. Search flight prices for each city using the Flight Search API
5. If flight prices drop below the threshold, send an SMS notification with Twilio

## Setup

To run this project, you will need to sign up for a few APIs and configure some environment variables:

### Env Variables

Create a `.env` file with the following keys:

Add your API keys to the `.env` file:

    ```env
    SHEETY_AUTH=your_sheety_auth_token
    SHEETY_GET_ENDPOINT=your_sheety_get_endpoint
    SHEETY_POST_ENDPOINT=your_sheety_post_endpoint
    SHEETY_PUT_ENDPOINT=your_sheety_put_endpoint

    TWILIO_ACCOUNT_SID=your_twilio_account_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    PHONE_SENDER=your_twilio_phone_number
    PHONE_RECEIVER=your_receiver_phone_number
    ```

### Sheety API

Used to manage data in a Google Sheet

1. Sign up for a free account at [Sheety](https://sheety.co)
2. Create a new Sheet called "flightDeals"
3. Add columns: "city," "iataCode," "lowestPrice," "id"
4. Copy the Sheety API endpoints from your sheet into `.env`
5. Sheety authentication token also saved in `.env`

### Flight Search API

Used to search flight prices

1. Sign up at [Aviationstack](https://aviationstack.com)
2. Get an API key and add to `.env`

### Twilio API

Used to send SMS notifications

1. Create a free Twilio trial account at [Twilio](https://www.twilio.com)
2. Find your account sid and auth token in the console
3. Add to `.env` along with your Twilio phone number

## Running

1. `pip install -r requirements.txt`
2. Configure your `.env` file with all credentials
3. `python flight_search.py`
4. It will search flight prices and send SMS alerts through Twilio if any deals are found
