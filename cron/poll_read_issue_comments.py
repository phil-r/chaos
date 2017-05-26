import logging
import os
from os.path import abspath, dirname

import settings
import github_api as gh

THIS_DIR = dirname(abspath(__file__))

__log = logging.getLogger("chaosbot")

def handle_comment(issue_comment):
    issue_id = issue_comment["issue_id"]
    global_comment_id = issue_comment["global_comment_id"]
    comment_text = issue_comment["comment_text"]
    __log.debug("Handling issue {issue}: comment {comment_text}".format(issue=issue_id, comment=comment_text)
    # Do stuff here

def poll_read_issue_comments():
    __log.info("looking for issue comments")

    api = gh.API(settings.GITHUB_USER, settings.GITHUB_SECRET)
    
    issue_comments = gh.comments.get_all_issue_comments(api, settings.URN)
    
    for issue_comment in issue_comments:
        handle_comment(issue_comment)
  
    __log.info("Waiting %d seconds until next scheduled Issue comment polling",
               settings.ISSUE_COMMENT_POLLING_INTERVAL_SECONDS)
