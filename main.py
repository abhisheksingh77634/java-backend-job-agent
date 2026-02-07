from job_sources import JOB_SOURCES

from job_scraper import fetch_jobs

from matcher import score_job

from emailer import send_email

results = []

for country, urls in JOB_SOURCES.items():

    for url in urls:

        jobs = fetch_jobs(url)

        for job in jobs:

            score = score_job(job["title"])

            if score >= 40:

                results.append({

                    "title": job["title"],

                    "link": job["link"],

                    "score": score,

                    "country": country

                })

results = sorted(results, key=lambda x: x["score"], reverse=True)[:15]

if results:

    send_email(results)
 
