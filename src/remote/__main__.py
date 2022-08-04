import uvicorn


def main():
    uvicorn.run('remote:app', port=4444, log_level='info', reload=True)
