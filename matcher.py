from resume_keywords import KEYWORDS, VISA_KEYWORDS
def score_job(title):
   score = 0
   for kw in KEYWORDS:
       if kw in title:
           score += 8
   for visa_kw in VISA_KEYWORDS:
       if visa_kw in title:
           score += 20
   return min(score, 100)
