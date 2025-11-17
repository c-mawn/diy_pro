# DIY Pro Extension 
![logo](./Logo.png)
## Human Computer Interaction -- Olin College of Engineering -- Fall '25
### Lily Wei, Trinity Lee, Kelsey McClung, AJ Bulow, Charlie Mawn

# Running The Extension:
- Download this repo to your local device
- Open your chrome extensions tab (chrome://extensions)[chrome://extensions] (you might need to type this into a tab yourself, as chrome:// is usually not linkable)
- Turn on developer mode
- Click 'load unpacked'
- Select the this downloaded directory to load
- Open the extension by opening your extensions menu, and selecting the DIY Pro extension

# Running The Website
- Run `pip install django` to install the django web framework
- After installing, `cd` into the `diy_pro_website` directory
- Once inside `diy_pro_website`, run `python manage.py runserver`. This will start up a local server.
- With the local server running, all buttons on the extension will correctly redirect to our website. If this isn't running, redirects to the website will show errors.
- Once finished, use `ctrl + c` to close the local server. Note: this is needs to be running 

# Tasks
- **Simple**: Image search. Use the DIY Pro extension to screenshot an image, search, and view closest matches.
- **Medium**: View purchasing options. After selecting the closest match, view purchasing and filter options from different online retailers and secondhand sites.
Medium: Learn more. View page of gathered resources from around the web. Click a tutorial to be taken to that webpage.
- **Complex**: Self Register themselves to be expert repairers. This means when people search for a tool, if someone registered themselves as an expert repairer, then people can see that they are someone that they can reach out for help
Prototype Limitations 

# Limitations
## Wizard-of-Oz & Hardcoded Limitations
Currently our prototype has Wizard-of-Oz search and filter features, as well as image search capabilities. This is mainly because figma has certain limitations that we felt we could preset without compromising the quality of the prototype. Furthermore the complex task is also limited as we did not have enough time to make it fully functional as part of our prototype, although there is enough to convey the overall idea. Search results would also be hard-coded as we could not actively scrap the internet via Figma.

## Other Limitations
Some limitations are that the current second iteration is still in progress and has some limited functionality due to the updated changes from the feedback. Our database for our complex task is also hard-coded/ignored as scaling questions are not addressed in the medium fidelity prototype.


