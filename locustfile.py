from locust import HttpUser, TaskSet, task, constant_pacing, constant
import random
import datetime

post_user_number = 6
get_user_number = 1
post_request_time = 0.5
get_request_time = 0.5

class POSTUser(HttpUser):
    weight = post_user_number
    wait_time = constant_pacing(post_request_time) 
    def on_start(self):
        self.name = random.randint(1,1000)
    @task
    def post_user(self):
        self.client.post('save_user_status/', data = {'name':self.name,'status':'soso'})


class GETUser(HttpUser):
    weight = get_user_number
    wait_time = constant_pacing(get_request_time)
    @task
    def get_all_last_data(self):
        self.client.get('get_all_last_data/')
        print(datetime.datetime.now())
