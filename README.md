
## Make your kindle4rss.com have an automated recurring push button press to send your articles to Kindle Reader or App

#### What is this?
It clicks on button to deliver new content on your kindle. Iff you only need 25 articles an dont need any other pro features this will deliver your content by pressing the button. If you do like the service and need pro fetures like >25 articles  please signup for paid pro account at kindle4rss.com  


#### Instructions
* export variables for username and password using USERNAME and PASSWORD for script to work
* have Python3 PIP install all modules in requirements.txt
* Add this script to your crontab like this to get all articles at 5AM every day:
  ```
  0 5 * * * python3 <path-to-script>/kindle4rss_push.py
  ```

## GitHub actions setup (no server needed, GitHub will run this nightly in Docker Container)
* please see my main.yaml for a GitHub Actions nightly Cronjob
* dont forget to add your GihHub Repo Secrets to your repo settings -> secrets section first

**original Python2 ported code:** www.github.com/dcrystalj/kindle4rss
