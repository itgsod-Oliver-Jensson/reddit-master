import yaml



with open("config.yaml") as config_file:
    config = yaml.load(config_file)


print config


from connections import Client


client = Client()




