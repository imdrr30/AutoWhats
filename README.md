# AutoWhats
Automate WhatsApp for away messages
## Deploy in Heroku
In order to work in background we need to deploy it in a server.
### Getting Started
- Get Heroku Free Dyno Account
- Install Heroku-CLI in your Machine
- In terminal or cmd enter:
- `$ heroku login`
- After Logging in
- Create an App.
- `$ heroku apps:create [NEW_APP_NAME]`
- Access that App
- `$ heroku git:remote -a YOUR_APP_NAME`

### Pre-Configuration 1
- Since We use Selenium with Chrome. We need to provide required dependencies for heroku.
```
heroku buildpacks:set heroku/python
heroku buildpacks:set https://github.com/heroku/heroku-buildpack-chromedriver
heroku buildpacks:set https://github.com/heroku/heroku-buildpack-google-chrome
```
- Copy and Paste above code in terminal
### Pre-Configuration 2
- Set ENV variable so that program knows where the drivers are located.
```
heroku config:set CHROMEDRIVER_PATH=/app/.chromedriver/bin/chromedriver
heroku config:set GOOGLE_CHROME_BIN=/app/.apt/usr/bin/google-chrome
```
- Copy and Paste above code in terminal
### Clone this repo and Push
- Clone this repo
- Go to the repo directoy.
```
git init
git add .
git commit -m "AutoWhatsService"
git push heroku master
```
- Paste this in terminal or cmd to deploy.
## Running the App
- After successful deployment, you can run the app by calling `<YOUR_APP_NAME>.herokuapp.com`.
- You will get the QR CODE to Scan
- After Scanning Click `Start` link.
- Finally you can see. Your WhatsApp message are being Auto Replied.
