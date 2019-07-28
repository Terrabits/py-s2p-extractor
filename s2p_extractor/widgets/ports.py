
port_regex          = r'\d*[1-9]+'
range_regex         = f'{port_regex}\\-{port_regex}'
port_or_range_regex = f'[({port_regex})({range_regex})]'
is_valid_regex      = f'^(({port_or_range_regex}),)*({port_or_range_regex})$'
