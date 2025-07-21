""" Experimenting with fetching from db """

from database import query

response0 = query.fetch_jobs("adzuna", 5)
response1 = query.fetch_jobs("test", 2)

print(response0[0])
print(response0[2])
print(response1[0])