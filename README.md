<p align="center">
  <img src="https://www.seven.io/wp-content/uploads/Logo.svg" width="250" alt="seven logo" />
</p>

<h1 align="center">seven SMS for Active Workflow</h1>

<p align="center">
  Official remote agent for <a href="https://github.com/automaticmode/active_workflow">Active Workflow</a> that sends SMS via the seven gateway.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-teal.svg" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/Active%20Workflow-remote%20agent-blue" alt="Active Workflow remote agent" />
  <img src="https://img.shields.io/badge/Python-3.8%2B-yellow" alt="Python 3.8+" />
</p>

---

## Features

- **Send SMS** - Trigger SMS messages from any Active Workflow scenario via the remote agent API
- **Credential or Env Auth** - Pass the API key as user credential or as `SEVEN_API_KEY` environment variable
- **Self-hosted Flask service** - Runs alongside your Active Workflow instance with no external dependencies

> **Note:** The Active Workflow remote-agent API does not support scheduling. The agent UI may show scheduling options - they are intentionally non-functional.

## Prerequisites

- Python 3.8+
- An Active Workflow instance reachable from the agent host
- A [seven account](https://www.seven.io/) with API key ([How to get your API key](https://help.seven.io/en/developer/where-do-i-find-my-api-key))

## Installation

### 1. Clone and start the Flask agent

```bash
git clone https://github.com/seven-io/active-workflow-sms.git
cd active-workflow-sms
pip install -r requirements.txt
python3.8 main.py
```

The agent listens on `http://localhost:5000/`.

### 2. Expose the agent URL to Active Workflow

```bash
export REMOTE_AGENT_URL="http://localhost:5000/"
```

### 3. Run Active Workflow

```bash
docker run --network host \
  -e REMOTE_AGENT_URL=$REMOTE_AGENT_URL \
  -p 3000:3000 --rm \
  -v aw-data:/var/lib/postgresql/11/main \
  automaticmode/active_workflow
```

## Configuration

### Option A: User credential

In Active Workflow open `/user_credentials/new` and create:

| Field | Value |
|-------|-------|
| Credential Name | `seven_api_key` |
| Credential Value | Your seven API key |

![Create User Credential](screenshots/create_credential.png)

### Option B: Environment variable

Set `SEVEN_API_KEY` on the host running `main.py` and skip the credential step entirely.

## Usage

Create a new agent in Active Workflow and pick the seven SMS agent type. The minimum option set is:

![Create Agent](screenshots/create_agent.png)

`apiKey` may also be omitted if `SEVEN_API_KEY` is exported on the agent host.

## Support

Need help? Feel free to [contact us](https://www.seven.io/en/company/contact/) or [open an issue](https://github.com/seven-io/active-workflow-sms/issues).

## License

[MIT](LICENSE)
