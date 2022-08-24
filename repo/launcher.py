from repo.mongo_repository import MongoRepository

if __name__ == '__main__':
    mr = MongoRepository()
    all = mr.find_all()

    for a in all:
        print(a)