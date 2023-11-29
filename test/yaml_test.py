import yaml

d = {
    'generate_quality_monthly_report_and_send_email': {
        'jobs': [
            {
                'generate_report_and_send': {
                    {'time': 'x'},
                    {'user': 'y'},
                    {'command': 'z'}
                }
            }
        ]
    }
}

print(yaml.dump(d))
