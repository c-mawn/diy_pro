# DIY Pro Extension 
![logo](./Logo.png)
## Human Computer Interaction -- Olin College of Engineering -- Fall '25
### Lily Wei, Trinity Lee, Kelsey McClung, AJ Bulow, Charlie Mawn

# Running The Extension:
- Download this repo to your local device
- Open your chrome extensions tab [chrome://extensions](chrome://extensions) (you might need to type this into a tab yourself, as chrome:// is usually not linkable)
- Turn on developer mode
- Click 'load unpacked'
- Select the this downloaded directory to load
- Open the extension by opening your extensions menu, and selecting the DIY Pro extension

# Getting Scraping Token Access
- Create an account with Scrape.do
- After following instructions with signing up and logging in, you can get the API key on the scraping website home screen. Follow this for further instructions: https://scrape.do/documentation/
- After getting the token, in terminal run `export TOKEN=` and then your token to set up token access

# Running The Website
- Run `pip install django` to install the django web framework
- After installing, `cd` into the `diy_pro_website` directory
- Once inside `diy_pro_website`, run `python manage.py runserver`. This will start up a local server.
- With the local server running, all buttons on the extension will correctly redirect to our website. If this isn't running, redirects to the website will show errors.
- Once finished, use `ctrl + c` to close the local server. Note: this is needs to be running 

# Contextual Framing
Imagine that you have just dropped your iPhone on the ground. The screen shatters, and you try to turn it on. Over and over, the screen flashes on, then after a moment, it turns back off. You don't have the money to buy a new phone right now, so you are determined to fix it yourself. You know that there are tons of videos on YouTube that can guide you through the process of fixing a broken screen, so you go to your computer and start searching. You come across a video that shows the person removing the phone screen, detaching it from the motherboard, and replacing the screen. You see the person use what looks like a tiny, unique screwdriver to remove a piece, but you have no idea where to buy the screwdriver. You haven’t seen this kind of screwdriver before, so you don't even know how to search for this exact screwdriver! So, you open the DIY Pro web extension to solve your problem.

# Tasks
- **Simple**: Image search. Use the DIY Pro extension to screenshot an image, search, and view closest matches.
- **Medium**: View purchasing options. After selecting the closest match, a list of tool purchase options will pop up with links too eBay pages. A list of expert repairers with skill sets around the tool also pops up with links to their profiles.
- **Complex**: Self Register themselves to be expert repairers. This means when people search for a tool, if someone registered themselves as an expert repairer, then people can see that they are someone that they can reach out for help

# Limitations
## Wizard-of-Oz & Hardcoded Limitations
Currently our prototype has the image search hardcoded. There is no AI analyzing the image and the image search results are fixed two five hard coded tools. The users in our database are also hardcoded. They are not real users and are randomly generated. Our tool tags for the users are also hardcoded too. Aside from those two, everything has been programmed to be functional. Our purchase tools page uses a script to scrape eBay for tools and our signup for users registers new users to our database. 

## Other Limitations
Some limitations are that the current second iteration is still in progress and has some limited functionality due to the updated changes from the feedback. Our database for our complex task is also hard-coded/ignored as scaling questions are not addressed in the medium fidelity prototype. Another big limitation is there is a bottleneck for webscraping due to needing to go through a third party to scrape eBay and as a result getting purchase results can take a while.

### Prior Work
- [First Iteration Figma Mockup](https://www.figma.com/proto/LCviy8TuxBVq5s4NyyT42r/LEvel-4-Part-6-Prototype?node-id=2-9&p=f&t=sNdPTx6cy81cT1IS-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=2%3A9)
- [Second Iteration Figma Mockup](https://www.figma.com/design/JsrGG0Rd2pEv7UIJjapmBi/LEvel-4-Updated-Prototype?m=auto&t=EEBaXXNXgl8Qu3J3-6)


