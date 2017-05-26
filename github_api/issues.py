

def close_issue(api, urn, issue_id):
    path="/repos/{urn}/issues/{issue}".format(urn=urn, issue=issue_id)
    data = {"state": "closed"}
    resp = api("PATCH", path, json=data)
    return resp
    
def open_issue(api, urn, issue_id):
    path="/repos/{urn}/issues/{issue}".format(urn=urn, issue=issue_id)
    data = {"state": "open"}
    resp = api("PATCH", path, json=data)
    return resp
