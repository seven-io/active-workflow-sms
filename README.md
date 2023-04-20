![](https://www.seven.io/wp-content/uploads/Logo.svg "seven Logo")

# Official Agent for [Active Workflow](https://github.com/automaticmode/active_workflow)

Custom agent using the remote API from Active Workflow. 
Please notice that scheduling does nothing 
even though the agent interface might not reflect that.


## Installation
**Start Flask:**

`python3.8 main.py`

**Expose remote agent URL in environment**

`export REMOTE_AGENT_URL="http://localhost:5000/"`

**Create a new user credential**

The API key can alternatively be stored as environment variable 
SEVEN_API_KEY on the Flask server. In this case you can go on to the next step.


Go to /user_credentials/new

Credential Name: seven_api_key

Credential Value: Your API key from seven.io
![Screenshot: Create User Credential](screenshots/create_credential.png "Screenshot: Create User Credential")

**Create a new agent**

Create a new agent with options in the format of:
![Screenshot: Create Agent](screenshots/create_agent.png "Screenshot: Create Agent")
The option apiKey may also be defined as environment variable SEVEN_API_KEY.

### Development
**Start Flask:**

`python3.8 main.py`

**Start Active Workflow:**

`docker run --network host -e REMOTE_AGENT_URL=$REMOTE_AGENT_URL -p 3000:3000 --rm -v aw-data:/var/lib/postgresql/11/main automaticmode/active_workflow`


#### Support
Need help? Feel free to [contact us](https://www.seven.io/en/company/contact/).


##### License
[![MIT](https://img.shields.io/badge/License-MIT-teal.svg)](LICENSE)