from locust import HttpUser, TaskSet, task, constant_pacing

# class WebsiteTasks(TaskSet): #TaskSet
#     @task
#     def get_all_last_data(self):
#         self.client.get('/get_all_last_data')
    
#    # @task
#    # def get_last_data(self):
#    #     self.client.get('/get_last_data')
        
# class WebsiteUser(HttpUser): #Locust
#     task_set = WebsiteTasks
#     min_wait = 100 #ms
#     max_wait = 500
class WebsiteUser(HttpUser):
    wait_time = constant_pacing(0.5) # 等待達到該時間後執行下一任務
    @task
    def post_user1(self):
        self.client.post('save_user_status/', data = {'name':'user1','status':'good'})
    @task
    def post_user2(self):
        self.client.post('save_user_status/', data = {'name':'user2','status':'soso'})    
    @task
    def post_user3(self):
        self.client.post('save_user_status/', data = {'name':'user3','status':'bad'})
    @task
    def post_user4(self):
        self.client.post('save_user_status/', data = {'name':'user4','status':'good'})
    @task
    def post_user5(self):
        self.client.post('save_user_status/', data = {'name':'user5','status':'soso'})
    @task
    def post_user6(self):
        self.client.post('save_user_status/', data = {'name':'user6','status':'bad'})
    # @task
    # def get_all_last_data(self):
    #     self.client.get('get_all_last_data/')
    # @task
    # def get_last_data(self):
    #     self.client.get('get_last_data/allen')
    # @task
    # def get_save_user_status(self):
    #     self.client.get('save_user_status/')

# locust --host=http://163.13.133.67:666/
