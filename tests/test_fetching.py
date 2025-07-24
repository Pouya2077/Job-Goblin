""" Experimenting with fetching from db """

from database import query

response = query.fetch_jobs("adzuna", 10)
# print(response)

response = query.fetch_filter_jobs("adzuna", 2, None, None, "Ontario, Canada")
print(response)

# response = query.delete_all_jobs()
# print(response)

# response = query.delete_all_jobs("test")
# print(response)

# response = query.delete_jobs("adzuna", 4)
# print(response)

# response = query.delete_filter_jobs("adzuna", 0, "Software Developer,", "vTech Solution", None)
# print(response)