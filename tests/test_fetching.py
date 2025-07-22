""" Experimenting with fetching from db """

from database import query

response0 = query.fetch_jobs("adzuna", 5)
response1 = query.fetch_jobs("test", 2)

# print(response0[0])
# print(response0[2])
# print(response1[0])

response2 = query.delete_jobs("test", 1)
# print(response2)

response3 = query.delete_filter_jobs("adzuna", 9, "Software Developer")
print(response3)