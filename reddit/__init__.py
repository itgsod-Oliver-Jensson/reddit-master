import yaml

with open("config.yaml") as config_file:
    config = yaml.load(config_file)


from reddit.connections import Client


client = Client()




