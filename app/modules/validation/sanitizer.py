"""
Sanitizer Module
"""


class Sanitizer():
    """Sanitize Inputs Module"""

    # Input Value
    _input = None

    # Sanitized Input Value
    _sinput = None

    def set_input(self, input_value):
        """Set Input Value"""
        self._input = input_value

    def set_sinput(self, sinput_value):
        """Set Sanitized Input Value"""
        self._sinput = sinput_value

    def get_sinput(self):
        """Get sanitized input value"""
        return self._sinput

    def get_input(self):
        """Get original input value"""
        return self._input

    def is_exact(self):
        """Check if original and sanitized value are the same"""
        return self._input == self._sinput and len(self._input) == len(self._sinput)

    def strip(self, chars=''):
        """Strip input value"""
        if not isinstance(self._input, (str)):
            self._sinput = str(self._input)
        else:
            self._sinput = self._input

        if len(chars) > 0:
            self._sinput = self._sinput.strip(chars)
        else:
            self._sinput = self._sinput.strip()

        return self._sinput

    def lstrip(self, chars=''):
        """Left strip input value"""
        if not isinstance(self._input, (str)):
            self._sinput = str(self._input)
        else:
            self._sinput = self._input

        if len(chars) > 0:
            self._sinput = self._sinput.lstrip(chars)
        else:
            self._sinput = self._sinput.lstrip()

        return self._sinput

    def rstrip(self, chars=''):
        """Right strip input value"""
        if not isinstance(self._input, (str)):
            self._sinput = str(self._input)
        else:
            self._sinput = self._input

        if len(chars) > 0:
            self._sinput = self._sinput.rstrip(chars)
        else:
            self._sinput = self._sinput.rstrip()

        return self._sinput

    def escape(self, chars=['&', '"', '\'', '>', '<']):
        """Escape input value"""
        html_escape_table = {
            "&": "&amp;" if '&' in chars else '&',
            '"': "&quot;" if '"' in chars else '"',
            "'": "&apos;" if '\'' in chars else '\'',
            ">": "&gt;" if '>' in chars else '>',
            "<": "&lt;" if '<' in chars else '<',
        }

        if not isinstance(self._input, (str)):
            self._sinput = str(self._input)
        else:
            self._sinput = self._input

        self._sinput = "".join(html_escape_table.get(c, c) for c in self._sinput)
        return self._sinput