from robocorp.tasks import task
from robocorp import browser 

@task
def extract_data_from_website():
    """ Extract data from a new website """
    browser.configure(
        slowmo=100,
    )   
    open_the_website()
    # log_in()

def open_the_website():
    """ Open the website by navigating to the given URL"""
    # browser.goto("https://gothamist.com/")
    browser.goto("https://robotsparebinindustries.com/")

# def log_in():
#     """ Fills in the login form and clicks on the 'Log in' button """
#     page = browser.page()
#     page.fill("#username", "maria")



