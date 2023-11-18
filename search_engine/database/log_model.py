class LogModel:
    def __init__(self, log_data):
        self.timestamp = log_data['timestamp']
        self.message = log_data['message']
        # Extract other necessary fields