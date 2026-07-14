
# def wrap_text(s, limit):
#     """
#     This function allows the user to wrap simple text s (no punctuation)
#     according to a character limit, as you might seen in Google docs or MS Word.
#     """
#     print("function working")
#     if limit < 22:
#         return "limit needs to be at least 22 for this exercise"
    
#     testing_max = max([len(x) for x in s.split()])
#     print(f"testing max: {testing_max}")
#     if max([len(x) for x in s.split()]) > limit:
#         return "can't wrap as at least one word is longer than the limit"
    
#     lines = []
#     #this will return a list of strings:
#     words = s.split()
#     count_so_far = 0
#     line_so_far = ""
#     while words:
#         #pop without parameter will pop out last word, so we change this to have 1 in it instead of nothing:
#         word = words.pop()
#         #plus 1 here is for the extra space between words:
#         if len(word)+1+count_so_far <= limit:
#             #by adding " " before the +word, you will have a space before the first word instead of only between one word and another, so we will
#             #essentially be starting with a needless space:

#             line_so_far += " " + word
#             count_so_far += len(word) + 1
#         else:
#         # we are missing word in this, we pop it out and essentially do not append it
#             lines.append(line_so_far)
#             line_so_far = ""
#             count_so_far = 0
#     # since the last line will never reach the limit, this tries to make sure that the last line is appended even though it doesn't reach that limit:
#     if line_so_far != "":
#         lines.append(line_so_far)
#     #prints each line:
#     for line in lines:
#         print(line)

# result = wrap_text("Hello Andy and Gizmo how are you", 23)
# print(f"result {result}")