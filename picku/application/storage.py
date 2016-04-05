from datetime import datetime
from collections import defaultdict
import uuid


class Storage():

    def __init__(self):
        self.by_routing_key = defaultdict(list)
        self.by_id = defaultdict(list)

    def save(self, routing_key, message):
        message_id = str(uuid.uuid1())
        entry = {'id': message_id, 'body': message, 'key': routing_key, 'ts': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        self.by_routing_key[routing_key].insert(0, entry)
        self.by_id[message_id] = entry

    def routing_keys(self):
        keys = [{'key': k, 'items': len(v)} for k, v in self.by_routing_key.items() if len(v)]
        keys.sort(key=lambda x: x['key'])
        return keys

    def messages(self, routing_key):
        return self.by_routing_key[routing_key]

    def get(self, message_id):
        return self.by_id[message_id]
