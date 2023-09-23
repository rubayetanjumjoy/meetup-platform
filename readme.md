# Meetup Platform

## Table of Contents

1. [Overview](#overview)
2. [Access Credentials](#access-credentials)
3. [Configuration](#configuration)
4. [Features](#features)
5. [Getting Started](#getting-started)
6. [API Endpoints](#api-endpoints)

---

## Overview

Meetup Platform is a web application designed to manage venues and events. It is integrated with Eventbrite via API to publish events.

---

## Access Credentials

- **Admin Panel**: 
  - **Username**: admin
  - **Password**: admin

---

## Configuration


To change the Eventbrite account, update the `.env` file with the following variables.
default value `ORGANIZATION_ID` and `SECRET_KEY` is given for the assignment purpose


---

## Features

### Admin Panel

- **Description**: A Django admin panel for managing users, venues, and events.
- **How to Access**: Navigate to `{base_url}/admin` and log in with the provided credentials.

#### Sub-Features

- **CRUD Operations for Events and Venues**: Create, Read, Update, and Delete events and venues.
- **Eventbrite Integration**: Events are automatically published to Eventbrite via API.
- **Admin Portal for Event Management**: A specialized portal within the admin panel for comprehensive event management.

### Web Application

- **Description**: A user-facing web application to display events.
- **How to Access**: Navigate to `{base_url}/web`.

#### Sub-Features

- **Event Listing**: View a list of all events on the landing page.
- **Event Search**: Use the search bar to find specific events.
- **Event Details**: Click on an event card to view detailed information, including:
  - **Venue Information**: Each event displays the venue name along with its latitude and longitude.
  - **Event Link**: A dedicated link for users to access each event.
  - **Map Integration**: Maps displaying the venue's location are available on the event details page.
  - **Event Timing**: The start and end dates for the event.
  - **Ticket Pricing**: Information on the ticket price for the event.



## Getting Started

### Prerequisites

- Python 3.x
- Django
- Virtualenv
- Docker and Docker Compose (Optional)

### Installation

#### Without Docker

1. **Clone the repo and navigate to the directory:**
    ```bash
    git clone https://github.com/rubayetanjumjoy/meetup-platform.git && cd meetup-platform
    ```

2. **Set up a virtual environment and activate it:**
    ```bash
    virtualenv venv && source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

#### With Docker

1. **Clone the repo and navigate to the directory:**
    ```bash
    git clone https://github.com/yourusername/meetup-platform.git && cd meetup-platform
    ```

2. **Run Docker Compose:**
    ```bash
    docker-compose up
    ```
---

## API Endpoints

### Authentication

- **Obtain Token**
  - **Endpoint**: `http://127.0.0.1:8000/api/token/`
  
- **Refresh Token**
  - **Endpoint**: `http://127.0.0.1:8000/api/token/refresh/`

### Events

- **Event Details**
  - **Endpoint**: `http://127.0.0.1:8000/api/events/{event_id}/`
  - **Description**: Get detailed information about a specific event.

- **Events List**
  - **Endpoint**: `http://127.0.0.1:8000/api/events/`
  - **Description**: Retrieve a list of events.
  - **Search by Events**: Append `?name` to the endpoint URL.
  - **Ordering Events**: Use the `ordering` parameter to sort events.
    - **Example**: To order by ticket price, use `?ordering=ticket_price`.

### Venues

- **Venues List**
  - **Endpoint**: `http://127.0.0.1:8000/api/venues/`
  - **Description**: Retrieve a list of venues.
  - **Order by Name**: Use the `name` parameter to sort venues.
    - **Example**: To order by name, use `?name`.

- **Venue Details**
  - **Endpoint**: `http://127.0.0.1:8000/api/venues/{venue_id}/`
  - **Description**: Get detailed information about a specific venue.

## Postman Documentation

For more details on the API endpoints, you can refer to the [Postman Documentation](https://documenter.getpostman.com/view/17378834/2s9YCBvA2s?fbclid=IwAR0uTBma6jCWgiqzHT0WEwTuJ9y-1_odg3r0IQ7B8IVNEXHnrY_XvTASQeE).