import json, yaml, requests
from datetime import datetime
from urllib3 import disable_warnings

disable_warnings()

def get_secret(secret):
    try:
        with open('/config/secrets.yaml', 'r', encoding='utf8') as file:
            secrets = yaml.full_load(file)
            for key, value in secrets.items():
                if key == secret:
                    return value
    except FileNotFoundError:
        print('secrets.yaml not found')
        exit()

host = get_secret('udm_host')
username = get_secret('udm_username')
password = get_secret('udm_password')

login_response = requests.post(f'https://{host}/api/auth/login',
    headers={'Content-Type': 'application/json'},
    data=json.dumps({'username': username, 'password': password}),
    verify=False)

stats_response = requests.get(f'https://{host}/proxy/network/api/s/default/stat/device/',
    cookies=login_response.cookies,
    verify=False)

data = stats_response.json()['data'][0]

print(json.dumps({
    'cpu': data['system-stats']['cpu'],
    'cpu_temp': round(data['temperatures'][1]['value'], 1),
    'system_temp': round(data['temperatures'][0]['value'], 1),
    'memory': data['system-stats']['mem'],
    'disk': round(data['storage'][1]['used'] / data['storage'][1]['size'] * 100, 1),
    'internet': data['internet'],
    'uptime': datetime.fromtimestamp(data['startup_timestamp']).isoformat(),
    'availability': data['uptime_stats']['WAN']['availability'],
    'average_latency': data['uptime_stats']['WAN']['latency_average'],
    'down': data['uplink']['rx_rate'] / 1000000,
    'up': data['uplink']['tx_rate'] / 1000000,
    'version': data['displayable_version']
}))
