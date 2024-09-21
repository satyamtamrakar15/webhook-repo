from flask import Blueprint, json, request,jsonify
from .utils import convert_iso_to_utc_string
import flask_pymongo
from app.extensions import mongo


webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')


@webhook.post('/receiver')
def receiver():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')
    event_data={}
    if event_type == 'push':
        event_data = {
            "request_id":data["after"],
            "author": data['pusher']['name'],
            "action": "PUSH",
            "to_branch": data['ref'].split('/')[-1],
            "timestamp":convert_iso_to_utc_string(data['head_commit']['timestamp'])
        }
    elif event_type == 'pull_request':
        if data['action']=='opened':
            event_data = {
                "request_id":data["pull_request"]["id"],
                "author": data['pull_request']['user']['login'],
                "action": "PULL_REQUEST",
                "from_branch": data['pull_request']['head']['ref'],
                "to_branch": data['pull_request']['base']['ref'],
                "timestamp": data['pull_request']['created_at']  
            }
        elif data['action']=='closed' and  data['pull_request']['merged_at'] is not None:
            event_data = {
                "request_id":data["pull_request"]["id"],
                "author": data['pull_request']['merged_by']['login'],
                "action":"MERGED",
                "from_branch": data['pull_request']['head']['ref'],
                "to_branch": data['pull_request']['base']['ref'],
                "timestamp": data['pull_request']['merged_at']
            }
    if event_data:
        try:
            mongo.db.events.insert_one(event_data)
            print("Event saved to DB  event:",event_data)
        except Exception as e:
            print("Error while saving to DB",e)
            return jsonify(e),500
    return {}, 200



@webhook.get('/events')
def get_github_events():
    try:
        page = int(request.args.get('page', 0))
        limit = int(request.args.get('limit', 50))
        skip = page * limit
        filter_option={}
        start_timestamp=request.args.get('start_timestamp')
        if start_timestamp:
            filter_option["timestamp"]={"$gt":start_timestamp}
        data = mongo.db.events.find(filter_option).sort('timestamp', flask_pymongo.DESCENDING).skip(skip).limit(limit).to_list()
        for item in data:
            item['_id'] = str(item.get('_id'))
        data.reverse()
        return jsonify(data), 200
    except Exception as e:
        return jsonify(error=str(e)), 500
