import multiprocessing

bind = "0.0.0.0:5000"
timeout = 120
worker_class = "gthread"
workers = multiprocessing.cpu_count() * 2 + 1
keepalive = 5
threads = 10