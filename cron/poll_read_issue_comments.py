import logging
import os
from os.path import abspath, dirname

import settings
import github_api as gh

THIS_DIR = dirname(abspath(__file__))

__log = logging.getLogger("chaosbot")

'''
Command Syntax
/vote close closes issue when no nay reactions on this comment are added within voting window
/vote reopen reopens issue when see above ^^^
/vote label=<LABEL_TEXT> adds label when ^^^
/vote remove-label=<LABEL_TEXT> removes label when ^^^
/vote assign=<USER> assigns to user when ^^^
/vote unassign=<USER> unassigns from user when ^^^
'''

COMMAND_LIST = ["/vote"]

def handle_vote_command(command):
    orig_command = command[:]
    # Check for correct command syntax, ie, subcommands
    log_warning = False
    if(len(command)):
        sub_command = command.pop(0)
        if(sub_command == "close"):
            pass # do stuff
        elif(sub_command == "reopen"):
            pass # do stuff
        else:
            # Other commands have an = in them
            sub_command = sub_command.split("=")
            if(len(sub_command > 1)):
                args = sub_command[1:]
                sub_command = sub_command[0]
                if(sub_command == "label"):
                    pass
                elif(sub_command == "remove-label"):
                    pass
                elif(sub_command == "assign"):
                    pass
                elif(sub_command == "unassign"):
                    pass
                else:
                    log_warning = True
            else:
                log_warning = True    
    else:
        log_warning = True
        
    if log_warning:
        __log.warning("Unknown issue command syntax: /vote {command}".format(command=orig_command))

def handle_comment(issue_comment):
    issue_id = issue_comment["issue_id"]
    global_comment_id = issue_comment["global_comment_id"]
    comment_text = issue_comment["comment_text"]
    __log.debug("Handling issue {issue}: comment {comment_text}".format(issue=issue_id, comment=comment_text))
    
    parsed_comment = map(lambda x: x.lower().strip(), comment_text.split(' '))
    
    command = parsed_comment.pop(0)
    if command in COMMAND_LIST:
        # We doin stuff boyz
        if command == "/vote":
            handle_vote_command(parsed_comment)

def poll_read_issue_comments():
    __log.info("looking for issue comments")

    api = gh.API(settings.GITHUB_USER, settings.GITHUB_SECRET)
    
    issue_comments = gh.comments.get_all_issue_comments(api, settings.URN)
    
    for issue_comment in issue_comments:
        handle_comment(issue_comment)
        
    __log.info("Waiting %d seconds until next scheduled Issue comment polling",
               settings.ISSUE_COMMENT_POLLING_INTERVAL_SECONDS)
