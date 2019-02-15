import yaml
import logging
import jsonschema


logger = logging.getLogger(__name__)


class GridCard:

    default_yaml_file_schema = {
        'type': 'object',
        'properties': {
            'grid': {
                'type': 'object',
                'patternProperties': {
                    '\w': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'minLength': 1,
                            'maxLength': 1,
                            'pattern': '\w',
                        },
                        'minItems': 1,
                    }
                },
                'additionalProperties': False,
                'minProperties': 1,
            },
            'serial': {
                'type': 'string',
                'pattern': '\w+'
            },
        },
        'required': ['grid', 'serial', ],
    }

    def __init__(self, grid_filepath):
        self.grid_filepath = grid_filepath
        self.grid_data = self.get_grid()

    def get_grid(self):
        data = self.load_grid_file(self.grid_filepath)
        logger.debug("Raw data from file: {}".format(data))
        self.validate_grid_data(data)
        return data

    def get_coordinate(self, key, number):
        return self.grid_data[str(key).lower()][int(number)-1]

    def get_serial(self):
        return self.grid_data['serial']

    def load_grid_file(self, grid_filepath):
        logger.debug("Loading grid file {}".format(grid_filepath))
        with open(grid_filepath, 'r') as f:
            return yaml.load(f)

    def validate_grid_data(self, yaml_data):
        validator = jsonschema.Draft4Validator(self.get_yaml_file_schema())
        errors = [str(e) for e in sorted(validator.iter_errors(yaml_data), key=str)]
        if len(errors):
            message = ("The following errors were "
                       "found while loading the grid card:\n{}"
                       ).format("\n\n".join(errors))
            raise ValueError(message)


    def get_yaml_file_schema(self):
        return self.default_yaml_file_schema


if __name__ == "__main__":
    card = GridCard("/home/usrolh/local/etc/grid_10115.yml")
    print(card.grid_data)
