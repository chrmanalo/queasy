from queasy.utils import converters, pipeline, tracer, yaml_reader

def test_converters():
    assert converters.number_to_upper(1) == 'A'

def test_pipeline():
    def filter_odd(items):
        return list(filter(lambda item: item % 2 != 0, items))
    def filter_gt5(items):
        return list(filter(lambda item: item > 5, items))
    test_data = [i for i in range(10)]
    filtered_data = pipeline.pipeline(
        value=test_data,
        function_pipeline=(
            filter_odd,
            filter_gt5
        )
    )
    assert filtered_data == [7, 9]

def test_tracer(capsys):
    @tracer.trace
    def show_args_and_kwargs(*args, **kwargs):
        return args, kwargs
    
    assert show_args_and_kwargs(10) == ((10,), {})
    captured = capsys.readouterr()
    expected_out = [
        '################################################################\n',
        'Tracing show_args_and_kwargs()...\n',
        'args=\t(10,)\n\n',
        'kwargs=\t{}\n\n',
        'result=\t((10,), {})\n\n',
        '################################################################\n'
    ]
    assert captured.out == ''.join(expected_out)

    assert show_args_and_kwargs(color='Red') == ((), {'color': 'Red'})
    captured = capsys.readouterr()
    expected_out = [
        '################################################################\n',
        'Tracing show_args_and_kwargs()...\n',
        'args=\t()\n\n',
        'kwargs=\t{\'color\': \'Red\'}\n\n',
        'result=\t((), {\'color\': \'Red\'})\n\n',
        '################################################################\n'
    ]
    assert captured.out == ''.join(expected_out)

    assert show_args_and_kwargs(10, 200, color='Blue', type='Dog') == ((10, 200), {'color': 'Blue', 'type': 'Dog'})
    captured = capsys.readouterr()
    expected_out = [
        '################################################################\n',
        'Tracing show_args_and_kwargs()...\n',
        'args=\t(10, 200)\n\n',
        'kwargs=\t{\'color\': \'Blue\', \'type\': \'Dog\'}\n\n',
        'result=\t((10, 200), {\'color\': \'Blue\', \'type\': \'Dog\'})\n\n',
        '################################################################\n'
    ]
    assert captured.out == ''.join(expected_out)

def test_yaml_reader():
    test_data = yaml_reader.read('queasy/tests/data/test_data.yml')
    assert test_data == 'This is a test data.'