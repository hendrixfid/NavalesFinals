# Webex Teams Integration and Faker Data Generation Project

## Setup
1. Install Docker if not already installed.
2. Build the Docker image:
   ```bash
   docker build -t webex-faker-app .

   docker run -e WEBEX_ACCESS_TOKEN='your_access_token' webex-faker-app python webex_integration.py

   
### 4.3 Screenshots and Project Submission (10 Points)

- Take screenshots of:
  - Docker build
  - Webex room creation and message sending
  - Faker data generation outputs

Place these screenshots in a `/screenshots` folder in your repository.

### 4.4 GitHub Repository Link

- After completing the above steps, create your repository on GitHub and push your code. Provide the repository link for review:
   ```bash
   git remote add origin <your-repo-url>
   git push -u origin main
   
