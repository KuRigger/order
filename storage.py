import json
from pathlib import Path
from config import APPLICATIONS_FILE, APPROVED_FILE

class JSONStorage:
    def __init__(self, filename):
        self.filename = Path(filename)
        self.data = self._load()
        
    def _load(self):
        try:
            if not self.filename.exists():
                self.filename.touch()
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, Exception):
            return []
            
    def _save(self):
        self.filename.parent.mkdir(exist_ok=True)
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2)
            
    def add(self, item):
    # Проверка дубликатов
        duplicate = next((x for x in self.data if 
            x.get('user_id') == item.get('user_id') or 
            x.get('email') == item.get('email') or 
            x.get('phone') == item.get('phone')), None)
        
        if duplicate:
            return False 
        self.data.append(item)
        self._save()
        return True
        
    def remove(self, predicate):
        self.data = [item for item in self.data if not predicate(item)]
        self._save()
        
    def find(self, predicate):
        return next((item for item in self.data if predicate(item)), None)

applications_storage = JSONStorage(APPLICATIONS_FILE)
approved_storage = JSONStorage(APPROVED_FILE)