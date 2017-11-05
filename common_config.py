import yaml
from collections import namedtuple

with open('train.yml', 'r', encoding='utf-8') as yml_file:
	model_cfg = yaml.safe_load(yml_file)
	DataConfig = namedtuple('DataConfig', model_cfg['data'].keys())(**model_cfg['data'])
	ModelConfig = namedtuple('ModelConfig', model_cfg['model'].keys())(**model_cfg['model'])
