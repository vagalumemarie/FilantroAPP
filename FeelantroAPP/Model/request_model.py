import requests

class RequestModel:
    def post_data_registration_volunteer(self, data):
        api_code = "https://savvyrobin.backendless.app/api/data/registration_for_volunteer"
        post_data = requests.post(api_code, json=data)
        return post_data


    def get_data_registration_volunteer(self,user_email):
        get_data = requests.get(f"https://savvyrobin.backendless.app/api/data/registration_for_volunteer?property=email&property=objectId")
        data = get_data.json()
        for dicti in data:
           if dicti["email"] == user_email:
                get_user_data = requests.get(f"https://savvyrobin.backendless.app/api/data/registration_for_volunteer/{dicti['objectId']}")
                user_data = get_user_data.json()
                return user_data


    def post_data_registration_users(self, data):
        api_code = "https://savvyrobin.backendless.app/api/data/registration_for_users"
        post_data = requests.post(api_code, json=data)
        return post_data


    def get_data_registration_users(self, user_email):
        get_data = requests.get(f"https://savvyrobin.backendless.app/api/data/registration_for_users?property=email&property=objectId")
        data = get_data.json()
        for dicti in data:
           if dicti["email"] == user_email:
                get_user_data = requests.get(f"https://savvyrobin.backendless.app/api/data/registration_for_users/{dicti['objectId']}")
                user_data = get_user_data.json()
                return user_data


    def post_data_request(self, request):
        api_code = "https://savvyrobin.backendless.app/api/data/requests"
        post_data = requests.post(api_code, json=request)
        return post_data


    def get_own_request(self, user_email):
        get_data = requests.get(
            f"https://savvyrobin.backendless.app/api/data/requests?property=email&property=objectId")
        data = get_data.json()
        for dicti in data:
            if dicti["email"] == user_email:
                get_user_data = requests.get(
                    f"https://savvyrobin.backendless.app/api/data/requests/{dicti['objectId']}")
                user_data = get_user_data.json()
                return user_data


    def get_all_requests(self):
        get_requests = requests.get(f"https://savvyrobin.backendless.app/api/data/requests?property=email&property=objectId&property=problem_description&property=status&property=photo_of_your_situation&property=location&property=assistance_category&property=term_of_execution&property=updated")
        request = get_requests.json()
        return request

    def delete_data_request(self, user_email):
        api_code = "https://savvyrobin.backendless.app/api/data/requests"
        post_data = requests.get(api_code)
        request = post_data.json()
        for request in request:
            if request["email"] == user_email:
                edit_request = requests.delete(f"https://savvyrobin.backendless.app/api/data/requests/{request['objectId']}")
                return edit_request


    def get_requests_volunteer(self):
        get_data = requests.get("https://savvyrobin.backendless.app/api/data/requests")
        data = get_data.json()
        empty_requests = []
        for item in data:
            if item["volunteer_phone"] == None:
                empty = requests.get(f"https://savvyrobin.backendless.app/api/data/requests/{item['objectId']}").json()
                empty_requests.append(empty)
        return empty_requests

    def edit_data_request(self, data, user_email):
        api_code = "https://savvyrobin.backendless.app/api/data/requests"
        post_data = requests.get(api_code)
        request = post_data.json()
        for request in request:
            if request["email"] == user_email:
                edit_request = requests.put(f"https://savvyrobin.backendless.app/api/data/requests/{request['objectId']}", json=data)
                return edit_request

    def get_own_request_volunteer(self, phone):
        get_data = requests.get(f"https://savvyrobin.backendless.app/api/data/requests")
        data = get_data.json()
        volunteer_requests = []
        for dicti in data:
            if dicti["volunteer_phone"] == phone:
                get_user_data = requests.get(
                    f"https://savvyrobin.backendless.app/api/data/requests/{dicti['objectId']}").json()
                volunteer_requests.append(get_user_data)
        return volunteer_requests

    def take_request(volunteer_number):
        get_data = requests.get(f"https://savvyrobin.backendless.app/api/data/requests")
        data = get_data.json()
        for request in data:
            if request["volunteer_phone"] == None:
                edit_request = requests.put(
                    f"https://savvyrobin.backendless.app/api/data/requests?property=volunteer_phone",
                    json={"volunteer_phone": volunteer_number})
                return edit_request



