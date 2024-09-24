# List Of Contents
<!-- TOC -->
* [List Of Contents](#list-of-contents)
* [Description project](#description-project)
  * [Description](#description)
    * [Task](#task)
  * [Description of input data](#description-of-input-data)
  * [CRUD of category](#CRUD-of-category)
    * [GET category](#GET-category)
    * [POST category](#POST-category)
    * [PUT category id](#PUT-category-id)
    * [DELETE category id](#DELETE-category-id)
  * [Call](#call)
    * [GET call](#GET-call)
    * [POST call](#POST-call)
  * [Requirements](#requirements)
* [Start Project](#start-project)
* [Run tests](#run-tests)
* [Note to project:](#note-to-project)
* [Description of input data](#description-of-input-data-1)
* [Test cases:](#test-cases)
  * [empty_test](#test_1)
<!-- TOC -->

# Description project


## Description
Ministry of Foreign Affairs of Ukraine (MFA of Ukraine) is a central executive body whose activities are directed and coordinated by the Cabinet of Ministers of Ukraine. The MFA of Ukraine is the main body in the system of central executive authorities in formulating and ensuring the implementation of the state policy in the field of foreign relations of Ukraine.

### Task
The Ministry of Foreign Affairs needs to process and analyze a large volume of telephone conversations. The goal is to create a structured dataset from audio recordings of these conversations, which can be used for future analysis and insights. If a conversation mentions a person's name and location, the system should extract and populate these details into the appropriate fields. Additionally, the system must categorize each conversation into one or more relevant categories and determine the emotional tone of the conversation

## Description of input data
As a user, I want to have API service with exact endpoints:

## CRUD of category
Categories represent the topics of conversation. Each conversation may cover multiple topics simultaneously. The conversation topics must be assigned correctly, as specialists will evaluate and assess the quality of the calls based on these topics from their respective fields.

When adding or updating a category, it is necessary to check if the conversations still belong to this category.

### GET category

– Returns a list of all conversation topics.

``
[{ "id": "category_id_1", "title": "Visa and Passport Services", "points": ["Border crossing", "International documentation"]}]
``
### POST category

– Creates a new conversation topic.

Request:

``
{"title": "Topic Title", "points": ["Key Point 1", "Key Point 2"]}  ``
``

Success Response (201 Created):

``
{"id": "new_category_id", "title": "Topic Title", "points": ["Key Point 1", "Key Point 2"]}``
``

Error Response (422 Unprocessable Entity)

### PUT category id

— Updates an existing conversation topic.

Request:

``
{"title": "New Topic Title", "points": ["New Key Point 1", "New Key Point 2"]}
``
Success Response (200 OK): 

``
{ "id": "category_id", "title": "New Topic Title", "points": ["New Key Point 1", "New Key Point 2"] }
``

Error Response (422 Unprocessable Entity)

### DELETE category id

 — Deletes a conversation topic by the specified identifier.

Success Response (200 OK)

Error Response (404 Not Found)

Validation Rules:
* **title** is required for POST, optional for PUT.
* **points** must be an array of strings if provided.

## Call

This API provides functionality for processing and analyzing audio calls. It allows users to submit audio files via a URL, where the service will handle the download, transcription, and analysis of the content. The system extracts key information such as the caller's name and location, determines the emotional tone of the conversation, and stores the results. Users can retrieve detailed information about a specific call using its unique identifier. The API supports wav and mp3 file formats and provides clear responses for successful operations as well as error conditions.

# GET call

– Retrieves details of a call by the specified identifier. The emotional tone must be one of the following values: Neutral, Positive, Negative, Angry. For the name and location fields: These are extracted from the call if possible. If extraction is not feasible or the information is unavailable, the fields will be returned as null

Success Response (200 OK): 

``
{  
  "id": "call_id",  
  "name": "Call Name",  
  "location": "Kyiv",  
  "emotional_tone": "Neutral",  
  "text": "Transcribed text",  
  "categories": ["Topic Title 1","Topic Title 2"]
}
``

Response (202 Accepted) if processing is not yet complete

## Requirements
1.  By default, five conversation topics should be created: Visa and Passport Services, Diplomatic Inquiries, Travel Advisories, Consular Assistance, Trade and Economic Cooperation.
2.  The system must be capable of operating without internet access (without relying on external services). File links can be sourced from a local network.
3. Calls conversation is conducted in English.
4. In the README, please describe the corner cases that are covered.

# Start Project
1. Go to the folder '**docker**' (as project root) which contains file docker-compose.py and folder Backend (contains project files);
2. You can type command "**docker-compose up**" or "**sudo docker-compose up**" into command line;
3. Open URl http://localhost:8080/api/v1/. You must see a list of sheets.

# Run tests
You have two choices how you can run tests:
1) You can open URL http://localhost:8080/api/v1/tests/
2)  You can type command "pytest Backend/tests/tests_views.py -s"
  
# Note to project:

# Description of input data

 
 # Test cases:
 
 ## test_1