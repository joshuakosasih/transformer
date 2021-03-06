from transformer.registry import register
from transformer.transforms.base import BaseTransform


class UtilStringToLineItemTransform(BaseTransform):

    category = 'util'
    name = 'string_to_lineitem'
    label = 'Text to Line-item'
    help_text = (
        'Convert comma delimited text to a line-item. \'a,b,c,d\' becomes [a,b,c,d]. More on line-items '
        '[here](https://zapier.com/help/formatter/#how-use-line-items-formatter).'
    )
    

    noun = 'Text'
    verb = 'Convert'

    def transform(self, str_input, **kwargs):

        if not str_input:
            return u''

        segments = str_input.split(',')
        return segments

register(UtilStringToLineItemTransform())
