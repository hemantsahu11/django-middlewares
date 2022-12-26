
 # we have function method of generating middleware also but that approach is legacy
class DemoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response        # settting response
        self.num_exceptions = 0

    def __call__(self, request):
        print("middleware called ")
        # print(dir(request))
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # logic executed before a call to view
        # gives access to the view itself and arguments
        print(f'view name : {view_func.__name__}')


    # def process_template_response(self, request, response):
    #     # here we can declare templates for showing data
    #     pass


    def process_exception(self, request , exception):
        self.num_exceptions += 1
        print("Exceptions count : {self.num_exceptions}")   # if any exception raised then exception count will be increased ++++1