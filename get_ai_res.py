"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import google.generativeai as genai

def ask_ai(data, query):
    # Configure the Google AI API with your API key
    genai.configure(api_key="YOUR_GOOGLE_API_KEY")

    # Create the model
    # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    # Start a chat session with the model
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "{\n  \"meta\": {\n    \"page\": {\n      \"cursor\": \"VMpBDsIgEEbhvcf41yyQWBO5ijGGUqBjp2pn0I3x7oau7PLlfbf9B1qF7gX-DA59Yhi8A78SLgb6kNoGDa0yia4pKV7jU7Ms1J-WqXPHg4vDaBvisDHjPP2Z1JXV0EwV3lmDzKEovP3ufgEAAP__\",\n      \"more\": true,\n      \"size\": 20\n    }\n  },\n  \"records\": [\n    {\n      \"id\": \"rec_cpsfrqib9qk52642cdh0\",\n      \"label\": \"idle\",\n      \"value\": 0.996094,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T05:02:34.944282Z\",\n        \"updatedAt\": \"2024-06-24T05:02:34.944282Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpsfrrcanfu3uibvm9c0\",\n      \"label\": \"idle\",\n      \"value\": 0.996094,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T05:02:37.440576Z\",\n        \"updatedAt\": \"2024-06-24T05:02:37.440576Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpsfrsf2qckgh4f8jeo0\",\n      \"label\": \"idle\",\n      \"value\": 0.996094,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T05:02:41.405013Z\",\n        \"updatedAt\": \"2024-06-24T05:02:41.405013Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpsfrtab9qk52642cdhg\",\n      \"label\": \"updown\",\n      \"value\": 0.546875,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T05:02:45.395264Z\",\n        \"updatedAt\": \"2024-06-24T05:02:45.395264Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpsfruf2qckgh4f8jeog\",\n      \"label\": \"snake\",\n      \"value\": 0.71875,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T05:02:49.381841Z\",\n        \"updatedAt\": \"2024-06-24T05:02:49.381841Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpsfrvab9qk52642cdi0\",\n      \"label\": \"snake\",\n      \"value\": 0.992188,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T05:02:53.377602Z\",\n        \"updatedAt\": \"2024-06-24T05:02:53.377602Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpsfs0ab9qk52642cdig\",\n      \"label\": \"idle\",\n      \"value\": 0.996094,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T05:02:57.364044Z\",\n        \"updatedAt\": \"2024-06-24T05:02:57.364044Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpsg5d4anfu3uibvm9fg\",\n      \"label\": \"idle\",\n      \"value\": 0.996094,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T05:23:00.905866Z\",\n        \"updatedAt\": \"2024-06-24T05:23:00.905866Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpsg5dab9qk52642cdq0\",\n      \"label\": \"idle\",\n      \"value\": 0.996094,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T05:23:01.728819Z\",\n        \"updatedAt\": \"2024-06-24T05:23:01.728819Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpshmaib9qk52642cdr0\",\n      \"label\": \"updown\",\n      \"value\": 0.996094,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T07:07:22.859644Z\",\n        \"updatedAt\": \"2024-06-24T07:07:22.859644Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpshmbkanfu3uibvm9h0\",\n      \"label\": \"wave\",\n      \"value\": 0.734375,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T07:07:26.656963Z\",\n        \"updatedAt\": \"2024-06-24T07:07:26.656963Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpshmcib9qk52642cdrg\",\n      \"label\": \"updown\",\n      \"value\": 0.976562,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T07:07:30.260216Z\",\n        \"updatedAt\": \"2024-06-24T07:07:30.260216Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpshmdib9qk52642cds0\",\n      \"label\": \"updown\",\n      \"value\": 0.996094,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T07:07:34.248744Z\",\n        \"updatedAt\": \"2024-06-24T07:07:34.248744Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpshmeib9qk52642cdsg\",\n      \"label\": \"updown\",\n      \"value\": 0.996094,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T07:07:38.245906Z\",\n        \"updatedAt\": \"2024-06-24T07:07:38.245906Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpshmfkanfu3uibvm9hg\",\n      \"label\": \"updown\",\n      \"value\": 0.996094,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T07:07:42.225272Z\",\n        \"updatedAt\": \"2024-06-24T07:07:42.225272Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpshmgib9qk52642cdt0\",\n      \"label\": \"updown\",\n      \"value\": 0.996094,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T07:07:46.216014Z\",\n        \"updatedAt\": \"2024-06-24T07:07:46.216014Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpshmhkanfu3uibvm9i0\",\n      \"label\": \"snake\",\n      \"value\": 0.988281,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T07:07:50.207201Z\",\n        \"updatedAt\": \"2024-06-24T07:07:50.207201Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpshmiib9qk52642cdtg\",\n      \"label\": \"snake\",\n      \"value\": 0.992188,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T07:07:54.202537Z\",\n        \"updatedAt\": \"2024-06-24T07:07:54.202537Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpshmjib9qk52642ce0g\",\n      \"label\": \"idle\",\n      \"value\": 0.996094,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T07:07:58.192814Z\",\n        \"updatedAt\": \"2024-06-24T07:07:58.192814Z\",\n        \"version\": 0\n      }\n    },\n    {\n      \"id\": \"rec_cpshmkib9qk52642ce5g\",\n      \"label\": \"updown\",\n      \"value\": 0.996094,\n      \"xata\": {\n        \"createdAt\": \"2024-06-24T07:08:02.174414Z\",\n        \"updatedAt\": \"2024-06-24T07:08:02.174414Z\",\n        \"version\": 0\n      }\n    }\n  ]\n}\n\n\nwhat are all the labels that are present?\n",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "The following labels are present in the provided data:\n\n* **idle**\n* **updown**\n* **snake**\n* **wave** \n",
                ],
            },
            {
                "role": "user",
                "parts": [
                    "how many idle states?",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "There are **10** idle states in the provided data. \n",
                ],
            },
        ]
    )

    # Send a message to the chat session with the updated data and query
    response = chat_session.send_message(f"{data} - Based on the given data, answer the following question: {query}")

    return response.text
