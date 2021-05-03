import logging
import time
import threading
import dataHandle as dh
import mongoDataInteract as mdb


if __name__ == "__main__":
    print(mdb.checkDataBaseExistance(None))