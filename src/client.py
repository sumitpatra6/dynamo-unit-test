from src.service import Service

def create_data():
    service = Service()
    service.create_date()
    print("Done")


def get_data():
    service = Service()
    service.get_data()


def query():
    service = Service()
    service.query("56b72315513547d688849c2a858ef9cd")


if __name__ == '__main__':
    query()