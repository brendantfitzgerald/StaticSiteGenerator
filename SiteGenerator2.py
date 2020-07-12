#Site Generator
#Create Posts and Pages according to Templates
#Parse beginning of post for "Template" and "Title"

import yaml
import markdown
import json
import os

#Load variables from JSON
SiteJSON = 'SiteGenerator.JSON'

SiteVariables = yaml.load(open(SiteJSON,'r'))
InputPath = SiteVariables['InputPath']
InputFiles = os.listdir(InputPath)
OutputPath = SiteVariables['OutputPath']
OutputFiles = os.listdir(OutputPath)
SiteName = SiteVariables['SiteName']



print (SiteVariables['SiteName'])