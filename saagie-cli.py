import click
import requests
import json
from requests.auth import HTTPBasicAuth

## Default params
defaultTarget = 'saagie-beta.prod.saagie.io'
defaultApiVersion = 'v1'
defaultConfigCacheFolder = '~/.saagie'
defaultConfigFile = 'config.json'

## Init some vars
saagiePlatform = ""
configFileFullPath = defaultConfigCacheFolder + '/' + defaultConfigFile

## Connect to a platform
@click.command()
@click.option('-u', '--username', prompt='Username: ', type=string, help="Login to the platform")
@click.option('-p', '--password', prompt='Password: ', type=string, hide_input=True, confirmation_prompt=True, help='Password to connect the platform')
@click.option('-e', '--environment', prompt='Environment: ', type=string, help='Desired target environment')
@click.option('-a', '--apiversion', prompt='API version: ', default=defaultApiVersion, type=string, help='Set the api version')
@click.argument('target', type=string, default=defaultTarget, show_default=True, help="Provide the desired target hostname")
def login(username, password, environment, target, apiversion):

    if (target and username and password):
        config['targets'][target]['username'] = username
        config['targets'][target]['password'] = password
        config['targets'][target]['environment'] = environment
        config['targets'][target]['apiversion'] = apiversion

        ## Update config cache file or create a new one
        try:
            with open(configFileFullPath, 'w') as configFile:
                json.dump(config, configFile)

        except e:
            echo.click(e)

    ## Authenticate
    saagiePlatform = "https://" + target + "/api/" +
    url = saagiePlatform + "/auth"
    requests.get(url, auth=HTTPBasicAuth(username, password))
    click.echo("Login Succeeded")   
