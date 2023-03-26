

RPC = "https://arb1.arbitrum.io/rpc"


login = 'my_login'
password = 'my_password'
address = '207.164.21.34'
port = '3128'

proxies = { 'all': f'http://{login}:{password}@{address}:{port}',}

changeIPlink = ""

request_kwargs = {"proxies":proxies, "timeout": 120}