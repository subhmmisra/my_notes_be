class BadRequestErrorMixin(object):
    def get_api_response(self, url, request_method="get", request_body=None, **kwargs):
        return getattr(self.client, request_method)(url, **kwargs)
    
    def run_required_fields_tests(
        self, url, request_method, erroneous_fields_set=None, request_body={}
    ):
        response = self.get_api_response(
            url, request_method=request_method, request_body=request_body
        )
        response_error_fields = set(error["field"] for error in response.data["errors"])

        self.assertEqual(response.status_code, 400)
        if erroneous_fields_set:
            self.assertSetEqual(erroneous_fields_set, response_error_fields)
        else:
            self.assertEqual(len(response.data["errors"]), 1)

        return response
