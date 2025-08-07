from database import query
import constants

constants.TABLE = "test_jobs"
query.delete_all_jobs()
