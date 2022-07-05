#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    ngx_clcn = client.logs.nginx

    lg_cnt = ngx_clcn.count_documents({})
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    print("{} logs".format(lg_cnt))
    print("Methods:")

    for mt in methods:
        print("\tmethod {}: {}".format(mt, ngx_clcn.count_documents(
            {"method": mt})))
    print("{} status check".format(ngx_clcn.count_documents(
        {"path": "/status"})))
