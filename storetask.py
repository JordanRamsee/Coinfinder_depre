class StoreTask:
    def __init__(self, task_id, exchanges, proxy, crypto_pair, proxy_exchanges):
        self.task_id = task_id
        self.exchanges = exchanges        
        self.proxy = proxy
        self.crypto_pair = crypto_pair
        self.proxy_exchanges = proxy_exchanges
