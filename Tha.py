import autolike
url = "https://www.facebook.com/profile.php?id=61556178773260" # any Facebook URL
run_time = 30 # time in seconds
like_result_dict = autolike.facebook_autolike(url, run_time)
print(like_result_dict)
