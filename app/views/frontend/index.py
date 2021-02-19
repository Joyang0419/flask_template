from . import frontend


@frontend.route('/', methods=['GET', 'POST'])
def index():
    return 'I am frontend'
