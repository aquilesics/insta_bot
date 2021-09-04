from instapy import InstaPy
from instapy import smart_run
from dotenv import load_dotenv
import os

load_dotenv()

# login credentials
insta_username = os.getenv('INSTA_USER')
insta_password = os.getenv('INSTA_PASS')


# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
  """ Activity flow """	
  session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)
	
  # general settings		
  #  session.set_dont_include(["friend1", "friend2", "friend3"])		
  
  # activity		
  session.unfollow_users(amount=500,
                           style="FIFO",
						#    instapy_followed_enabled = True,
						#    instapy_followed_param = "all",
						#    nonFollowers = False,
                           unfollow_after=12 * 60 * 60, sleep_delay=601)