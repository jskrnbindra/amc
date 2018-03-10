APPOINTMENT_TYPES = [
    'Joints pain',
    'Baldness',
    'Migraine',
    'Obesity',
    'Piles',
    'Infertility',
    'Sexual Problem',
    'Psoriasis',
    'High BP',
    'High Cholesterol',
    'Breathing Difficulty',
    'Hyperacidity',
    'Hepatitis B&C',
    'Skin Disorder',
    'Diabetes',
    'Paralysis',
    'Depression',
    'Cervical Spondylitis',
    'Gynaecology Problems'
]

EMAIL_TEMPLATES = {
    'new_subscriber': {
        'from': 'no-reply@ayurvedaludhiana.com',
        'subject': 'Welcome to Ayurveda Multispeciality Centre',
        'body': 'Hi %s, welcome to Ayurveda Multispeciality Centre. This is just a test.'
    },
    'new_subscriber_admin': {
        'from': 'admin@ayurvedaludhiana.com',
        'subject': 'New subscriber - %s',
        'body': '%s just subscribed to our mailing list. This is just a test of our automated mail alerts.',
        'to': ['bindrajskrn@yahoo.com', 'jskrnbindra@gmail.com']
    },
    'new_appointment': {
        'from': 'no-reply@ayurvedaludhiana.com',
        'subject': 'Your appointment has been confirmed',
        'body': 'Hi %s, your appointment has been confirmed. This is just a test.'
    },
    'new_appointment_admin': {
        'from': 'admin@ayurvedaludhiana.com',
        'subject': 'New appointment - %s',
        'body': 'A new appointment has been made by %s. This is just a test of our automated mail alerts.',
        'to': ['bindrajskrn@yahoo.com', 'jskrnbindra@gmail.com']
    }
}
