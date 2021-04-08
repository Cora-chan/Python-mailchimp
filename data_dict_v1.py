# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import pandas as pd
import redis  as rd

#data=pd.read_csv("x_book.csv")
#print(data)

pool = rd.ConnectionPool(host='redissuper.bfjfunds.com.au',port=6379,db=0,password="rockydrew123");
r=rd.Redis(connection_pool=pool);

keys=r.keys();

print(r.get("SUPER-Order:9548797"));

#print(keys);


# pipe = r.pipeline();
# pipe_size=100000;

# len=0;
# key_list=[];
# print(r.pipeline());
# keys=r.keys();
# for key in keys:
#     key_list.append(key);
#     pipe.get(key);
#     if len<pipe_size:
#         len+=1;
#     else:
#         for(k,v)in zip(key_list,pipe.execute()):
#             print (k,v);
#         len=0;
#         key_list=[];

# for (k,v)in zip(key_list, pipe.execute()):
#     print (k,v);
        
# pipe = r.pipeline();
# pipe_size=100000;

# len=0;
# key_list=[];
# print(r.pipeline());
# keys=r.keys();
# for key in keys:
#     key_list.append(key);
#     pipe.get(key);
#     if len<pipe_size:
#         len+=1;
#     else:
#         for(k,v)in zip(key_list,pipe.execute()):
#             print (k,v);
#         len=0;
#         key_list=[];

# for (k,v)in zip(key_list, pipe.execute()):
#     print (k,v);














