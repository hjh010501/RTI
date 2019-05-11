def database_load(*databases):
    for database in databases:
        __import__('RTI.database.{}'.format(database))


def feature_load(*features):
    for feature in features:
        __import__('RTI.feature.{}'.format(feature))


def resource_load(*resources):
    for resource in resources:
        __import__('RTI.resource.{}'.format(resource))
