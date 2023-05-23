from multiprocessing import cpu_count


def max_workers():
    return cpu_count()


bind = '0.0.0.0:80'
max_requests = 1000
worker_class = 'uvicorn.workers.UvicornWorker'
workers = max_workers()
