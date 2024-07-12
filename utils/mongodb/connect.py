from pymongo import MongoClient

from data.config import MONGO_DB


class DataBase:  # sinxron mongo db ga ulanish ishlatilgani yo'q
    def __init__(self):
        cluster = MongoClient(MONGO_DB)

        self.db = cluster["Joylinks_Grant_Bot"]
        self.users = self.db["Users"]
        self.questions = self.db["Questions"]

        self.questions_count = len(list(self.questions.find({})))

    def get_user(self, chat_id):
        user = self.users.find_one({"chat_id": chat_id})

        if user is not None:
            return user

        user = {
            "chat_id": chat_id,
            "is_passing": False,
            "is_passed": False,
            "question_index": None,
            "answers": []
        }

        self.users.insert_one(user)

        return user

    def set_user(self, chat_id, update):
        self.users.update_one({"chat_id": chat_id}, {"$set": update})

    def get_one_question(self, index):
        return self.questions.find_one({"id": index})

    def get_list_questions(self, index):

        return [self.questions.find_one({"id": i}) for i in index]

    def get_questions_all(self):
        from random import sample
        list = []
        for i in self.questions.find({}):
            list.append(i['id'])
        random_ = sample(list, 8)
        return random_
