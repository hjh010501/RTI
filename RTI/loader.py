def database_load(*databases):
    for database in databases:
        __import__('RTI.Database.{}'.format(database))


def feature_load(*features):
    for feature in features:
        __import__('RTI.Feature.{}'.format(feature))


def resource_load(*resources):
    for resource in resources:
        __import__('RTI.Resource.{}'.format(resource))
