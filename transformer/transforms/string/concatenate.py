from transformer.registry import register
from transformer.transforms.base import BaseTransform


class StringConcatenateTransform(BaseTransform):

    category = 'string'
    name = 'concatenate'
    label = 'Concatenate Array of Strings'
    help_text = (
        '[\'a\',\'b\',\'c\'] will be concatenated into \'abc\'.'
    )
    noun = 'Line-item'
    verb = 'concatenate'

    def transform_many(self, inputs, options=None, **kwargs):
        """
        Override the standard behavior of the transform_many by only
        accepting list inputs which we use to perform the join operation.
        """

        if options is None or options.get('join_text') is None:
            join_text = ""
        else:
            join_text = options.get('join_text')

        if not isinstance(inputs, list):
            self.raise_exception('Concatenate requires a line-item as input.')

        return join_text.join(inputs)

    def fields(self, *args, **kwargs):
        return [
            {
                'type': 'unicode',
                'required': False,
                'key': 'join_text',
                'label': 'Text to put between each concatenation',
                'help_text': (
                    'Text to put between each concatenation. '
                    'Concatenation of [\'a\', \'b\', \'c\'] with join_text = \'-\' will result in \'a-b-c\'. '
                    'Default value is empty.'
                ),
            },
        ]


register(StringConcatenateTransform())
