import threading

def run_async(target_func, *args, **kwargs):
    thread = threading.Thread(target=target_func, args=args, kwargs=kwargs)
    thread.start()
